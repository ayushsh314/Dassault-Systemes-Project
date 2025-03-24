# program to capture single image from webcam in python

# importing OpenCV library
import cv2

# initialize the camera
# If you have multiple camera connected with
# current device, assign a value in cam_port
# variable according to that
def capt():
	cam_port = 0
	cam = cv2.VideoCapture(cam_port)

	# reading the input using the camera
	result, image = cam.read()

	# If image will detected without any error,
	# show result
	if result:

		# showing result, it take frame name and image
		# output
		# saving image in local storage
		cv2.imwrite("178.jpg", image)

		# If keyboard interrupt occurs, destroy image
		# window


	# If captured image is corrupted, moving to else part
	else:
		print("No image detected. Please! try again")

	cam.release()
	return 
	
