import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('/Users/tanvikrishnapatil/x/venv/lib/python2.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/Users/tanvikrishnapatil/x/venv/lib/python2.7/site-packages/cv2/data/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
count=1

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            print(count)
            crop_img = roi_color[ey: ey + eh, ex: ex + ew]
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            s1='madhavi/life_{}.jpg'.format(count)
            count=count+1
            img3 = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
            (thresh, im_bw) = cv2.threshold(img3, 155, 255, cv2.THRESH_OTSU)
            cv2.imwrite(s1,im_bw)
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
