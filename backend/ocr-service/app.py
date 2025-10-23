from flask import Flask, request, jsonify
from flask_cors import CORS
import easyocr
import cv2
import numpy as np
import io
from PIL import Image

app = Flask(__name__)
CORS(app)

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "OCR service is running", "service": "EasyOCR API"})

@app.route('/extract_text', methods=['POST'])
def extract_text():
    try:
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided"}), 400
        
        file = request.files['image']
        if file.filename == '':
            return jsonify({"error": "No file selected"}), 400
        
        # Read image file
        image_bytes = file.read()
        image = Image.open(io.BytesIO(image_bytes))
        
        # Convert to numpy array for OpenCV
        image_array = np.array(image)
        
        # Perform OCR
        results = reader.readtext(image_array)
        
        # Format results
        extracted_text = []
        for (bbox, text, confidence) in results:
            extracted_text.append({
                "text": text,
                "confidence": float(confidence),
                "bbox": bbox
            })
        
        return jsonify({
            "success": True,
            "text_blocks": extracted_text,
            "full_text": " ".join([item["text"] for item in extracted_text])
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
