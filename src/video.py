import cv2


def video_func(ip_camera):
    print('Открываем видео поток ...')
    cap = cv2.VideoCapture(ip_camera)
    print(cap.isOpened())
    # cap.open()
    print(cap.isOpened())
    (grabbed, frame) = cap.read()
    fshape = frame.shape
    fheight = fshape[0]
    fwidth = fshape[1]
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 24.0, (fwidth, fheight))
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            cv2.imshow("video", frame)
        else:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    print("Я уже всё")    


video_func('dance.mp4')
