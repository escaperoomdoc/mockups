import redis
import sys
import cv2


gray = cv2.imread('./media/print1.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('gray', gray)
cv2.waitKey(0)
exit(0)

# read images
img_bg = cv2.imread('./media/bg.png')
img_print = cv2.imread('./media/print1.png')

# wxyh - rectangle positon (x,y,w,h), rect(x,y,x+w,y+h)
xywh = (470, 260, 90, 90)
rect = xywh[:2] + (xywh[0] + xywh[2], xywh[1] + xywh[3])

# resize print to the target rectangle size
img_print_resized = cv2.resize(img_print, xywh[2:], interpolation = cv.INTER_CUBIC)

# crop tshirt from the source background image
img_cropped_bg = img_bg[rect[1]:rect[3], rect[0]:rect[2]]
#img_bitwised = cv.bitwise_and(img_cropped_bg, img_print_resized)
img_merged = cv2.addWeighted(img_cropped_bg,0.2,img_print_resized,0.8,0)
cv2.imshow('img_merged', img_merged)

'''
img_bg[rect[1]:rect[3], rect[0]:rect[2]] = img_print_resized
cv.rectangle(img_print, rect[:2], rect[2:], (0, 255, 0), 3)
cv.imshow('result', img_bg)
'''

cv2.waitKey(0)

