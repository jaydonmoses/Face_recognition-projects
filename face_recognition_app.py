import cv2
import face_recognition

#Load known face encodings and names
known_face_encodings = []
known_face_names = []

known_person1_image = face_recognition.load_image_file("person1.jpg")
known_person2_image = face_recognition.load_image_file("person2.jpg")

known_person_encoding1 = face_recognition.face_encodings(known_person1_image)[0]
known_person_encoding2 = face_recognition.face_encodings(known_person2_image)[0]

known_face_encodings.append(known_person_encoding1)
known_face_encodings.append(known_person_encoding2)

known_face_names.append("Jaydon Moses")
known_face_names.append("Elon Musk")

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

        # Draw a rectangle around the face and label it
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
video_capture.release()
cv2.destroyAllWindows()