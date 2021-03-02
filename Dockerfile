FROM tiangolo/uwsgi-nginx-flask:python2.7
ENV FLASK_APP app/myproject.py
WORKDIR /app
COPY . /app
EXPOSE 50000
ENTRYPOINT [ "python" ]
CMD [ "myproject.py" ]
