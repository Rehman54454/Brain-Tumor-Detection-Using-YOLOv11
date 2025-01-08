import cv2
from ultralytics import YOLO
img=cv2.imread(r"C:\Users\3s\Downloads\TEST IMAGES\BRAIN TUMOR\5.jpg")
#print(img)

img=cv2.resize(img,(640,640))
model=YOLO(r"C:\Users\3s\Downloads\YOLOV9 ON CANCER\50 epochs\best.pt")

results=model(img)

detected_image=results[0].plot()

cv2.imshow("defects",detected_image)
cv2.waitKey()
cv2.destroyAllWindows()


