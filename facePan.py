#import required libraries 
import cv2 #import OpenCV library
import time #importing time library
#load cascade classifier training file for lbpcascade
lbp_face_cascade = cv2.CascadeClassifier('data/lbpcascade_frontalface.xml')
# NOW USING HAAR BCAUSE OF ACCURACY BUT LBP IS WAAY FASTER
haar_face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml')

cam = cv2.VideoCapture(0) # cam is the videofeed from video0
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cam.set(cv2.CAP_PROP_FPS, 15) # use uvcdynctrl -f to find out device frame formats
t1 = time.time() # DEBUG: start timer for monitoring speed


def main():
    w = cv2.CAP_PROP_FRAME_WIDTH
    h = cv2.CAP_PROP_FRAME_HEIGHT
    y = 135
    x= 200
    # Program function
    while True:
        (ret, frame) = cam.read() # Grab tuples from cam (True/False, Frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = haar_face_cascade.detectMultiScale(gray, 1.2, 5, 0, (0, 0)) # img,scaleFactor,minNeighbors, flags, min_size

        if (len(faces)):
            for (x,y,w,h) in faces: # iterate through all found faces
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2) # draw a rectangle
                if y <=135: # dont crop when nearing top of frame
                    y = 135
                if x<=200: # dont crop when nearing left of frame
                    x= 200
                crop_img = frame[y-135:y+135+h, x-200:x+200+w] # crop video to 1/4 size
                cv2.imshow("cropped", crop_img)
        else:
            crop_img = frame[y-135:y+135+h, x-200:x+200+w]
            cv2.imshow("cropped", crop_img)
        t5 = time.time() # DEBUG: check how long processing takes
        #print("Frame displayed at " + str(round(t5-t1, 3)) + "s")

        # PRESS ESC TO EXIT
        if cv2.waitKey(50) == 27:
            break
    cam.release()
    cv2.destroyAllWindows()

#For starting the .py script
if __name__ == '__main__':
    main()