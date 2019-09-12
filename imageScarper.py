import urllib.request
import cv2
import numpy as np
import os
import requests
from PIL import Image
from io import StringIO

def store_images_set(negative_images_link):
    negative_image_urls = urllib.request.urlopen(negative_images_link,timeout=5).read().decode()

    if not os.path.exists('neg'):
        os.makedirs('neg')
    
    pic_num = len(os.listdir('neg/')) + 1

    for i in negative_image_urls.split('\n'):
        print('Attempting to get img')
        try:
            img = Image.open(requests.get(i,timeout=5,stream=True).raw)
            img.save("neg/"+str(pic_num)+".jpg")
            urllib.request.urlretrieve(i, "neg/"+str(pic_num)+".jpg")
            print("reading image")
            img = cv2.imread("neg/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            print("resizing image")
            resizied_image = cv2.resize(img, (100,100))
            print("writing image")
            cv2.imwrite("neg/"+str(pic_num)+'.jpg',resizied_image)
            pic_num += 1
            print("image done")
            print("")

        except Exception as e:
            print(str(e))

def create_index_images():
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            if file_type == 'neg':
                line = file_type+'/'+img+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)
            elif file_type == 'pos':
                line = file_type+'/'+img+' 1 0 0 50 50\n'
                with open('info.dat','a') as f:
                    f.write(line)

store_images_set('http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513')
store_images_set('http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152')
create_index_images()