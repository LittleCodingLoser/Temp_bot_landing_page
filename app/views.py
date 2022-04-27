from flask import render_template
from app import app
from flask import Flask, render_template, url_for, request, jsonify, json
from google.oauth2 import id_token
from google.auth.transport import requests
import sys
import os
from flask_wtf.csrf import CSRFProtect, CSRFError
from app import models

GOOGLE_OAUTH2_CLIENT_ID = os.environ.get("GOOGLE_OAUTH2_CLIENT_ID")


app.config['SECRET_KEY'] = os.urandom(24)

csrf = CSRFProtect(app)

@app.route("/", methods=['GET', 'POST'])
def main_page():
    return render_template("main.html") 

# render health leader form page
@app.route("/recycle_sign_up", methods = ["POST", "GET"])
def health_leader_page():
    return render_template("health_leader_page.html", google_oauth2_client_id = GOOGLE_OAUTH2_CLIENT_ID, csrf = csrf)

# health leader form submit
@app.route("/health_leader_submit", methods=['POST'])
def health_leader_submit():
    current_condition = "尚未註冊"
    healthLeaderClass = int(request.form.get('health-leader-class'))
    id = request.form.get('health-leader-id')
    password = request.form.get('health-leader-password')
    gmail = request.form.get('email')
    
    current_condition = models.InsertHealthLeaderData(healthLeaderClass, id, password, gmail)

    return jsonify(condition = current_condition), 200


# render student form page
@app.route("/student_sing_up", methods = ["POST", "GET"])
def student_page():
    return render_template("student.html", google_oauth2_client_id = GOOGLE_OAUTH2_CLIENT_ID, csrf = csrf)

# student form submit
@app.route("/student_submit", methods=['POST'])
def student_submit():
    current_condition = "尚未註冊"
    studentClass = int(request.form.get('student-class'))
    number = int(request.form.get('student-seat_number'))
    gmail = request.form.get('email')
    
    current_condition = models.InsertStudentData(studentClass, number, gmail)

    return jsonify(condition = current_condition), 200

# raise CSRF error 
@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return e.description, 400

# if __name__ == "__main__":
#     app.debug = True
#     app.run()