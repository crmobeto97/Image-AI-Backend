# Create network for environment

this folder have the scripts for create the diferent networks for diferent environments

## Documentation

base on:

1. ChatGPT-3.5

## Docker Network

### Quick Starter

#### Create Network

```bash
./create_docker_network.sh
```

#### Review

export name like variable environment

```bash
export network_name="image-ia"
```

list docker networks

```bash
docker network ls
```

get ocr-receipt-dev network details

```bash
docker network inspect $network_name
```

#### Delete Network

```bash
docker network rm $network_name
```
