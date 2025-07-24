import cv2
import face_recognition
import csv
from datetime import datetime
import os

def log_attendance(name):
    """Log attendance with timestamp"""
    if name == "Unknown":
        return
        
    now = datetime.now()
    date_string = now.strftime('%Y-%m-%d')
    time_string = now.strftime('%H:%M:%S')
    
    # Check if person is already logged today
    already_logged = False
    if os.path.exists('attendance_log.csv'):
        with open('attendance_log.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            for row in reader:
                if row[0] == name and row[1] == date_string:
                    already_logged = True
                    break
    
    # Log attendance if not already logged today
    if not already_logged:
        with open('attendance_log.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            if os.path.getsize('attendance_log.csv') == 0:
                writer.writerow(['Name', 'Date', 'Time'])
            writer.writerow([name, date_string, time_string])
            print(f"Logged attendance for {name}")

# Load known face encodings and names from CSV
with open('known_faces.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    known_faces_parse = []

    # Skip the header row
    next(csv_reader)

    for line in csv_reader:
        known_faces_parse.append((line[0], line[1], line[2]))

# Test the functions we made
def get_encodings():
    encodings = []
    for first_name, last_name, image_path in known_faces_parse:
        x = face_recognition.load_image_file(image_path)
        y = face_recognition.face_encodings(x)[0]
        encodings.append(y)
    return encodings

def get_names():
    names = []
    for first_name, last_name, image_path in known_faces_parse:
        full_name = f"{first_name} {last_name}"
        names.append(full_name)
    return names

# Load known face encodings and names
known_face_encodings = get_encodings()
known_face_names = get_names()

#initialize webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Find all face locations and encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Loop through each face found in the frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Compare the current face encoding with known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # Use the first match found
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            log_attendance(name)

        # Draw a rectangle around the face and label it
        color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.putText(frame, name, (left + 6, bottom - 6), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 1)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
video_capture.release()
cv2.destroyAllWindows()