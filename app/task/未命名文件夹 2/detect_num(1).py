import cv2
import numpy as np
from keras.models import load_model
from PIL import Image

image = cv2.imread('C:\\Users\\ailab\\PycharmProjects\\drone\\pic\\image4.jpg', 0)

def numRecognize(original_img):
    model = load_model('C:\\Users\\ailab\\PycharmProjects\\drone\\models\\num.h5')
    #将图像反色


    gray=cv2.cvtColor(original_img,cv2.COLOR_BayerGR2GRAY)
    img_adjust=255-gray

    #调整图像的大小为28*28像素
    img_adjust=cv2.resize(img_adjust,(28,28),interpolation=cv2.INTER_CUBIC)

    #调整图像为所需的四维向量
    img_adjust=(img_adjust.reshape(1, 1, 28, 28)).astype("float32") / 255
    #数字识别
    predict = model.predict_classes(img_adjust)
    print('识别为：')
    return predict

img_1=numRecognize(image)
print(img_1)
#cv2.imshow('1',img_1)
#cv2.waitKey(0)
#print(image)

#img_1 = (img_1.reshape(1,1,28,28)).astype("float32")/255


#predict = model.predict_classes(img_1)
#print ('识别为：')
#print (predict)

