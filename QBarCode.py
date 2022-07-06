import cv2
import numpy as np
from pyzbar.pyzbar import decode
import pyttsx3

img = cv2.imread('C:\\Users\\paras\\OneDrive\\Documents\\VS CODE\\QRCode Authentication\\paras.png')
# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

with open('C:\\Users\\paras\\OneDrive\\Documents\\VS CODE\\QRCode Authentication\\DataList.txt') as f:
    myDataList = f.read().splitlines()

while True:

    # success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)

        if myData in myDataList:
            myOutput = 'Authorized'
            print(myData)
            print("Authorized")
            # speak(myData)
            # speak("Authorized")
            myColor = (0,255,0)
        else:
            myOutput = 'Un-Authorized'
            print("Un-Authorized!!")
            print("Un-Authorized!!")
            # speak(myData)
            # speak("Un-Authorized!!")
            myColor = (0, 0, 255)

        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,myColor,5)
        pts2 = barcode.rect
        cv2.putText(img,myOutput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,myColor,2)

    cv2.imshow('Result',img)
    cv2.waitKey(1)