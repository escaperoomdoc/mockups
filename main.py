import redis
import sys
import cv2 as cv

img_bg = cv.imread('./media/bg.png')
img_print = cv.imread('./media/print1.png')
xywh = (470, 260, 90, 90)
rect = xywh[:2] + (xywh[0] + xywh[2], xywh[1] + xywh[3])
img_resized = cv.resize(img_print, xywh[2:], interpolation = cv.INTER_CUBIC)
cv.imshow('result1', img_resized)

#cv.rectangle(img_print, rect[:2], rect[2:], (0, 255, 0), 3)
#cv.imshow('result', img_bg)
cv.waitKey(0)

