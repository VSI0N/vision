# AI-Enhanced Railway Safety and Crowd Management

## Overview
AI-Enhanced Railway Safety and Crowd Management is an innovative project aimed at revolutionizing the Indian Railways by leveraging cutting-edge AI technology to address critical challenges faced by the railway sector. Our project focuses on real-time anomaly detection, crowd management, and crime prevention using the existing CCTV network.

## Objective
Our objective is to enhance passenger safety, comfort, and the overall travel experience within the Indian Railways by deploying state-of-the-art AI models and real-time data analysis. We aim to address the following key challenges:
- Real-time anomaly detection for enhanced crowd management and crime prevention.
- Efficient monitoring of maintenance tasks to ensure railway infrastructure remains safe and reliable.
- Providing immediate guidance and assistance to passengers during security threats or other emergencies.

## Key Features
- **AI Models:** We fine-tune deep learning models using Vision Transformer (ViT) and You Only Look Once (YOLO) for real-time anomaly detection.
- **Web Application:** Our AI seamlessly integrates into a user-friendly web application for accessible results.
- **CCTV Network Integration:** Utilizing existing CCTV infrastructure for real-time monitoring and enhanced security.
- **Frame Storage and Preprocessing:** Implementation of a frame storage system for capturing and preprocessing CCTV images.
- **GPS-Based Guidance:** Providing real-time route guidance during emergencies for passenger safety.

## Technological Stack
Our project leverages a robust technological stack, including:
- Hugging Face
- HTML, CSS
- Python Flask
- SQLAlchemy
- TensorFlow, PyTorch
- Google Maps Geolocation API
- GitHub
- OpenCV

## Installation

### Set Up a Virtual Environment
1. Create a virtual environment with `python3 -m venv venv`.
2. Activate the virtual environment using `source venv/bin/activate` on Linux/MacOS or `venv\Scripts\activate` on Windows.

### Install Dependencies
1. Install the required dependencies with `pip install -r requirements.txt`.

### Set Up the Database
1. Modify the `config.py` file to set up your database configuration.
2. Run `flask db upgrade` to set up the database.

### Run the Application
1. Start the application using `flask run`.
2. The app should now be running on `http://127.0.0.1:5000`.

## Docker Setup (Optional)

### Build the Docker Image
1. Build the Docker image with `docker build -t railway-safety-ai .`.

### Run the Docker Container
1. Run the Docker container with `docker run -p 5000:5000 railway-safety-ai`.
2. The app will be accessible at `http://localhost:5000`.

## Usage
For detailed usage instructions and examples, please refer to the User Guide.

## Partnerships
Our project's success depends on building strong collaborations with railway authorities, enabling integration with the IRCTC App, and gaining access to real-time location data to optimize crowd management and safety.

## Contributing
We welcome contributions from the community. If you'd like to contribute to our project, please refer to our Contribution Guidelines.

## License
This project is licensed under the MIT License.
