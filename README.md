# Join Lists

Pequeño repositorio que implementa en un Docker una aplicación que toma dos listas con periodos (cada periodo con fecha inicio, fecha fin y propiedades adicionales, distintas en cada lista) y los unifica de manera que los periodos comunes, agrupen las distintas propiedades adicionales. 

Ejemplo:


~~~~
Lista 1:

 Start: 01-01-2021, End: 03-01-2021, Atributo1: 1
 Start: 06-01-2021, End: 06-01-2021, Atributo1: 2
 Start: 07-01-2021, End: 09-01-2021, Atributo1: 2
 
 
 Lista 2:
 
 Start: 01-01-2021, End: 01-01-2021, Atributo2: A
 Start: 06-01-2021, End: 08-01-2021, Atributo2: B

 
 Salida:
 
 Start: 01-01-2021, End: 01-01-2021, Atributo1: 1, Atributo2: A
 Start: 02-01-2021, End: 03-01-2021, Atributo1: 1
 Start: 06-01-2021, End: 08-01-2021, Atributo1: 2, Atributo2: B
 Start: 09-01-2021, End: 09-01-2021, Atributo1: 2
 

~~~~

Para ejecutar el Docker, basta con tener instalado docker en la máquina y ejecutar el script del directorio raiz:

~~~~
sh start.sh
~~~~

Después, se escribirá en el Navegador: http://localhost:50000/ y se obtendrá la salida esperada. 


Me he tomado la libertad de modificar levemente el comportamiento esperado para las salidas. Se encontrarán propiedades llamadas 'custom_values' que contienen el listado de variables que aplican en cada periodo. En la entidad PeriodsEntity, gestioné esas propiedades que eran diferentes entre listas, dentro de la propiedad "custom_values". Al ser esta propiedad un diccionario, puedo añadir las variables que vayan existiendo de manera dinámica. Una solución más sencilla podría haber sido hardcodear 'type' y 'value' como propiedades de la clase, pero preferí generarlas así y gestionar las propiedades de manera dinámica durante el código, para generar un código que fuera más flexible a cambios.


### El código
Se ha implementado un pseudo sistema de Clean Architecture. Se utilizan Use Cases para contener la lógica de negocio y Adaptors y Presenters para la modificación estructural de los datos que se van a manejar. Se definió una Entity intentando no definirle lógica, a lo sumo algunas operaciones primitivas de la entidad.
Dentro de los Use Case, se creó uno para optimizar las listas antes de combinarlas. compact_list_use_case.py contiene ese caso de uso y es porque se vieron casos en los que las entradas por defecto podían optimizarse, antes de su procesado.
El Use Case principal, CombineListsUseCaseTestCase, recorre la primera lista de inputs, y va cotejando el elemento actual con los sucesivos elementos de la otra lista, en el momento que se aplica por completo el elemento actual de la primera lista, se pasa al siguiente y se sigue la segunda lista por donde iba.
Al final, dos bucles recogen los elementos sobrantes al final de alguna de las listas, con respecto a la otra.

Durante la comprobación de elementos de ambas listas, se pudo observar distintos tipo de relación:___

Elemento de lista1 empieza y acaba antes que elemento comparado de lista2 --> se añade a la lista el elemento de lista1 por completo

Elemento de lista2 empieza y acaba antes que elemento comparado de lista1 --> se añade a la lista el elemento de lista2 por completo

Elemento de lista1 empieza antes que el elemento comparado de lista2 --> se añade a la lista el elemento de lista1 hasta la fecha que empieza el elemento de lista2 combinando propiedades de ambos

Elemento de lista2 empieza antes que el elemento comparado de lista1 --> se añade a la lista el elemento de lista2 hasta la fecha que empieza el elemento de lista1 combinando propiedades de ambos

Elemento de lista1 empieza a la vez pero acaba antes del elemento comparado de lista2 --> se añade a la lista el elemento de lista1 y se cambia la fecha de inicio elemento de lista2 a la de fin del de lista1 combinando propiedades de ambos

Elemento de lista2 empieza a la vez pero acaba antes del elemento comparado de lista1 --> se añade a la lista el elemento de lista2 y se cambia la fecha de inicio elemento de lista1 a la de fin del de lista2 combinando propiedades de ambos

Elemento de lista1 empieza a la vez pero acaba despues del elemento comparado de lista2 --> se añade a la lista el elemento de lista2 y se cambia la fecha de inicio elemento de lista1 a la de fin del de lista2 combinando propiedades de ambos

Elemento de lista2 empieza a la vez pero acaba despues del elemento comparado de lista1 --> se añade a la lista el elemento de lista2 y se cambia la fecha de inicio elemento de lista2 a la de fin del de lista1 combinando propiedades de ambos

Ambos son iguales --> se añade a la lista uno de los dos, combinando las propiedades de ambos y se pasa al siguiente de cada lista.

Y esa es la lógica que sigue el caso de uso principal.



### Los Tests

Hay 10 tests unitarios. Normalmente las Entities no tienen lógica y no deben tener tests por sí mismas, pero decidí ser laxo en ese sentido en la interpretación que hace Clean Architecture de las Entities.
No hay mockeos, y el test de la clase CombineListsUseCaseTestCase podría haber mockeado las llamadas a los Use Cases de CompactListUseCase. Aligerando el tests y haciendolo independiente de la lógica de esos Use Cases. Al no hacerlo, se puede considerar más como un Main Path test o de Integración interna.


### Posibles mejoras

 - Implementar un entrypoint que admita entradas diferentes y se puedan probar más casos.
 - Modificar el output para que sea exacto al solicitado inicialmente.