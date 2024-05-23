import cv2
import numpy as np

image = cv2.imread('gul.jpg')

# SIFT tanımlayıcısı
sift = cv2.SIFT_create()
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Keypoint ve tanımlayıcılar
keypoints, descriptors = sift.detectAndCompute(gray_image, None)

# Keypointleri img üzerine çizme
img_keypoints = cv2.drawKeypoints(image, keypoints, None)

# Keypoint + Bounding box
koordinat_keypoint = np.array([kp.pt for kp in keypoints], dtype=np.int32)
x, y, w, h = cv2.boundingRect(koordinat_keypoint)

# Çiçek tespiti
gul_bolge = image[y:y+h, x:x+w]
img_hsv = cv2.cvtColor(gul_bolge, cv2.COLOR_BGR2HSV)

# Genişletilmiş Mor HSV aralığı (120-180 tonları)
lower_purple = np.array([120, 50, 50])
upper_purple = np.array([180, 255, 255])


mask = cv2.inRange(img_hsv, lower_purple, upper_purple)
img_hsv[mask > 0] = [150, 255, 255]
img_hsv[mask==0]=[0,0,0]
img_bgr = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)


image[y:y+h, x:x+w] = img_bgr


cv2.imshow(' Gül', image)
cv2.imshow('Keypoints with image', img_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()
