#import librtmp
import cv2
import sys

#first test not working
#create a connectionconn=librtmp.RTMP("rtmp://172.19.43.190/live/prova2",live=True)
# Attempt to connectconn.connect(None)
# Get a file-like object to access to the streamstream = conn.create_stream(0,True,update_buffer=True)
# Read 1024 bytes of data
#data = stream.read(1024)

# Classifier for face
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Classifier for eyes
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
# Classifier for ears
left_ear_cascade = cv2.CascadeClassifier('haarcascade_mcs_leftear.xml')
right_ear_cascade = cv2.CascadeClassifier('haarcascade_mcs_rightear.xml')

video_capture = cv2.VideoCapture('rtmp://172.19.62.109/live/prova1')

# Control if avoid video capture
if(not video_capture.isOpened()):
	sys.exit()

#print video_capture.open(cascPath)

# Define codec and create Video Writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('LiveDrone.avi',fourcc, 20.0, (1280,720))
out2 = cv2.VideoWriter('LiveDronewithDetection.avi',fourcc, 20.0, (1280,720))

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    frame = cv2.flip(frame,1)

    # Write the frame
    out.write(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
	flags = cv2.CASCADE_SCALE_IMAGE
	)

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
    	roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            #Draw a circle around the eyes
            cv2.circle(roi_color, ((ex+ex+ew)/2,(ey+ey+eh)/2),23,(255,0,0),3, 5)
            #cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
    
    left_ear = left_ear_cascade.detectMultiScale(gray, 1.3, 5)
    right_ear = right_ear_cascade.detectMultiScale(gray, 1.3, 5)
    # Draw rectangle around the ears
    for (a,b,c,d) in left_ear:
        cv2.rectangle(frame, (a,b), (a+c,b+d), (0,255,255), 2,99)
    for (e,f,g,z) in right_ear:
        cv2.rectangle(frame, (e,f), (e+g,f+z), (0,255,255), 2,99)

    # Display the resulting frame
    cv2.imshow('FaceDetection', frame)

    # Write frame Detection
    out2.write(frame)

    # For exit from video press 'q' 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture and release the writing 
video_capture.release()
# Release video without the detection
out.realease()
# Release a video with the detection
out2.release()
cv2.destroyAllWindows()
