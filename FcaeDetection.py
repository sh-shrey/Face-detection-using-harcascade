import cv2
image = cv2.imread("pic2.jpg");
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
haar_face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
face = haar_face_cascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=4)
for x,y,w,h in face:
    cv2.rectangle(image,(x,y),(x+w, y+h),(0,255,255),4)
print("Faces Found",len(face))
cv2.imshow("Face detection",image)
#cv2.imshow("Gray",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()