# Image-AI-Backend

this project is for create for backend to Image Models input IA

## Technology Stack

Tecnologies used in the project (including cloud platform)

1. Ubuntu
1. Docker
1. Python
    * [FastAPI](https://fastapi.tiangolo.com)

## Project Structure

```
myproject/
├── app/
│   └── routes/
│       └── detect.py
├── ia_model/
│   ├── base_detector.py
│   └── darknet_detector.py
├── utils/
│   └── image_utils.py
├── config.py
├── requirements.txt
├── README.md
└── main.py
```

## Environment Variable

All configurable variables are centralized in `config.py`:

```python
from pathlib import Path
from ia_model.darknet_detector import DarknetDetector  # Replace this if you switch models

# Image folders
TEMP_DIR = Path("/temp")
RAW_FOLDER = Path("raw")
PROCESSED_FOLDER = Path("processed")

# Model injection
MODEL = DarknetDetector()

# Model config
GENERATED_FILENAME = "predictions.jpg"
MODEL_WORKING_DIR = Path("ia_model/darknet")
OUTPUT_SUFFIX = "-processed"
```

To switch to another model, replace `DarknetDetector` with your own detector in `config.py` and adjust paths or suffixes as needed.

---

## 🔧 Switching to a Different AI Model

The default model used is YOLOv3 via the [pjreddie/darknet](https://github.com/pjreddie/darknet) repository.

To change the model, follow these steps:

### 1. **Update the Dockerfile**

Replace this section:

```dockerfile
## Copy Yolo IA Model 
RUN mkdir ia_model
WORKDIR /home/ia_model
RUN git clone https://github.com/pjreddie/darknet
WORKDIR /home/ia_model/darknet
RUN make
RUN wget https://pjreddie.com/media/files/yolov3.weights
```

With setup instructions for your new model. For example:

```dockerfile
RUN git clone https://github.com/your-org/your-model.git
WORKDIR /home/ia_model/your-model
RUN make  # or any custom setup
```

### 2. **Create or Update Your Detector Class**

Implement a detector class in `ia_model/your_detector.py` inheriting from `base_detector.py`.
Make sure to define a `.detect(image_path)` method.

### 3. **Update config.py**

Point to the new detector class and model-specific settings:

```python
from ia_model.your_detector import YourDetector
MODEL = YourDetector()
GENERATED_FILENAME = "output.jpg"
MODEL_WORKING_DIR = Path("ia_model/your-model")
OUTPUT_SUFFIX = "-result"
```

Done — no need to modify your route logic in `detect.py`.

---


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
            cd realtime/src/ 
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
