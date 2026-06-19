# Image Analyzer API[Task-3]

A Flask-based image processing API that accepts JPEG image uploads, analyzes image brightness using OpenCV, draws a bounding box around the center region of the image, and returns analysis results in JSON format.

#Features

- Upload JPEG images through a REST API
- Process images using OpenCV
- Convert images to grayscale
- Calculate average image brightness
- Draw a 100×100 bounding box around the image center
- Return results as a JSON response
- Error handling for invalid or missing uploads

#Tech Stack

1. Backend
    - Python 3.x
    - Flask
2. Image Processing
    - OpenCV
    - NumPy
3. Testing Tools
    - Postman
    - curl

#Running the Application

- Start the Flask server:

python app.py

Expected output:

* Running on http://127.0.0.1:5000
- Testing the API
1. Using Postman
Create a POST request.
Use URL:
http://127.0.0.1:5000/api/analyze
Open Body → form-data.
Add a field:
Select an image.
Click Send.
2. Using curl
curl.exe -X POST -F "image=@testimg.jpg" http://127.0.0.1:5000/api/analyze [run this command on powershell]