FROM ubuntu:22.04
WORKDIR /home
## Configure Time Zone
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America\Mexico_City

## Update SO and dependencies
# review package actual version https://packages.ubuntu.com/

# for package ffmpeg libsm6 libxext6 reference https://stackoverflow.com/questions/55313610/importerror-libgl-so-1-cannot-open-shared-object-file-no-such-file-or-directo
RUN apt-get -y update && apt-get install -y --no-install-recommends tzdata unzip curl nano wget iputils-ping telnet python3-pip tesseract-ocr tesseract-ocr-spa ffmpeg libsm6 libxext6 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip

## Installing code depedencies
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

## Copy code
COPY ./app ./app
# WORKDIR /home/app

## for realtime test local changes files
RUN mkdir /home/realtime

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
#CMD tail -f /dev/null