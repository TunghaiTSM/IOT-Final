import cv2
import numpy as np
import os
from PIL import Image, ImageDraw, ImageFont

from DB import AWS_DB # write_data (self, user, photo) 
from SendMail import SendMail # publish (self, msg)
from pi_send_shutdown import Shutdown # now ()


recognizer = cv2.face.LBPHFaceRecognizer_create()  #使用舊版opencv-contrib-python，例如：版本3.4.3.18
recognizer.read('models/train.yml')
cascadePath = "src/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
font = ImageFont.truetype('NotoSerifCJK-Regular.ttc', 40)  #sudo apt-get install fonts-noto-cjk
id = 0
names = ['JSL', 'TaLen', 'None'] #id為1，對應名字為建庭
camema = cv2.VideoCapture(0)
camema.set(3, 640) # 設定影片寬度
camema.set(4, 480) # 設定影片高度
minW = 0.1*camema.get(3)
minH = 0.1*camema.get(4)
blue = (255,0,0)
green = (0,255,0)
red = (0,0,255)
safe_flag = True
safe_counter = 0
while True:
    ret, img = camema.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5, minSize = (int(minW), int(minH)) )
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), green, 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        if (confidence < 65):
            name = names[id]
            confidence = str(100 - round(confidence)) +"%"
            safe_flag = True
            safe_counter = 0
            print ("Verified!", names[id])
            AWS_DB ().write_data (names[id], "KNOWN!")

        else:
            name = "未知"
            confidence = str(100 - round(confidence)) +"%" 
            safe_counter += 1
            if (safe_flag and safe_counter <= 100):
                print ("Safe")

            else:
                safe_flag = False
                print ("Unknown")
                AWS_DB ().write_data ("Unknown", "PEDOBEAR!") # FIXME
                SendMail ().publish ("BAD GUY APPEARED! Shutting down the PC from Raspberry Pi!")
                Shutdown ().now  ()



        imgPIL = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) #cv2轉換成PIL 
        draw = ImageDraw.Draw(imgPIL)
        draw.text((x+5,y-5), str(name), font=font, fill=blue)  #使用PIL顯示中文
        draw.text((x+5,y+h-5), str(confidence), font=font, fill=red)
        img = cv2.cvtColor(np.asarray(imgPIL),cv2.COLOR_RGB2BGR) #PIL轉換成cv2
    cv2.imshow('image',img) 
    k = cv2.waitKey(10) & 0xff #等待0.01秒
    if k == 27:
        break

print("\n程式結束")
camema.release()
cv2.destroyAllWindows()
