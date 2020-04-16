import cv2
video_1 = cv2.VideoCapture(0)                       # will activate the cemera
while(video_1.isOpened()):                          # if the cemera is available then only while loop will work
    ret,frame=video_1.read()                        # will read the frames 
    # advance commands are :
    print("Frame Width is : {}".format(cv2.CAP_PROP_FRAME_WIDTH))     # will print the Width of frame
    print("Frame Height is : {}".format(cv2.CAP_PROP_FRAME_HEIGHT))   # will print the Height of frame
    print("Frame Rate is : {}".format(cv2.CAP_PROP_FPS))
    
    
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)   # will convert the colour image to gray image 
    cv2.imshow('live vedio',frame)                  # will show the frames
    if cv2.waitKey(1) & 0xFF == ord('q'):           # when we press q record will get stop
        break
print("Number of Frames : {}".format(cv2.CAP_PROP_FRAME_COUNT))       # will print number of frames
print("Contrast of the image : {}".format(cv2.CAP_PROP_CONTRAST))
video_1.release()                     # will deactivate the cemera
cv2.destroyAllWindows()               # will destroy all windows