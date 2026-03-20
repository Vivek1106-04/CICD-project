from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Enable CORS so the frontend can successfully make requests to the backend
CORS(app)

@app.route('/student-details', methods=['GET'])
def get_student_details():
    return jsonify({
        "student_name": "Vivek",
        "roll_number": "2023bcs0175"
    })

if __name__ == '__main__':
    # Bind to all interfaces so Docker can route traffic
    app.run(host='0.0.0.0', port=5000)