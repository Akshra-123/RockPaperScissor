import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
cap=cv2.VideoCapture(0)
cap.set(3,640) # setting the third id which is width to 640
cap.set(4,480) # setting the height to 480

detector = HandDetector(maxHands=1)
while True:
    imgBG = cv2.imread("RPS\\Resources\\Resources\\BG.png")
    success , img = cap.read()
    imgscaled = cv2.resize(img , (0,0) , None , 0.875 , 0.875)
    imgscaled=imgscaled[:,80:480]
    
    hands , img = detector.findHands(imgscaled)
    
    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        print(fingers)
        
    imgBG[234:654,795:1195]=imgscaled
    
    
    #cv2.imshow("Image" , img)
    cv2.imshow("BG" , imgBG)
    #cv2.imshow("Scaled Image" , imgscaled)
    
    cv2.waitKey(1)
