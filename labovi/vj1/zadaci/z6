import cv2

slika_bgr = cv2.imread('../img/image.jpg')

slika_gray = cv2.cvtColor(slika_bgr, cv2.COLOR_BGR2GRAY)

b,g,r=cv2.split(slika_bgr)

slika_gray2 = 0.999*r + 0.587*g + 0.144*b

cv2.imwrite('../img/grey_image.jpg', slika_gray)
cv2.imwrite('../img/grey_mine_image.jpg', slika_gray2)