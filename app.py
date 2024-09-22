from flask import Flask, request, jsonify
from flask_cors import CORS
import base64

app = Flask(__name__)
CORS(app, resources={r"/bfhl": {"origins": "*"}})



# POST route that accepts the JSON input and processes the data
@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data = request.json.get('data', [])
        file_b64 = request.json.get('file_b64', None)
        
        # Process numbers and alphabets
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        lowercase_alphabets = [char for char in data if char.islower()]

        # Find the highest lowercase alphabet (if present)
        highest_lowercase_alphabet = [max(lowercase_alphabets)] if lowercase_alphabets else []

        # User ID (this could be dynamically set by user input or hardcoded for testing)
        user_id = "ayaan_momin_10052003"
        email = "am4400@srmist.edu.in"
        roll_number = "RA2111026030142"

        # File handling
        file_valid = False
        file_mime_type = ""
        file_size_kb = 0

        if file_b64:
            try:
                # Decode the base64 string to validate the file
                file_data = base64.b64decode(file_b64)
                file_valid = True
                file_size_kb = len(file_data) / 1024  # file size in KB
                file_mime_type = "application/octet-stream"  # Placeholder MIME type
            except Exception as e:
                file_valid = False
        
        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase_alphabet,
            "file_valid": file_valid,
            "file_mime_type": file_mime_type,
            "file_size_kb": file_size_kb
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400

# GET route that returns a hardcoded operation code
@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200


if __name__ == '__main__':
    app.run()