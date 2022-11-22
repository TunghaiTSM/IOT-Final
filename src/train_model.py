import cv2
import numpy as np
from PIL import Image
import os
path = 'dataset'
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("src/haarcascade_frontalface_default.xml");

def getFaceAndID(path):
    images = [os.path.join(path,f) for f in os.listdir(path)]     
    FaceList = []
    IDList = []
    for image in images:
        img = Image.open(image).convert('L') #轉換成灰階
        img_np = np.array(img,'uint8')
        id = int(os.path.split(image)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_np)
        for (x,y,w,h) in faces:
            FaceList.append(img_np[y:y+h,x:x+w])
            IDList.append(id)
    return FaceList, IDList

print ("\n影像辨識中")
face, id = getFaceAndID(path)
recognizer.train(face, np.array(id))
recognizer.write('models/train.yml') #儲存訓練結果
print("\n訓練出{0}張臉".format(len(np.unique(id))))
