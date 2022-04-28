import mysql.connector
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def select_health_leader():
    # 初始化連接
    db = mysql.connector.connect(
        host = os.environ.get("MYSQL_HOST"),
        user = os.environ.get("MYSQL_USER"),
        password = os.environ.get("MYSQL_PASSWORD"),
        database = os.environ.get("MYSQL_DATABASE"),
        buffered = True,
        use_pure=True
    )
    myCursor = db.cursor(buffered = True) 

    myCursor.execute("SELECT * FROM health_leader")
    health_leader_list = myCursor.fetchall()
    myCursor.close()
    db.close()
    return health_leader_list

def select_student(class_number):
    # 初始化連接
    db = mysql.connector.connect(
        host = os.environ.get("MYSQL_HOST"),
        user = os.environ.get("MYSQL_USER"),
        password = os.environ.get("MYSQL_PASSWORD"),
        database = os.environ.get("MYSQL_DATABASE"),
        buffered = True,
        use_pure=True
    )
    myCursor = db.cursor(buffered = True) 

    myCursor.execute("SELECT * FROM Student Where class = " + str(class_number))
    student_list = myCursor.fetchall()
    myCursor.close()
    db.close()
    return student_list