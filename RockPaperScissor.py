import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time

cap=cv2.VideoCapture(0)
cap.set(3,640) # setting the third id which is width to 640
cap.set(4,480) # setting the height to 480

timer=0
detector = HandDetector(maxHands=1)
StateResult=False
StartGame=False

while True:
    imgBG = cv2.imread("RPS\\Resources\\Resources\\BG.png")
    success , img = cap.read()
    imgscaled = cv2.resize(img , (0,0) , None , 0.875 , 0.875)
    imgscaled=imgscaled[:,80:480]
    
    hands , img = detector.findHands(imgscaled)
    
    if StartGame:
        
        if StateResult is False:
            timer = time.time() - initialTime
            cv2.putText(imgBG, str(int(timer)), (605, 435), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)
        
        if hands:
            hand = hands[0]
            fingers = detector.fingersUp(hand)
            print(fingers)
        
    imgBG[234:654,795:1195]=imgscaled
    
    
    #cv2.imshow("Image" , img)
    cv2.imshow("BG" , imgBG)
    #cv2.imshow("Scaled Image" , imgscaled)
    
    key=cv2.waitKey(1)
    
    if (key==ord('s')):
        StartGame=True
        initialTime=time.time()
