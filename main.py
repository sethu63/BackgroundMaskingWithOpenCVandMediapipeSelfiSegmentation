import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv2.VideoCapture(0)                                               #enables window camera capture
cap.set(3,600)                                                          #width of the window
cap.set(4,480)                                                          #height of the window
segmentor = SelfiSegmentation()
fpsReader = cvzone.FPS()                                                #counts the frame per second
lsImg = os.listdir("images")                                            #where are the images stored location
print(lsImg)                                                            #list of image names will be printed to console
imgls = []                                                              #image list

for imgPath in lsImg:
    img = cv2.imread(f'images/{imgPath}')
    imgls.append(img)                                                   #reading and adding images to the imgls list or array
print(imgls)                                                            #printing the same

imgIndex = 0                                                            #starting drom the index "0"

while True:
    success, img = cap.read()
    imgOut = segmentor.removeBG(img,imgls[imgIndex],threshold=0.3)      # removes the background and adds new one
    imgStacked = cvzone.stackImages([img,imgOut],2,1)                   #applies both the befpre and after windows at the same time and displays as one
    _, imgStacked = fpsReader.update(imgStacked,color=(0,0,255))        #fps counter
    print(imgIndex)                                                     #prits to the console

    cv2.imshow("Image",imgStacked)                                      #shows the final output to the window


    key = cv2.waitKey(1)
    #from here we will be able to change the images using simple for loop
    if(key==ord('a')):                                                  #'a' orks as "<-" key
        if(imgIndex>0):
            imgIndex-=1
    elif (key == ord('d')):                                             #'d' orks as "->" key
        if(imgIndex<len(lsImg)-1):
            imgIndex += 1
    elif (key == ord('q')):                                             # to terminate the process
        break