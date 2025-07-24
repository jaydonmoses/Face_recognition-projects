# Face Recognition Attendance System

This project is a real-time face recognition system built with Python and OpenCV, designed for automated attendance tracking.

## Features

* **Real-time Face Detection & Recognition:** Identifies individuals from a live video feed.
* **Attendance Tracking:** (Mention if you have this functionality) Potential for logging recognized individuals.
* **Scalable:** Easy to add new faces to the recognition database.

## Screenshots

* **Recognizing Jaydon Moses:**
    ![Jaydon Moses Recognition]
  ![IMG_9677](https://github.com/user-attachments/assets/9badfd59-51ef-40df-88c2-d3c24e120b15)

* **Recognizing Elon Musk (from image):**
    ![Elon Musk Recognition]
  ![IMG_9679](https://github.com/user-attachments/assets/d11bb018-3a7f-4629-8a8e-443d128e046e)

## Technologies

* **Python**
* **OpenCV**
* **face_recognition library** (or specify your chosen library/algorithms)

## Getting Started

### Prerequisites

* Python 3.x
* `pip`

### Installation

1.  Clone this repository: `git clone https://github.com/your-username/your-repository-name.git`
2.  Navigate to the project directory: `cd your-repository-name`
3.  Install dependencies: `pip install -r requirements.txt` (Make sure you have a `requirements.txt` file).

### Usage

1.  Place images of known individuals in the `known_faces/` directory.
2.  Run the main script: `python face_recognition_app.py`
3.  A window will open, displaying the live video feed with recognized names.

## Project Structure

<br /> ├── face_recognition_app.py
<br /> ├── known_faces/
<br /> ├── requirements.txt
<br /> └── README.md

## Future Enhancements

* Dedicated attendance database.
* Improved user interface.
* Advanced reporting features.
