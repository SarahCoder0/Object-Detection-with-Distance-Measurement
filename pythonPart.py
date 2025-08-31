import cv2
import serial

# Connect to Arduino via serial port
arduino = serial.Serial('COM3', 9600)  # Replace 'COM3' with your port
threshold_distance = 20  # in cm

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Capture video frame
    if not ret:
        break

    # Read distance data from Arduino
    if arduino.in_waiting > 0:
        distance = int(arduino.readline().decode().strip())
        print(f"Distance: {distance} cm")

        # Overlay bounding box if object is close
        if distance < threshold_distance:
            height, width, _ = frame.shape
            cv2.rectangle(frame, (50, 50), (width-50, height-50), (0, 255, 0), 2)
            cv2.putText(frame, f"Object Detected ({distance} cm)", (60, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the video frame
    cv2.imshow("Object Detection", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
arduino.close()
