import cv2

# Load the pre-trained face detection model from OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

    # Iterate through the detected faces
    for (x, y, w, h) in faces:
        # Crop the detected face region
        face = frame[y:y+h, x:x+w]

        # Apply Gaussian blur to the detected face
        blurred_face = cv2.GaussianBlur(face, (99, 99), 10)

        # Replace the face in the original frame with the blurred face
        frame[y:y+h, x:x+w] = blurred_face

    # Display the resulting frame
    cv2.imshow("Face Detection and Blur", frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
