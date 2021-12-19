import cv2 
from cvzone.PoseModule import PoseDetector
detector = PoseDetector()

# detect body pose from read image

'''
img = cv2.imread('media/bg.png')
img = detector.findPose(img)
imglist,bbox = detector.findPosition(img, bboxWithHands=False)
cv2.imshow("bg_Result", img)
cv2.waitKey(1)
'''

# detect body pose from live camera feed
cap = cv2.VideoCapture(0)
while True:
  success, img = cap.read()
  img = detector.findPose(img)
  imglist,bbox = detector.findPosition(img, bboxWithHands=False)
  cv2.imshow("MyResult", img)
  k = cv2.waitKey(1)
  if (k==27) or (k=='q') or (k=='Q'):
    break
cap.release()
