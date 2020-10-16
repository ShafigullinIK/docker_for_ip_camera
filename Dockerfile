FROM conda/miniconda3
# FROM nvidia/cuda:10.2-base

RUN conda update -n base -c defaults conda
RUN conda config --add channels conda-forge && conda config --set channel_priority strict

RUN conda install -c conda-forge opencv

RUN apt update && apt install -y libgl1-mesa-glx

RUN pip install torch torchvision
RUN conda install -c conda-forge albumentations

RUN mkdir -p /bus
WORKDIR /bus/camera

ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility
ENV NVIDIA_REQUIRE_CUDA "cuda>=8.0"

CMD [ "nvidia-smi" ]