from bots.modules import crawl, timer, email_func as email, mysql_func as DB, send_line_message as LINE


def activate_bot():
    
    # 遍歷每班的衛生股長
    health_leader_list = DB.select_health_leader()
    line_message = "\n還沒填體溫的名單\n"

    for i in health_leader_list:

        # 爬蟲該班學生的座號與體溫並建表
        temp_table = crawl.crawl_temp_data(i[1], i[2])

        # 將未填名單建立成line訊息字串
        line_message += f"{i[0]}: "
        
        # 建表 key是座號 value是Gmail
        student_list = DB.select_student(i[0])
        email_table = { j[1]: j[2] for j in student_list }

        # 遍歷temp_table並發信 若該學生未上傳體溫(體溫呈現nan)且DB中有他的Gmail再發信 再寄信給環保 通知有多少人沒填體溫
        for j in range(1, len(temp_table) + 1):
            if str(temp_table["溫度"][j]) == "nan": # 沒填體溫

                # 只要沒填就插進line字串裡
                line_message += str(temp_table["座號"][j]) + " "

                # 如果又恰好有註冊機器人服務則發信
                if email_table.get(temp_table["座號"][j], False):
                    email.send_email_to_regular_user(email_table.get(temp_table["座號"][j]))

        line_message += "\n"
    
    line_message += "好ㄟ就這樣"
    LINE.lineNotifyMessage(line_message)