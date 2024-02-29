FROM python:3.9
RUN pip install torch==1.13.1 torchvision==0.14.1 --extra-index-url https://download.pytorch.org/whl/cu113

RUN apt update
RUN apt install -y git

ENV HOME /workspace
WORKDIR $HOME

RUN pip install 'git+https://github.com/MaureenZOU/detectron2-xyz.git'
RUN pip install git+https://github.com/cocodataset/panopticapi.git
RUN git clone https://github.com/UX-Decoder/Semantic-SAM
WORKDIR $HOME/Semantic-SAM
RUN pip install -r requirements.txt

# this repository stuff:
WORKDIR $HOME
ENV REPODIR $HOME/ponti_IA
RUN git clone https://github.com/kauevestena/ponti_IA.git
WORKDIR $REPODIR
RUN pip install -r requirements.txt