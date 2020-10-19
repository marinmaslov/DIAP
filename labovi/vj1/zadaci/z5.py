import cv2

slika = cv2.imread('../img/image.jpg')

retci = slika.shape[0]
stupci = slika.shape[1]
kanali = slika.shape[2]

for k in range(0, kanali):
    for i in range(0, retci):
        for j in range(0, stupci):
            if slika[i, j, k] == 255:
                slika[i, j, k] = 0

cv2.imwrite("../img/nova_image.jpg", slika)