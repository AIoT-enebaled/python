import cv2
import time
import datetime

# Initialize the webcam capture object
cap = cv2.VideoCapture(0)

# Initialize the cascade classifiers for detecting faces and bodies
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody_default.xml")

detection = False
detection_stopped_time = None
timer_started = False
SECONDS_TO_RECORD_AFTER_DETECTION = 5

# Set up the video output object
frame_size = (int(cap.get(3)), int(cap.get(4)))  # Get the size of each frame
fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Define the codec for the video file


# Main loop for capturing frames and processing them
while True:
    # Capture a frame from the webcam
    _, frame = cap.read()
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces and bodies in the frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    bodies = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    # If a face or body is detected, write the frame to the video output
    if len(faces) + len(bodies) > 0:
        if detection:
            timer_started = False
        else:
            detection = True
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            out = cv2.VideoWriter(f"{current_time}.mp4", fourcc, 10, frame_size,)
            print("Started Recording!")
    elif detection:
       if timer_started:
           if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
               detection = False
               timer_started = False
               out.release()
               print("Stopped Recording!")
        
       else:
        timer_started = True   
        detection_stopped_time = time.time()    
        
    if detection:
        out.write(frame)
        
    # Display the current frame
    cv2.imshow("Camera", frame)
    
    # If the user presses the 'q' key, break out of the loop
    if cv2.waitKey(1) == ord('q'):
        break
    
# Release the video capture and output objects, and close the display window
out.release()
cap.release()
cv2.destroyAllWindows()
