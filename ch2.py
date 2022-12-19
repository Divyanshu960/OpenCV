import cv2 as c
import numpy as np
from matplotlib import pyplot as plt
   
rows = 2
columns = 2
fig = plt.figure(figsize=(10, 7))
  
img = c.imread("Res/Divyanshu.png")
kernel = np.ones((5,5),np.uint8)
 
imgGray = c.cvtColor(img,c.COLOR_BGR2GRAY)
imgBlur = c.GaussianBlur(imgGray,(7,7),0)
imgCanny =c.Canny(img,150,200)
imgDilation = c.dilate(imgCanny,kernel,iterations = 1)

Image1 = c.imshow("Gray Image",imgGray)
Image2 = c.imshow("Blur Image",imgBlur)
Image3 = c.imshow("Canny Image",imgCanny)
Image4 = c.imshow("Dilated Image",imgDilation)
fig.add_subplot(rows, columns, 1)
   
# showing image
plt.imshow(Image1)
plt.axis('off')
plt.title("First")
  
# Adds a subplot at the 2nd position
fig.add_subplot(rows, columns, 2)
  
# showing image
plt.imshow(Image2)
plt.axis('off')
plt.title("Second")
  
# Adds a subplot at the 3rd position
fig.add_subplot(rows, columns, 3)
  
# showing image
plt.imshow(Image3)
plt.axis('off')
plt.title("Third")
  
# Adds a subplot at the 4th position
fig.add_subplot(rows, columns, 4)
  
# showing image
plt.imshow(Image4)
plt.axis('off')
plt.title("Fourth")
c.waitKey(0)
