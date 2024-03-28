
# First working version at 24/12/2023:
FROM pytorch/pytorch:latest

# prevent apt from hanging
ARG DEBIAN_FRONTEND=noninteractive

ENV HOME /workspace
WORKDIR $HOME

# general system dependencies:
RUN apt update
RUN apt install -y git
RUN apt install libgl1-mesa-glx -y
RUN apt install libglib2.0-0 -y

# dependency: lavis:
RUN pip install salesforce-lavis

# this repository stuff:
WORKDIR $HOME
ENV REPODIR $HOME/ponti_IA
RUN git clone https://github.com/kauevestena/ponti_IA.git
WORKDIR $REPODIR
RUN pip install -r requirements.txt

# saving frozen requirements:
RUN pip list --format=freeze > frozen_requirements.txt

