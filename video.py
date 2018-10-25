import cv2

#cap = cv2.VideoCapture('sora.avi')
cap = cv2.VideoCapture(0)
codecs = 'MJPG'
fourcc = cv2.VideoWriter_fourcc(*codecs)
# fps = int(cap.get(cv2.CAP_PROP_FPS))
fps = 10
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
out = cv2.VideoWriter('out.avi', fourcc, fps, size)

while True:
    ret, frame = cap.read()
    # k = cv2.waitKey(fps)
    k = cv2.waitKey(1)
    if k == 27 or not ret:
        break
    rotate = cv2.getRotationMatrix2D((size[0] / 2, size[1] / 2), 90, 1)
    frame = cv2.warpAffine(frame, rotate, size)
    cv2.imshow('video', frame)
    out.write(frame)

cap.release()
cv2.destroyAllWindows()
