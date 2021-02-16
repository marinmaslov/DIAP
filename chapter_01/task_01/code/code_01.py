import cv2

image = cv2.imread('../img/image.jpg')

rows, columns, channels = image.shape

print("Original Image: ")
print('No. of rows: ' + str(rows))
print('No. of columns: ' + str(columns))
print('No. of channels: ' + str(channels))