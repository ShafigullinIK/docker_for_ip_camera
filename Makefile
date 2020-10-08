build:
	docker build -t shafigullinik/opencv .

run:
	docker run -it --volume $(shell pwd)/src:/usr/src/app --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" --env="DISPLAY" shafigullinik/opencv python app_ip.py

bash:
	docker run -it --volume $(shell pwd)/src:/usr/src/app --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" --env="DISPLAY" shafigullinik/opencv bash

web_camera:
	docker run -it --volume $(shell pwd)/src:/usr/src/app --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" --device=/dev/video0:/dev/video0 --env="DISPLAY" shafigullinik/opencv bash 