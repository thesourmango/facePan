# Needs pip install opencv-contrib-python && pip install opencv-python
#import required libraries 
import cv2 #import OpenCV library
import time #importing time library
lbp_face_cascade = cv2.CascadeClassifier('data/lbpcascade_frontalface.xml') #load cascade classifier training file for lbpcascade
haar_face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml') # using haar bcause of accuracy but lpb is waay faster

cam = cv2.VideoCapture(0) # cam is the videofeed from video0
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
t1 = time.time() # DEBUG: start timer for monitoring speed
(ret, frame) = cam.read() # Grab tuples from cam (True/False, Frame)
w,h = frame.shape[1], frame.shape[0] # grab frame size
print("Resolution: ", w, "x", h)
zoom = 4; # How much zoom/crop you want
crop = [w/zoom*2, h/zoom*2] # times 2 bcause left and right
print("Cropping to: ", crop[0], "x", crop[1])
x,y = crop[0]/2 ,crop[1]/2 # If face not detected on frame 1 we need some dummy coords x & y/2
lastFace = x,y,w,h # keep track of last "discovered" face

def drawRect(frame,faces):
    x,y,w,h = faces[0] # first face coordinates
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2) # draw a GREEN rectangle
    
def trackFace(frame,faces):
    pass
    
def waitForFace(frame,lastFace): # if no face detected, idle, then try again
    x,y,w,h = int(lastFace[0]),int(lastFace[1]),int(lastFace[2]),int(lastFace[3])
    cX,cY = int(x+(w/2)), int(y+(h/2)) # Face centre coords
    crop_img = frame[cY-135:cY+135, cX-200:cX+200] # crop video to 1/4 size around face
    cv2.imshow("cropped", crop_img) # DEBUG: show cropped frame
    t2 = time.time() # DEBUG: check how long processing takes
    return crop_img

def detectFace(gray,frame): # try to find face
    faces = lbp_face_cascade.detectMultiScale(gray, 1.2, 5, 0, (0, 0)) # img,scaleFactor,minNeighbors, flags, min_size
    if (len(faces)):
        for (x,y,w,h) in faces: # if face detected
            x,y,w,h = faces[0] # first face coordinates
            if y <=135: y = 135  # dont crop when nearing top of frame
            if x <=200: x = 200  # dont crop when nearing left of frame
            
            drawRect(frame,faces)  # draw a rectangle around detected face
            cX,cY = int(x+(w/2)), int(y+(h/2)) # Face centre coords
            crop_img = frame[cY-135:cY+135, cX-200:cX+200] # crop video to 1/4 size around face

            global lastFace
            lastFace = x,y,w,h # save last detected face coords
            # trackFace(frame) # face detected, move to tracking
            return crop_img
    else:
        crop_img = waitForFace(frame,lastFace)
        return crop_img

def main():
    while True:
        (ret, frame) = cam.read() # Grab tuples from cam (True/False, Frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convert img to grayscale, speeds up tracking no penalty in acc
        crop_img = detectFace(gray,frame) # Run tracking on grayscale img with last known coords
        cv2.imshow("cropped", crop_img) # DEBUG: show cropped frame

        if cv2.waitKey(50) == 27: # PRESS ESC TO EXIT
            break
    cam.release()
    cv2.destroyAllWindows()

#For starting the .py script
if __name__ == '__main__':
    main()
