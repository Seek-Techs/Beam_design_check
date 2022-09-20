import cv2
img = cv2.imread('python.jpg', cv2.IMREAD_UNCHANGED)
print('original dimensions : ', img.shape)
scale_percent = 20
width = int(img.shape[1] * scale_percent/100)
height = int(img.shape[0] * scale_percent/100)
dim = (width, height)
  
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
print('Rsized dimension : ', resized.shape)
cv2.imshow('resized image', resized)
cv2.waitkey(0)
cv2.destroyAllWindows()