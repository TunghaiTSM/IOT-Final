import cv2
import os

# Get Username to create target_path
#name = input ("Input your username: ")
name = "Samson"
target_path = os.path.join (os.path.abspath(os.getcwd()), "dataset", name)
if not os.path.exists (target_path):
    os.makedirs (target_path)
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

    #-------------------------EVENT HANDLING---------------------------
    k = cv2.waitKey(1)
    # ESC pressed
    if k%256 == 27:
        print("Escape hit, closing...")
        break
    
    
    # SPACE pressed
    elif k%256 == 32:
        img_name = target_path + "/image_" + str (img_counter) + ".jpg"
	
        if cv2.imwrite(img_name, frame):
            print("{} written!".format(img_name))
            img_counter += 1
    #------------------------------------------------------------------



# Cleaning up...
cam.release()
cv2.destroyAllWindows()
