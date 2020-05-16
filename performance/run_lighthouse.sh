#!/usr/bin/env bash

URL=$1
PORT=$2
SESSION_ID=$3

echo "Find which container is running the current test..."
for container in $(docker ps -a -q); do
  log=$(docker logs "${container}")

  # if log contains SESSION_ID, then set CONTAINER_ID and break
  if [[ "${log}" == *"$SESSION_ID"* ]]; then
    echo "Found Container ID: ${container}"
    export CONTAINER_ID="${container}"
    break
  fi
done

# get container name # Commented out for now
# CONTAINER_NAME=$(docker inspect "${CONTAINER_ID}" --format='{{json .Name}}')

echo "$ docker exec ${CONTAINER_NAME} sudo lighthouse ${URL} --port ${PORT} ..."
docker exec "${CONTAINER_ID}" sudo lighthouse "${URL}" \
    --port "${PORT}" \
    --emulated-form-factor "desktop" \
    --only-categories "performance" \
    --output "json"
