from app.modules.crawl import check_health_leader
from app.modules.class_exist import check_class
import os
import mysql.connector

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# models that handle with inserting data into the database
class HealthLeader():
    def __init__(self, health_leader_class, student_id, password, email):
        self.health_leader_class = health_leader_class
        self.student_id = student_id
        self.password = password
        self.email = email

    def insert_to_db(self):
        try:
            # check the validation of the data
            if not check_class(self.health_leader_class):
                raise ValueError("班級不存在啊")
            result = check_health_leader(self.health_leader_class, self.student_id, self.password)
            if result == 0:
                raise ValueError("帳密無法用於登入")
            elif result == -1:
                raise ValueError("帳密不屬於該班級")

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
            myCursor.execute("INSERT INTO health_leader (class, student_id, password, gmail) VALUES (%s, %s, %s, %s)", (self.health_leader_class, self.student_id, self.password, self.email))
            db.commit()
            health_leader_condition = "註冊成功"

            myCursor.close()
            db.close()
        except ValueError as ErrorMsg:
            health_leader_condition = str(ErrorMsg)
        except Exception as e:
            if str(e)[0:12] == "1062 (23000)": # repeated primary key
                health_leader_condition = "該資料已註冊過"
            else:
                health_leader_condition = "Oops! 意外的錯誤產生了"

        return health_leader_condition


class Student():
    def __init__(self, student_class, seat_number, gmail):
        self.student_class = student_class
        self.seat_number = seat_number
        self.gmail = gmail

    def insert_to_db(self):
        try:
            # check the validation of the data
            if not check_class(self.student_class):
                raise ValueError("班級不存在啊")
            
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
            # 將學生資料插入學生table
                
            myCursor.execute("SELECT EXISTS(SELECT * FROM health_leader WHERE class = {0})".format(self.student_class))
            i = myCursor.fetchone()
            if not i[0]:
                raise ValueError("無該班環保股長資料")

            myCursor.execute("INSERT INTO Student (class, seat_number, gmail) VALUES (%s, %s, %s)", (self.student_class, self.seat_number, self.gmail))
            db.commit()
            student_condition = "註冊成功"
        
            myCursor.close()
            db.close()

        except ValueError as ErrorMsg:
            student_condition = str(ErrorMsg)
        except Exception as e:
            if str(e)[0:12] == "1062 (23000)": # repeated primary key
                student_condition = "該資料已註冊過"
            else:
                student_condition = "Oops! 意外的錯誤產生了"
        return student_condition