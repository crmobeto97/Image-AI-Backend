# Image-AI-Backend

this project is for create for backend to Image Models input IA

## Technology Stack

Tecnologies used in the project (including cloud platform)

1. Ubuntu
1. Docker
1. Python
    * [FastAPI](https://fastapi.tiangolo.com)

## Environment Variable


### Quick Start

1.  Create the network follow  [README.md](./network/README.md) in [network](./network/)

    1.  Enter in  [network](./network/)
    1.  Run script [create_docker_network.sh](./network/create_docker_network.sh) 

    if you creatred before only run in your terminal

    1. network_name="image-ia"


1.  Build and Run python app container
    1.  Build insided the folder [src](./src/) with the command:
        ```bash
        docker build . -t python-1
        ```
    1.  Run the Container App:
        *   For interactive terminal session with the host local files (for modification and test in real team, not need re-build) run
            Linux
            ```bash
            $ docker run -it --rm --name=backend --network $network_name --ip 10.0.0.3 -p 8000:8000 -v $(pwd):"/home/realtime" python-1 bash
            ```
            PowerShell
            ```bash
            $ docker run -it --rm --name=backend --network "image-ia" --ip "10.0.0.3" -p 8000:8000 -v ${PWD}:"/home/realtime" python-1 bash
            ```

            or

            ```bash
            $ docker run -it \
                --rm \
                --name backend \
                --network $network_name \
                --ip 10.0.0.3 \
                -p 8000:8000 \
                -v $(pwd):"/home/realtime" \
                python-1 bash
            ```
            For run the application inside the terminal run:

            ```bash
            uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
            ```

        *   For non interactive run

            ```bash
            docker run --rm -d --name=backend -p 8000:8000 python-1
            ```

        flags:

        * `--rm`&nbsp;&nbsp;&nbsp;&nbsp;    Erase the docker after stop
        * `-d`&nbsp;&nbsp;&nbsp;&nbsp;      Run container in background and print container ID
        * `-it`&nbsp;&nbsp;&nbsp;&nbsp;      Interactive session
        * `--name`&nbsp;&nbsp;&nbsp;&nbsp;   Containers name
        * `-p`&nbsp;&nbsp;&nbsp;&nbsp;       Publish a container's port(s) to the host (e.g., `-p <host port>:<container port>`)


        more information flags in [docker container run options](https://docs.docker.com/reference/cli/docker/container/run/#options)

<!-- Bibliografy -->
[1]: https://example          "example documentation"
[2]: https://pjreddie.com/darknet/yolo/ "YOLO: Real-Time Object Detection"
