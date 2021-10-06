import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    ret,frame = cap.read() # it returns two values one is frame and other is bool, if ret is true then it means frams is ok otherwise its not
    gray_frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    if ret == False:
        continue

    cv.imshow("Video Frame",frame)
    cv.imshow("Gray Frame",gray_frame)

    # wait for the user input - q, then will stop the loop
    key_pressed = cv.waitKey(1) & 0xFF # after getting any input from the keyword program will wait for 1 ms
    if key_pressed == ord('q'):
        break

cap.release()
cv.destroyAllWindows()