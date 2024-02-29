FROM python:3.9
RUN pip install torch==1.13.1 torchvision==0.14.1 --extra-index-url https://download.pytorch.org/whl/cu113

ENV HOME /workspace
WORKDIR $HOME
ARG DEBIAN_FRONTEND=noninteractive

# general system dependencies
RUN apt update
RUN apt install -y git
RUN apt install libgl1-mesa-glx -y
RUN apt install libglib2.0-0 -y

# Semantic-SAM dependencies:
RUN pip install 'git+https://github.com/MaureenZOU/detectron2-xyz.git'
RUN pip install git+https://github.com/cocodataset/panopticapi.git
RUN git clone https://github.com/UX-Decoder/Semantic-SAM
WORKDIR $HOME/Semantic-SAM
RUN pip install -r requirements.txt

# WORKDIR $HOME
# RUN git clone https://github.com/facebookresearch/Mask2Former.git
# WORKDIR $HOME/Mask2Former/mask2former/modeling/pixel_decoder/ops
# ENV CUDA_HOME=/usr/local/cuda

# this repository stuff:
WORKDIR $HOME
ENV REPODIR $HOME/ponti_IA
RUN git clone https://github.com/kauevestena/ponti_IA.git
WORKDIR $REPODIR
RUN pip install -r requirements.txt