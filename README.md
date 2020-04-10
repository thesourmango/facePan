# facePan
Face recognition and tracking using a 4k webcam, python and opencv, to accomplish teacher tracking 4x zoom and pan

## background
There are a lot of expensive PTZ cameras and associated software sold at insane price points for classroom streaming.
These efforts are made as part of a larger digtalisation project, where one branch is focusing on streaming, specifically classroom streaming.
One of the challenges of classroom streaming is how to keep the teacher in frame, preferably also filling up most of the frame since the camera will typically be in a small PiP frame on top of a presentation screen stream.

## purpose
This project is intended to work as a Proof of Concept to convince the AV-department and/or management to choose this approach for classroom streaming instead of expensive motorized cameras with proprietary software.

## setup
A Logitech Brio 4k webcam was selected as a "cheap" wide FOV camera.
Python-OpenCV makes implementation of face recognition easy.
The challenge is merely the lacking python skills of the teacher (me :p).

## future
As soon as a convincing "working" prototype is presented, resources may be allocated appropriately and eventual dedicated rasPies, Rock64s or similar can be utilized for automating this task for non-technical teachers. 
This means, that eg. resource optimization among other tasks, are of low priority.
For now, a .bat script at startup, a plugin or even just a python script for OBS as well as similar solutions are perfectly adequate.

## structure
The repo consists of a jupyter notebook where testing can be conducted. 
 - Just create a new code block when implementing new features
The .py script can be used for classroom testing where jupyter isn't installed for now, or for OBS script testing etc.
 - If anyone starts creating a plugin for OBS please create a subfolder for that
 
The data folder contains the face recognition cascade files from opencv and some test pics, you'll need the cascade files for testing.

## dependencies
tested on Ubuntu 18.04 and 19.04 and Windows 10 x64 Build 1809 (also some dev preview build)
python 3.6 and 3.7
opencv 3.4.6 and 4.1.0
cascade files
before running scripts, please make sure you have installed opencv-contrib-python and opencv-python by running
#### pip install opencv-contrib-python && pip install opencv-python

## comments
Thank you for your support, I lack time and skills to finish this PoC, I really appreciate all the help I can get.
I cannot offer you compensation UNLESS you are a student at Arcada, in which case I can offer you study credits for your efforts.
Also if you are interested in continuing working on this after its protype stage, resources might be allocated for the development of the "final" product. I have no intentions of selling this at any point (duh, code on git).
