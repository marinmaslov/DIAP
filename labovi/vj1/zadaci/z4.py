import cv2

slika_bgr = cv2.imread('../img/image.jpg')

b,g,r = cv2.split(slika_bgr)

slika_hsv=cv2.cvtColor(slika_bgr, cv2.COLOR_BGR2HSV)

b,g,r = cv2.split(slika_hsv)

cv2.imwrite('../img/b2.jpg', b)
cv2.imwrite('../img/g2.jpg', g)
cv2.imwrite('../img/r2.jpg', r)

cv2.imwrite('../img/hsv_image.jpg', slika_hsv)