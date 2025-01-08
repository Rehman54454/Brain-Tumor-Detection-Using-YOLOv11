# Brain-Tumor-Detection-Using-YOLOv11
A YOLOv11-based model for real-time detection and classification of brain tumors into benign and malignant categories.
![BT 1](https://github.com/user-attachments/assets/4e939fff-c8f3-4dbc-963a-c1627b068933)
![BT3](https://github.com/user-attachments/assets/0bff025c-3ca0-47c9-a867-bdc560571e4a)
![BT5](https://github.com/user-attachments/assets/9492e3aa-7875-45fb-841e-1ed1f748de26)

# **Description:**
This project focuses on developing a YOLOv11-based deep learning model for brain tumor detection, specifically identifying the presence of a tumor (tumor or no tumor) from medical images. The aim is to provide a robust, real-time solution for assisting medical professionals in diagnosing brain tumors effectively and efficiently. By leveraging advanced object detection techniques, the model ensures accurate and reliable predictions, contributing to faster diagnostic processes and improved patient outcomes.

# **YOLOv11:**
YOLOv11 is an advanced real-time object detection model designed to achieve higher accuracy and faster inference speeds compared to its predecessors. It incorporates enhanced architectural components, such as improved feature extraction, advanced attention mechanisms, and optimized loss functions, making it suitable for detecting complex patterns in challenging datasets. YOLOv11 is versatile and highly efficient, making it ideal for applications in healthcare, robotics, and other fields requiring precise object detection.

# **OpenCV:**
OpenCV (Open Source Computer Vision Library) is used for image processing tasks in this project. It helps in reading, displaying, and manipulating the images used for detection. OpenCV integrates seamlessly with YOLOv9, enabling effective and real-time detection.

# **Model:**
Download trained model trainable weights to load for real time testing from [here](https://universe.roboflow.com/brain-tumor-jolxi/brain-tumor-detection-o0ggc/dataset/2)

# **Dataset:**
You can download and check dataset from [here](https://universe.roboflow.com/brain-tumor-jolxi/brain-tumor-detection-o0ggc/dataset/2)

# **How to Run the Code:**
Install the required dependencies.

Run the TESTING.py file

Download the requirements.txt, replace the image path with your input image file and the YOLO model path with your trained model in the main.py code, then execute the script to detect brain tumor.

# **Example Output:**
Tumor (Confidence: 0.92)







