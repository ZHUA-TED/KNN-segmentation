__author__ = 'zhengxiaoyu'
from  numpy import *
import cv2
import numpy
from scipy.cluster.vq import *
img = cv2.imread('/Users/zhengxiaoyu/Downloads/IMG_0651.JPG')
center = 3
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
datalab = cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
column = len(datalab[1,])
rows = len(datalab)
ab = datalab[:,:,2:3]
ab = reshape(ab,rows*column,2)
ans ,arr = kmeans2(ab.astype(float),center,iter=15,missing='warn')
cluster = []
a = []
for i in range(center):
    cluster.append(a)
    a = []
arr = reshape(arr,(rows,column),order=1)
img_backup = img.copy()
print ans
for i in range(rows):
    for j in range(column):
        img_backup[i,j] = [0,0,0]
for z in range(center):
    for x in range(rows):
        for y in range(column):
            if arr[x,y] == z:
                #print z
                img_backup[x,y] = img[x,y]
                #cluster[z].append([x,y])
    cv2.imwrite('%s.jpg'%z,img_backup)
    print 'cluster%s'%z
