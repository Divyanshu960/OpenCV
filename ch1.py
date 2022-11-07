import cv2 as c
print("Package Imported")
#
# img = c.imread("Res/viper.jpg")
# c.imshow("Output",img)
# c.waitKey(5000)
#
# cap = c.VideoCapture("Res/gojo.mp4")
cap = c.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
    success,img = cap.read()
    c.imshow("Video",img)
    if c.waitKey(1) & 0xFF == ord('q'):
        break