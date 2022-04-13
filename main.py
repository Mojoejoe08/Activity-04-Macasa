import cv2

filePath = 'My.png'

image = cv2.imread(filePath,1)

cv2.imshow("Taglife",image)

cv2.waitKey(0)

cv2.destroyAllWindows()