import cv2
import os


COUNT_OF_FILES = 5
COUNT_OF_FRAMES = 1000
COUNT_OF_ATTEMPTS = 3


def video_func(ip_camera):
    cap = _open_video(ip_camera)
    if cap.isOpened():
        (grabbed, frame) = cap.read()
        fshape = frame.shape
        fheight = fshape[0]
        fwidth = fshape[1]
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        file_number = _get_max_file_number()
        for i in range(COUNT_OF_FILES):
            out = cv2.VideoWriter(f'/bus/camera/{file_number + i}.avi', fourcc, 24.0, (fwidth, fheight))
            print(f'Пишем видео в файл {file_number + i}.avi ....')
            counter = 0
            while(cap.isOpened() and counter < COUNT_OF_FRAMES):
                counter += 1
                ret, frame = cap.read()
                if ret:
                    out.write(frame)
                else:
                    break
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
    cap.release()


def _open_video(ip_camera):
    print('Открываем видео поток ...')
    cap = cv2.VideoCapture(ip_camera)
    attempt = 0
    while (attempt < COUNT_OF_ATTEMPTS and not cap.isOpened()):
        attempt += 1
        cap = cv2.VideoCapture(ip_camera)
        if not cap.isOpened():
            print(f'Не удалось открыть видео с {attempt} попытки')
    if cap.isOpened():
        print("Видео открыто")
    else:
        print("Не удалось открыть видео")
    return cap


def _get_max_file_number():
    max_number = 0
    files = os.listdir(os.getcwd())
    for filename in files:
        if filename.endswith(".avi"):
            max_number = max(int(filename.split('.')[0]), max_number)
    return max_number + 1
