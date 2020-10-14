FROM conda/miniconda3

RUN conda update -n base -c defaults conda
RUN conda config --add channels conda-forge && conda config --set channel_priority strict

RUN conda install -c conda-forge opencv

RUN apt update && apt install -y libgl1-mesa-glx

RUN mkdir -p /bus
WORKDIR /bus/camera

CMD [ "python", "/bus/camera/app.py" ]