from bots.modules import crawl, timer, email_func as email, mysql_func as DB, send_line_message as LINE

def activate_bot_2():

    # 遍歷每班的衛生股長
    health_leader_list = DB.select_health_leader()
    line_message = "\n逾時填報人數\n"

    for i in health_leader_list:

        # 爬蟲該班學生的座號與體溫並建表
        temp_table = crawl.crawl_temp_data(i[1], i[2])

        # 遍歷temp_table 若該學生未上傳體溫(體溫呈現nan) 就增加未填報的人數 再寄信給環保 通知有多少人沒填體溫
        studentCnt = 0
        users_have_not_upload_cnt = 0
        student_list = []

        # 尋找已註冊的使用者 計算已註冊但仍未填體溫的數量
        user_list = DB.select_student(i[0])
        user_set = { j[1] for j in user_list }

        for j in range(1, len(temp_table) + 1):
            if str(temp_table["溫度"][j]) == "nan":
                studentCnt += 1
                student_list.append(temp_table["姓名"][j])
                if temp_table["座號"][j] in user_set:
                    users_have_not_upload_cnt += 1
        print(f"{i[0]} : {studentCnt} students have not uploaded and {users_have_not_upload_cnt} of them are temp_bot users")

        line_message += f"{i[0]}有{studentCnt}人未填報\n"
        email.send_email_to_health_leader(i[3], studentCnt, student_list)
    
    line_message += "好ㄟ就這樣"
    LINE.lineNotifyMessage(line_message)