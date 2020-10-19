import cv2

slika = cv2.imread('../img/image.jpg')

nova_slika = cv2.resize(slika, (0,0), fx=2, fy=2)
retci2, stupci2, kanali2 = nova_slika.shape

print("UVECANA SLIKA: ")
print('Broj redaka je ' + str(retci2))
print('Broj stupaca je ' + str(stupci2))
print('Broj kanala je ' + str(kanali2))

cv2.imwrite("../img/image_large.jpg", nova_slika)