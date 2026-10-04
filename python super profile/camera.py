import cv2
cap = cv2.VideoCapture(0)
cap.open(0)


while True :
    ret , frame = cap.read()
    cv2.imshow("frame ",frame )
    if cv2.waitkey(20 ) and 0xFF==ord("q"):
        break 
    if cv2.waitkey(33)== ord ("a"):
        cap.imwrite("image.png", frame )
cap.release()
cv2.distroyAllWindows()