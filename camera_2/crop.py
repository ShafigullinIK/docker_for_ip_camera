import cv2
import os


def crop_and_save(img_name, dest):
    frame = cv2.imread(f'frames/{img_name}')
    print(img_name)
    croped_frame = frame[340:570, 0:700]
    cv2.imwrite(f"{dest}/{img_name}", croped_frame)


def crop_all_in_folder():
    dest = f'{os.getcwd()}/frames/croped'
    files = os.listdir(f'{os.getcwd()}/frames')
    for filename in files:
        if filename.endswith(".jpg"):
            crop_and_save(filename, dest)


crop_all_in_folder()
