#!/bin/bash

# Function to check if a Docker network exists
network_exists() {
  docker network inspect "$1" > /dev/null 2>&1
}

# Create the main network with a specified IP range if it doesn't exist
if network_exists "ocr-receipt-dev"; then
  echo "Network 'ocr-receipt-dev' already exists."
else
  docker network create --driver bridge \
    --subnet 10.0.0.0/24 \
    --gateway 10.0.0.1 \
    ocr-receipt-dev
  echo "Network 'ocr-receipt-dev' created successfully."
fi

# Confirm the networks have been created
echo "Docker networks status:"
docker network ls

# Inspect the created networks for verification
# echo "Inspecting 'ocr-receipt-dev' network:"
# docker network inspect ocr-receipt-dev


