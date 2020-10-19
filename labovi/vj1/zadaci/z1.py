import cv2

slika = cv2.imread('../img/image.jpg')

retci, stupci, kanali = slika.shape

print("ORGINAL: ")
print('Broj redaka je ' + str(retci))
print('Broj stupaca je ' + str(stupci))
print('Broj kanala je ' + str(kanali))