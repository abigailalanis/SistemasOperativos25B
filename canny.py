
1  import cv2
2
3  img = cv2.imread('cartas.jpg',0)
4  bordeCanny = cv2.Canny(img, 100, 200)
5
6  cv2.imshow('Original', img)
7  cv2.imshow('blur', bordeCanny)
8
9  cv2.waitkey(0)
10 cv2.destroyAllWindows()
