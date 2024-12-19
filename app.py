import requests
from flask import Flask, request, jsonify
from services.email_service import send_email
from flask_cors import CORS
from config import Config

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


@app.route('/send-candidate-message', methods=['POST'])
def send_candidate_message():
    data = request.json
    message_body = data.get('message_body')
    id_value = data.get('id')

    if not message_body or not id_value:
        return jsonify({"status": "error", "message": "All fields are required"}), 400
    print(Config.COOKIE, Config.APOLLO)
    url = "https://wellfound.com/graphql"
    headers = {
        "Cookie": 'cookie-here',
        "Origin": "https://wellfound.com",
        "X-Angellist-Dd-Client-Referrer-Resource": "/jobs/messages/:id?",
        "X-Apollo-Operation-Name": "CandidateSendMessage",
        "X-Apollo-Signature": Config.APOLLO,
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Referer": f"https://wellfound.com/jobs/messages/{id_value}"
    }
    payload = {
        "operationName": "CandidateSendMessage",
        "variables": {
            "input": {
                "id": id_value,
                "type": "JOBPAIRING",
                "body": message_body
            }
        },
        "extensions": {
            "operationId": "tfe/1ee8d94da36a0811d05340d91a4427175dbb8abfafe2dab802483d375fdcfb7d"
        }
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
