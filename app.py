from flask import Flask, request, jsonify
from services.email_service import send_email
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/send-message', methods=['POST'])
def send_email_route():
    data = request.json
    recipient_email = data.get('recipient_email')
    message_body = data.get('message_body')

    if not recipient_email or not message_body:
        return jsonify({"status": "error", "message": "All fields are required"}), 400

    response = send_email(recipient_email, message_body)
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
