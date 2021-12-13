import sys
import cv2
import brightness
import time

# read source print image and make a mask of it: 0/1 -> 0/255
img_mask = cv2.imread('./media/print1.png', cv2.IMREAD_GRAYSCALE)
print(sys.getsizeof(img_mask))
img_mask[img_mask > 0] = 255

# read background and print images as is (BGR)
img_bg = cv2.imread('./media/bg.png')
img_print = cv2.imread('./media/print1.png')

# set paste rectangle: wxyh - (x,y,w,h), rect - (x,y,x+w,y+h)
xywh = (470, 260, 90, 90)
rect = xywh[:2] + (xywh[0] + xywh[2], xywh[1] + xywh[3])

# resize print and mask to the target rectangle size
img_print_resized = cv2.resize(img_print, xywh[2:], interpolation = cv2.INTER_CUBIC)
img_mask_resized = cv2.resize(img_mask, xywh[2:], interpolation = cv2.INTER_CUBIC)

# crop tshirt from the source background image and apply bright + contrast
img_cropped_bg = img_bg[rect[1]:rect[3], rect[0]:rect[2]]
img_cropped_bg = brightness.apply_brightness_contrast(img_cropped_bg, 150, 200)

# merge img_cropped_bg and print image for shaddowing
img_merged = cv2.addWeighted(img_cropped_bg, 0.7, img_print_resized, 0.5, 0)
img_merged[img_mask_resized == 0] = (0, 0, 0)

# put merge image to the sourc background: img_bg[rect[1]:rect[3], rect[0]:rect[2]] = img_merged
img_result = img_bg.copy()
for y in range(xywh[2]):
	for x in range(xywh[3]):
		if img_mask_resized[y,x] > 0: img_result[y+xywh[1],x+xywh[0]] = img_merged[y,x]

# show chick
cv2.imshow('img_result', img_result)
cv2.waitKey(0)

