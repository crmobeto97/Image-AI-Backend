#!/bin/bash

# Function to check if a Docker network exists
network_exists() {
  docker network inspect "$1" > /dev/null 2>&1
}
network_name="image-ia"
# Create the main network with a specified IP range if it doesn't exist
if network_exists "$network_name"; then
  echo "Network '$network_name' already exists."
else
  docker network create --driver bridge \
    --subnet 10.0.0.0/24 \
    --gateway 10.0.0.1 \
    $network_name
  echo "Network '$network_name' created successfully."
fi

# Confirm the networks have been created
echo "Docker networks status:"
docker network ls

# Inspect the created networks for verification
# echo "Inspecting 'ocr-receipt-dev' network:"
# docker network inspect ocr-receipt-dev


