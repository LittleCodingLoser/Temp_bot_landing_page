from app.modules.mysql_func import insert_student_data, insert_health_leader_data
from app.modules.crawl import check_health_leader
from app.modules.class_exist import check_class

# models that handle with inserting data into the database

def InsertStudentData(student_class, seat_number, gmail):
    try:
        # check the validation of the data
        if not check_class(student_class):
            raise ValueError("班級不存在啊")
        
        student_condition = insert_student_data(student_class, seat_number, gmail)

    except ValueError as ErrorMsg:
        student_condition = str(ErrorMsg)
    except Exception as e:
        student_condition = "Oops! 意外的錯誤產生了"
    return student_condition

def InsertHealthLeaderData(health_leader_class, student_id, password, email):
    try:
        # check the validation of the data
        if not check_class(health_leader_class):
            raise ValueError("班級不存在啊")
        result = check_health_leader(health_leader_class, student_id, password)
        if result == 0:
            raise ValueError("帳密無法用於登入")
        elif result == -1:
            raise ValueError("帳密不屬於該班級")

        health_leader_condition = insert_health_leader_data(health_leader_class, student_id, password, email)
    except ValueError as ErrorMsg:
        health_leader_condition = str(ErrorMsg)
    except Exception as e:
        health_leader_condition = "Oops! 意外的錯誤產生了"

    return health_leader_condition