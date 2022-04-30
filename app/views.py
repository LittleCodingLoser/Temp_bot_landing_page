from flask import render_template
from app import app
from flask import Flask, render_template, url_for, request, jsonify, json, redirect
from google.oauth2 import id_token
import sys
import os
from flask_wtf.csrf import CSRFProtect, CSRFError
from app import models
import pandas as pd
from github import Github

GOOGLE_OAUTH2_CLIENT_ID = os.getenv("GOOGLE_OAUTH2_CLIENT_ID")
GITHUB_ACCESS_TOKEN = os.getenv("GITHUB_ACCESS_TOKEN")

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

    health_leader_data = models.HealthLeader(
        int(request.form.get('health-leader-class')),
        request.form.get('health-leader-id'),
        request.form.get('health-leader-password'),
        request.form.get('email')
    )
    
    current_condition = health_leader_data.insert_to_db()

    return jsonify(condition = current_condition), 200


# render student form page
@app.route("/student_sing_up", methods = ["POST", "GET"])
def student_page():
    return render_template("student.html", google_oauth2_client_id = GOOGLE_OAUTH2_CLIENT_ID, csrf = csrf)

# student form submit
@app.route("/student_submit", methods=['POST'])
def student_submit():
    current_condition = "尚未註冊"
    studentData = models.Student(
        int(request.form.get('student-class')),
        int(request.form.get('student-seat_number')),
        request.form.get('email')
    )
    
    current_condition = studentData.insert_to_db()

    return jsonify(condition = current_condition), 200

@app.route("/email_redirect")
def email_redirect():

    # connect to the email_count.csv on github
    github = Github(GITHUB_ACCESS_TOKEN)
    repo = github.get_user().get_repo("Temp_bot_landing_page")
    contents = repo.get_contents("email_count.csv")

    # decode the content
    contentsString = contents.decoded_content.decode()

    # get the last grid on the csv, which is the email count of the day
    tableString = contentsString.split(',')

    # plus one to the count and make a new string
    tableString[-1] = str(int(tableString[-1]) + 1)
    newContents = ",".join(i for i in tableString)

    # update the csv
    repo.update_file(contents.path, "test", newContents, contents.sha)

    # redirect to the temperature uploading page
    return redirect("https://webap1.kshs.kh.edu.tw/kshsSSO/publicWebAP/bodyTemp/index.aspx")

# raise CSRF error 
@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return e.description, 400