import os
import numpy as np
import matplotlib.pyplot as plt
import cv2


image_path = 'C:/Users/Vaibhav/Desktop/Trial/MIO-TCD-Localization/'


def loadImages(path):
    

    image_files = sorted([os.path.join(path, 'train', file)
                          for file in os.listdir(path + "/train")
                          if file.endswith('.jpg')])
    
    return image_files



def processing(data):

    height = 220
    width = 220
    dim = (width, height)
    for i in range(0,len(data)):
        img = cv2.imread(data[i], cv2.IMREAD_UNCHANGED)
        res = cv2.resize(img, dim, interpolation=cv2.INTER_LINEAR)
        blur = cv2.medianBlur(res,5)
        cv2.imwrite('C:/Users/Vaibhav/Desktop/Trial/MIO-TCD-Localization/train_nonoise/'+data[i][-12:],blur)
        



def main():
    global image_path
    dataset = loadImages(image_path)
    processing(dataset)
   

  
main()

