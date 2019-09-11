import numpy as np
import cv2

cascade_file = cv2.CascadeClassifier('watch-cascade.xml')

img = cv2.imread('unnamed.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

prod = cascade_file.detectMultiScale(gray, 8,8)

for(x,y,w,h) in prod:
      font = cv2.FONT_HERSHEY_SIMPLEX
      cv2.putText(img,'Kleenex', (x-w, y-h), font, 0.5, (0,255,255), 2, cv2.LINE_AA)
      #img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
      roi_gray = gray[y:y+h, x:x+w]
      roi_color = img[y:y+h, x:x+w]

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
