import cv2 #importing cv
import cvzone
from cvzone.HandTrackingModule import HandDetector #for detecting hand
import time
import random

cap=cv2.VideoCapture(0) #for opening webcam
cap.set(3, 640) #setting property 3(width)
cap.set(4, 480) #setting property 4(height)

detector=HandDetector(maxHands=1) #we will detect only one hand

timer=0
stateResult=False
startGame=False
scores=[0, 0] #score of [AI, player]

while True:
    imgBG=cv2.imread("Resources/BG.png") #accessing BG image from resources folder
    success, img=cap.read() #capturing image

    imgScaled=cv2.resize(img, (0, 0), None, 0.875, 0.875) #resizing image
    imgScaled=imgScaled[: ,80:480] #cropping width of scaled image

    #find hands
    hands, img = detector.findHands(imgScaled) #(imgScaled, draw=True, flipType=True)

    if startGame:

        if stateResult is False:
            timer=time.time()-initialTime
            cv2.putText(imgBG, str(int(timer)), (604, 435), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)
            #putting timer(image, text, position, font style, scale, colour(purple), thickness)

            if timer>3: #setting timer
                stateResult=True
                timer=0

                if hands:
                    playerMove=None
                    hand=hands[0]
                    fingers=detector.fingersUp(hand)
                    if fingers==[0, 0, 0, 0, 0]:
                        playerMove=1
                    if fingers==[1, 1, 1, 1, 1]:
                        playerMove=2
                    if fingers==[0, 1, 1, 0, 0]:
                        playerMove=3
                    randomNumber=random.randint(1, 3) #generate random number 1, 2, 3
                    imgAI=cv2.imread(f'Resources/{randomNumber}.png', cv2.IMREAD_UNCHANGED)
                    imgBG=cvzone.overlayPNG(imgBG, imgAI, (149, 310)) #(149, 310)->position

                    #Player wins
                    if (playerMove==1 and randomNumber==3) or \
                       (playerMove==2 and randomNumber==1) or \
                       (playerMove==3 and randomNumber==2):
                        scores[1] +=1

                    #AI wins
                    if (playerMove==3 and randomNumber==1) or \
                       (playerMove==1 and randomNumber==2) or \
                       (playerMove==2 and randomNumber==3):
                        scores[0] +=1


                    # print(fingers)
                    # print(playerMove)

    imgBG[234:654, 795:1195] = imgScaled #putting scaled img on bg (numbers are set by analysing pixels using paint)

    if stateResult:
        imgBG=cvzone.overlayPNG(imgBG, imgAI, (149, 310)) #(149, 310)->position

    cv2.putText(imgBG, str(scores[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
    cv2.putText(imgBG, str(scores[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)

    # cv2.imshow("Image", img) #displaying our image
    cv2.imshow("BG", imgBG) #displaying our BG image
    # cv2.imshow("Scaled", imgScaled) #displaying scaled image

    key= cv2.waitKey(1) #delay in ms
    if key==ord(' '):   #press space to start game
        startGame=True
        initialTime=time.time()
        stateResult=False
