#!/bin/bash
{
  if (
    nc localhost 50000 </dev/null
    echo $?
  ); then
    previous_container=$(docker ps -a | grep -e join_lists)
    if [ -z ${previous_container} ]; then
      echo 'Container unset, creating...'
    else
      echo "Removing previous container"
      docker stop join_lists
      docker rm join_lists
      echo 'Previous container removed. Creating a new one...'
    fi
    docker build -t join_lists .
    docker run -d -p 50000:50000 --name join_lists join_lists
    echo "All done! Enter here: http://localhost:50000/"
    while true; do
      docker logs join_lists
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
