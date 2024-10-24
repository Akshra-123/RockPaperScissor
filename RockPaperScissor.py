import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time
import random

cap=cv2.VideoCapture(0)
cap.set(3,640) # setting the third id which is width to 640
cap.set(4,480) # setting the height to 480

timer=0
detector = HandDetector(maxHands=1)
StateResult=False
StartGame=False
scores=[0,0] # [AI,Player]

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
        
        if timer>3:
            StateResult=True
            timer=0
            
            if hands:
                hand = hands[0]
                fingers = detector.fingersUp(hand)
                if fingers==[0,0,0,0,0]:
                    PlayerMove=1
                if fingers==[1,1,1,1,1]:
                    PlayerMove=2
                if fingers==[0,1,1,0,0]:
                    PlayerMove=3
                
                RandomNumber=random.randint(1,3)
                imgAI = cv2.imread(f'RPS\\Resources\\Resources\\{RandomNumber}.png',cv2.IMREAD_UNCHANGED)
                imgBG = cvzone.overlayPNG(imgBG,imgAI,(149,310))
                
                if ((PlayerMove == 1 and RandomNumber == 3) or (PlayerMove == 2 and RandomNumber == 1) or (PlayerMove == 3 and RandomNumber == 2)):
                    scores[1] += 1
 
                    # AI Wins
                if ((PlayerMove == 3 and RandomNumber == 1) or (PlayerMove == 1 and RandomNumber == 2) or (PlayerMove == 2 and RandomNumber == 3)):
                    scores[0] += 1
                        
                print(PlayerMove)
                print(fingers)
        
    imgBG[234:654,795:1195]=imgscaled
    
    if StateResult:
        imgBG = cvzone.overlayPNG(imgBG,imgAI,(149,310))
        
    cv2.putText(imgBG, str(scores[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
    cv2.putText(imgBG, str(scores[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
    
    
    #cv2.imshow("Image" , img)
    cv2.imshow("BG" , imgBG)
    #cv2.imshow("Scaled Image" , imgscaled)
    
    key=cv2.waitKey(1)
    
    if (key==ord('s')):
        StartGame=True
        initialTime=time.time()
        StateResult=False
