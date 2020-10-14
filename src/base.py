import cv2


def video_func(ip_camera):
    print('Открываем видео поток ...')
    cap = cv2.VideoCapture(ip_camera)
    (grabbed, frame) = cap.read()
    fshape = frame.shape
    fheight = fshape[0]
    fwidth = fshape[1]
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 24.0, (fwidth, fheight))
    print('Пишем видео в файл output.avi ....')
    print('Нажмите ctrl+C чтобы остановить запись')
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            out.write(frame)
        else:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    # cv2.destroyAllWindows()


video_func('rtsp://170.93.143.139/rtplive/470011e600ef003a004ee33696235daa')
