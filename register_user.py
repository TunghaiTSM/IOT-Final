import cv2
import os


# Get Username to create target_path
name = input ("Input your username: ")
target_path = os.path.join (os.path.abspath(os.getcwd()), "dataset", name)
print (target_path)


# Start capturing headshots
cam = cv2.VideoCapture(0)

cv2.namedWindow("press space to take a photo", cv2.WINDOW_NORMAL)
cv2.resizeWindow("press space to take a photo", 500, 300)

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("press space to take a photo", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = target_path.join ("image_{}.jpg".format(img_counter))
	
        print("Writing into {}...".format(img_name))

#if not cv2.imwrite(img_name, frame):
#           raise Exception("Could not write image")
        if not cv2.imwrite(img_name, img):
            raise Exception("Could not write image")
        else:
            print("{} written!".format(img_name))
            img_counter += 1

cam.release()

cv2.destroyAllWindows()
