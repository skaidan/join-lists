#!/bin/bash
{
    if (nc localhost 50000 < /dev/null; echo $?); then
        previous_container=`docker ps -a | grep -e real_sandbox`
        if [ -z ${previous_container} ]; then
            echo 'Container unset, creating...'
        else
            echo "Removing previous container"
            docker stop real_sandbox
            docker rm real_sandbox
            echo 'Previous container removed. Creating a new one...'
        fi
        docker build -t real_sandbox .
        docker run -d -p 50000:50000  --name real_sandbox  real_sandbox
        echo "All done! Enter here: http://localhost:50000/"
        while true
        do
            docker logs real_sandbox
            sleep 10
        done
    else
        echo "The port 50000 is already in use. Please stop the process in that port and try again"

    fi
} || {
    # exit on error
    echo 'There was an error setting up the Docker container'
    exit 1
}
