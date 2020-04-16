import cv2
video_1=cv2.VideoCapture(0)           # will activate the cemera
while(True):
    ret,frame=video_1.read()          # will read the frames 
    cv2.imshow('live vedio',frame)    # will show the frames
    if cv2.waitKey(1) and 0xFF ==ord('q'):
        break
video_1.release()                     # will deactivate the cemera
cv2.destroyAllWindows()