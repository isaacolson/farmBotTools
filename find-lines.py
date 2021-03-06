import cv2
import numpy as np
imgloc = r"" #enter path to picture here, between the quotes ("")'s with backslashes (\)'s denoting 'folder levels'
img = cv2.imread(imgloc)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
img = cv2.line(img,(814,1609),(814,1679+200),(255,255,255),1)

lines = cv2.HoughLines(edges,10,np.pi/180,200)
for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)


cv2.imwrite('houghlines_gray.jpg',gray)
cv2.imwrite('houghlines_canny.jpg',edges)
cv2.imwrite('houghlines_write.jpg',img)
cv2.imwrite('test.jpg',img)
