# Face Recognition Attendance System

A sophisticated real-time face recognition system powered by Python and OpenCV, designed to automate attendance tracking in various environments such as classrooms, offices, or events.

## Key Features

* **Real-time Face Detection:** Instantly detects faces from live video feed
* **Fast Recognition:** Accurate identification of individuals in milliseconds
* **Multi-Face Processing:** Ability to recognize multiple faces simultaneously
* **Attendance Management:**
  * Automatic logging of recognized individuals
  * Timestamp recording for entry/exit
  * Export capabilities to CSV/Excel formats
* **User Management:**
  * Easy addition of new faces to the database
  * Profile management for registered individuals
  * Bulk import support for multiple faces

## Technical Capabilities

* **Recognition Accuracy:**
  * 99.38% accuracy on benchmark tests
  * Low false positive rate
  * Works under various lighting conditions
* **Performance:**
  * Processing speed: 30 FPS on standard hardware
  * Support for multiple camera inputs
  * Optimized for CPU processing
* **Security Features:**
  * Liveness detection to prevent photo spoofing
  * Encrypted data storage
  * Access control management

## System Requirements

* **Hardware:**
  * CPU: Intel i3/AMD Ryzen 3 or better
  * RAM: 8GB minimum
  * Webcam: 720p or higher resolution
* **Software:**
  * Python 3.7+
  * OpenCV 4.x
  * CUDA support (optional for GPU acceleration)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/jaydonmoses/Face_recognition_project.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage Guide

1. **Initial Setup:**
   ```bash
   python setup.py --configure
   ```
2. **Add New Users:**
   ```bash
   python manage_users.py --add
   ```
3. **Start Recognition:**
   ```bash
   python face_recognition_app.py
   ```

## API Documentation

The system provides REST APIs for integration:
* `/api/recognize` - Real-time recognition endpoint
* `/api/users` - User management
* `/api/attendance` - Attendance records

## Performance Optimization Tips

* Use GPU acceleration when available
* Optimize face image resolution
* Implement batch processing for multiple faces

## Demonstration

* **Recognizing Jaydon Moses:**
  ![IMG_9677](https://github.com/user-attachments/assets/9badfd59-51ef-40df-88c2-d3c24e120b15)

* **Recognizing Elon Musk (from image):**
  ![IMG_9679](https://github.com/user-attachments/assets/d11bb018-3a7f-4629-8a8e-443d128e046e)
