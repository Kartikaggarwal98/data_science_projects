import cv2
import numpy as np
from matplotlib import pyplot as plt
f= np.load('./data/my_face_data.npy')

#print f.shape
l=np.load('./data/my_face_labels.npy')
#l=np.asarray([0,0,1,1,2,2])
#print l.shape
f=f.reshape((f.shape[0], f.shape[1]*f.shape[2]))
print f.shape

# import numpy as np

rgb = cv2.VideoCapture(0)
facec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# print facec
font = cv2.FONT_HERSHEY_SIMPLEX

def dist(x1,x2):
    print x1.shape,x2.shape
    print "Distance Calling..."
    return np.sqrt(sum((x1-x2)**2))
    print dist(np.array([0,0]),np.array([1,1]))


def knn(X_train, x, y_train, k=2):
    vals = []
    
    for ix in range(X_train.shape[0]):
        v = [dist(x, X_train[ix, :]), y_train[ix]]
        vals.append(v)
    
    updated_vals = sorted(vals, key=lambda x: x[0])
    pred_arr = np.asarray(updated_vals[:k])
    pred_arr = np.unique(pred_arr[:, 1], return_counts=True)
    pred = pred_arr[1].argmax()
    # return pred_arr[0][pred]
    return pred_arr, pred_arr[0][pred]

def get_name(im):
    print l
    print "@@@@@@@@@"
    X_train = f[:, :]
    X_test = f[4, :]
    print X_train.shape, X_test.shape
    print "call KNN....."
    pr = knn(X_train, im, l[:])
    return pr[1]

def recognize_face(im):
    if im.any():
        print "@@@@",im.shape,"@@@@"
        im = cv2.resize(im, (100, 100))
        im = im.flatten()
        #im=cv2.cvtColor(im,cv2.COLOR_RGB2GRAY)
        print im.shape
        print "!!!!!!!!!!"
        return get_name(im)

while True:
    _, fr = rgb.read()
    print "%%%%%%%%%%%%%%"
    print fr.shape
    gray = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
    print gray.shape
    faces = facec.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        print "&&&&&&&&&&&&&&&&&&&&"
        fc = gray[x:x+w, y:y+h]
        print fc.shape
        out = recognize_face(fc)
        cv2.putText(gray, out, (x, y), font, 1, (255, 255, 0), 2)
    	cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)
    
    cv2.imshow('rgb', fr)
    cv2.imshow('gray', gray)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()