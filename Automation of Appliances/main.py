import cv2
import imutils
from cvzone.SerialModule import SerialObject
import time
from twilio.rest import Client

# Twilio credentials for sending SMS
account_sid = 'ACc44aa232850f1f70b62bb7e1599d757d'
auth_token = '2602d7cc81501cd3ec5b3d045fe484af'
client = Client(account_sid, auth_token)

# Create an Arduino serial connection
arduino = SerialObject("/dev/cu.usbserial-10")

# Initialize time variables
t_in = time.time()
count = 0

# Initialize the HOG person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Open the video capture
cap = cv2.VideoCapture('Untitled.avi')

# Flag to track first detection
first = False

# Main loop for processing video frames
while cap.isOpened():
    # Read the video stream frame
    ret, image = cap.read()
    if ret:
        # Resize the image for processing
        image = imutils.resize(image, width=min(400, image.shape[1]))

        # Detect people regions using HOG
        (regions, _) = hog.detectMultiScale(image, winStride=(4, 4), padding=(4, 4), scale=1.05)
        
        # If people detected
        if len(regions) >= 1:
            # Send data to Arduino, reset timer and count
            arduino.sendData([1, 1])
            t_in = time.time()
            count = 0
            first = True
        else:
            # If count reaches 2, send SMS and reset
            if count == 2:
                time.sleep(7)
                message = client.messages.create(
                    body='WE ARE TURNING OFF THE APPLIANCES AS THE TIME LIMIT EXCEEDED.',
                    from_='+15673132006',
                    to='+916284132990'
                )
                count = 0
                first = False
                time.sleep(5)
                arduino.sendData([0, 0])
                continue

            # If it's the first iteration, turn off appliances
            if first is False:
                arduino.sendData([0, 0])
            else:
                # If time limit exceeded, send SMS reminder
                arduino.sendData([0, 1])
                curr = time.time() - t_in
                if curr >= 20:
                    count += 1
                    message = client.messages.create(
                        body=f'PLEASE TURN OFF THE APPLIANCES OF YOUR ROOM - REMINDER {count}',
                        from_='+15673132006',
                        to='+916284132990'
                    )
                    t_in = time.time()

        # Draw rectangles around detected regions
        for (x, y, w, h) in regions:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Display the output image
        cv2.imshow("Image", image)

        # Exit loop on pressing 'q'
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

# Release resources and close windows
cap.release()
cv2.destroyAllWindows()
