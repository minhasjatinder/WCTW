import cv2
import imutils
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.SerialModule import SerialObject
import time
import os
from twilio.rest import Client

# To send sms
account_sid = 'ACc44aa232850f1f70b62bb7e1599d757d'
auth_token = '2602d7cc81501cd3ec5b3d045fe484af'
client = Client(account_sid, auth_token)
detector = FaceDetector()
arduino = SerialObject("/dev/cu.usbserial-10")
t_in = time.time()
count = 0

# Initializing the HOG person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cap = cv2.VideoCapture('Untitled.avi')
# bool = True
first = False
while cap.isOpened():
	# Reading the video stream
	ret, image = cap.read()
	if ret:
		image = imutils.resize(image,
							width=min(400, image.shape[1]))

		# Detecting all the regions in the Image that has a person inside it
		(regions, _) = hog.detectMultiScale(image,winStride=(4, 4), padding=(4, 4), scale=1.05)
		if len(regions)>=1:
			arduino.sendData([1, 1])
			t_in = time.time()
			count = 0
			first = True
		else:
			if count == 2:
				time.sleep(7)
				message = client.messages \
					.create(
						body='WE ARE TURNING OFF THE APPLIANCES AS THE TIME LIMIT EXCEEDED.',
						from_ =  +15673132006,
						to = +916284132990
					)
				# bool = False
				count = 0
				first = False
				time.sleep(5)
				arduino.sendData([0,0])
				continue
			if first == False:
				arduino.sendData([0, 0])
			else:
				arduino.sendData([0, 1])
				curr = time.time() - t_in
				if curr >= 20:  
					count += 1
					
					message = client.messages \
						.create(
							body=f'PLEASE TURN OFF THE APPLIANCES OF YOUR ROOM - REMINDER {count}',
							from_ =  +15673132006,
							to = +916284132990
						)
					t_in = time.time()
			
			
	    
		for (x, y,w, h) in regions:
			cv2.rectangle(image, (x, y),
						(x + w, y + h),
						(0, 0, 255), 2)

		# Showing the output Image
		cv2.imshow("Image", image)
		if cv2.waitKey(25) & 0xFF == ord('q'):
			break
	else:
		break

cap.release()
cv2.destroyAllWindows()