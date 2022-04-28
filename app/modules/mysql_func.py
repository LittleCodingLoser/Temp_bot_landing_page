import mysql.connector
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def insert_student_data(student_class, seat_number, gmail):
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
    print(os.environ.get("MYSQL_HOST"))
    # 將學生資料插入學生table
    try:
        
        myCursor.execute("SELECT EXISTS(SELECT * FROM health_leader WHERE class = {0})".format(student_class))
        i = myCursor.fetchone()
        if not i[0]:
            raise ValueError("無該班環保股長資料")

        myCursor.execute("INSERT INTO Student (class, seat_number, gmail) VALUES (%s, %s, %s)", (student_class, seat_number, gmail))
        db.commit()
        student_condition = "註冊成功"
    except ValueError as ErrorMsg:
        student_condition = str(ErrorMsg)
    except Exception as e:
        if str(e)[0:12] == "1062 (23000)": # repeated primary key
            student_condition = "該資料已註冊過"
        else:
            student_condition = "Oops! 意外的錯誤產生了"

    myCursor.close()
    db.close()
    return student_condition

def insert_health_leader_data(health_leader_class, student_id, password, email):
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

    # 將衛生股長資料插入衛生股長table
    try:

        myCursor.execute("INSERT INTO health_leader (class, student_id, password, gmail) VALUES (%s, %s, %s, %s)", (health_leader_class, student_id, password, email))
        db.commit()
        health_leader_condition = "註冊成功"

    except Exception as e:
        if str(e)[0:12] == "1062 (23000)": # repeated primary key
            health_leader_condition = "該資料已註冊過"
        else:
            health_leader_condition = "Oops! 意外的錯誤產生了"

    myCursor.close()
    db.close()
    return health_leader_condition