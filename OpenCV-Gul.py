import cv2
import numpy as np

img = cv2.imread("gul.jpg")
# Image to HSV
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Trackbar penceresi 
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640, 300)

def nothing(x):
    pass

cv2.createTrackbar("Hue Min", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("Hue Max", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("Sat Min", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("Sat Max", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("Val Min", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("Val Max", "Trackbars", 255, 255, nothing)

while True:
    h_min=cv2.getTrackbarPos("Hue Min", "Trackbars")
    h_max =cv2.getTrackbarPos("Hue Max", "Trackbars")
    s_min = cv2.getTrackbarPos("Sat Min", "Trackbars")
    s_max = cv2.getTrackbarPos("Sat Max", "Trackbars")
    v_min=cv2.getTrackbarPos("Val Min", "Trackbars")
    v_max = cv2.getTrackbarPos("Val Max", "Trackbars")

    # Renkler img ile kırmızı hsv kodları alındı
    # lower = np.array([h_min,s_min,v_min])
    # upper = np.array([h_max,s_max,v_max])
    # 0 7 0  15 255 255
    # mask = cv2.inRange(hsv_img,lower,upper)

    # Kırmızı rengin iki aralığı
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 100, 100])
    upper_red2 = np.array([180, 255, 255])


     # Maske 
    mask1 = cv2.inRange(hsv_img, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv_img, lower_red2, upper_red2)
    mask  = cv2.bitwise_or(mask1, mask2)

    cv2.imshow('Gul',img)
    cv2.imshow('maske',mask)
    
    img_result = img.copy()
    img_result[mask > 0] = [153, 0, 102]
    #img_result = cv2.cvtColor(img,cv2.COLOR_HSV2BGR) 
    
    # Siyah arka plan
    img_result[mask == 0] = [0, 0, 0]

    # Sonuç
    cv2.imshow('Result Image', img_result)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 



    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

    

cv2.destroyAllWindows()
