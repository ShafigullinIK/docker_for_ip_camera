build:
	docker build -t shafigullinik/opencv .

run:
	docker run -it --volume $(shell pwd)/src:/usr/src/app --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" --env="DISPLAY" shafigullinik/opencv python app_copy.py

bash:
	docker run -it --volume $(shell pwd)/src:/usr/src/app --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" --env="DISPLAY" shafigullinik/opencv bash

camera1:
	docker run -it --volume $(shell pwd)/camera_1:/bus/camera --volume $(shell pwd)/src:/bus/app --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" --env="DISPLAY" shafigullinik/opencv

camera2:
	docker run -it --volume $(shell pwd)/camera_2:/bus/camera --volume $(shell pwd)/src:/bus/app --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" --env="DISPLAY" shafigullinik/opencv bash

camera3:
	docker run -it --volume $(shell pwd)/camera_3:/usr/src/camera --volume $(shell pwd)/src:/usr/src/app --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" --env="DISPLAY" shafigullinik/opencv python camera/app.py