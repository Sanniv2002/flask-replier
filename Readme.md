# Message Sender App

This is a simple web application that allows users to send messages via email to specific threads on Wellfound (formerly AngelList). The app is built with a Python Flask backend and a frontend for user interaction.

---

## Features

- Send messages to a specified thread email (optional field).
- Validate input for email format and message content.
- Secure email sending using SMTP with app-specific passwords.

---

## Tech Stack

- **Backend**: Python Flask
- **Frontend**: React
- **Email Sending**: SMTP via Python's `smtplib`

---

## Prerequisites

1. **Python**: Make sure Python 3.7+ is installed.
2. **SMTP Configuration**:
   - A Gmail account or another email provider that supports SMTP.
   - For Gmail, enable **2-Step Verification** and create an **App Password**.
3. **Frontend**:
   - Already integrated with this backend for sending requests.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Sanniv2002/flask-replier.git
   cd flask-replier

2. Create a virtual environment:
   ```bash
   python -m venv ./venv
   source ./venv/bin/activate
   pip install -r requirements.txt

3. Start the flask server:
   ```bash
   export $(cat .env | xargs)
   python app.py
