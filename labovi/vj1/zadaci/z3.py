import cv2

slika = cv2.imread('../img/image.jpg')

b,g,r = cv2.split(slika)

cv2.imwrite('../img/b.jpg', b)
cv2.imwrite('../img/g.jpg', g)
cv2.imwrite('../img/r.jpg', r)