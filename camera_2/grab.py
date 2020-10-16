import cv2
import os


def grab(video):
    cap = cv2.VideoCapture(video)
    counter = _get_max_file_number()
    while(cap.isOpened()):
        counter += 1
        ret, frame = cap.read()
        if ret:
            if counter % 15 == 0:
                cv2.imwrite(f'frames/{counter}.jpg', frame)
                print(counter)
        else:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()


def _get_max_file_number():
    max_number = 0
    files = os.listdir(f'{os.getcwd()}/frames')
    for filename in files:
        if filename.endswith(".jpg"):
            max_number = max(int(filename.split('.')[0]), max_number)
    return max_number + 1


grab('43.avi')
