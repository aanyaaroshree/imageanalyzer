from flask import Flask, request, jsonify
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/api/analyze', methods=['POST'])
def analyze():

    if 'image' not in request.files:
        return jsonify({"status": "error", "message": "No image uploaded"}), 400

    file = request.files['image']

    file_bytes = np.frombuffer(file.read(), np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if image is None:
        return jsonify({"status": "error", "message": "Invalid image"}), 400

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    brightness = float(np.mean(gray))

    h, w = image.shape[:2]

    center_x = w // 2
    center_y = h // 2

    half = 50

    cv2.rectangle(
        image,
        (center_x - half, center_y - half),
        (center_x + half, center_y + half),
        (0, 255, 0),
        2
    )

    return jsonify({
        "status": "processed",
        "brightness": round(brightness, 2)
    })

if __name__ == "__main__":
    app.run(debug=True)