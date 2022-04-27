import smtplib
import email.message
import os

def send_email_to_regular_user(user):
    try:
        # 信件內文
        msg = email.message.EmailMessage()
        msg["From"] = "kshstemperaturebot@gmail.com"
        msg["To"] = user 
        msg["Subject"] = "你484還沒填體溫"
        msg.add_alternative("""
            <h3>快填體溫，不然被罰愛校!</h3>
            <p>傳送門在這</p>
            <a href="https://webap1.kshs.kh.edu.tw/kshsSSO/publicWebAP/bodyTemp/index.aspx">點我</a>
            <p>話說spy family真的很好看</p>
            <img src = "https://i.imgur.com/aY9L5Zq.jpg" style = "width: 273px; height: 184px">
        """, subtype = "html")

        # 寄出
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("kshstemperaturebot@gmail.com", os.environ.get("EMAIL_PASSWORD"))
        server.send_message(msg)
        print("Email sent successfully")
        server.close()
    except Exception as e:
        print(f"Fail to send mail to {user} cuz {e}")

def send_email_to_health_leader(user, cnt, student_list):
    try:
        # 信件內文
        msg = email.message.EmailMessage()
        msg["From"] = "kshstemperaturebot@gmail.com"
        msg["To"] = user 
        msg["Subject"] = f"你們班還有{cnt}個人沒填體溫"
        msg_content = "\n".join(str(i) for i in student_list)
        msg.set_content(f"{msg_content}還沒填體溫喔\n如果這些同學還沒註冊的話請幫忙大力督促")

        # 寄出
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("kshstemperaturebot@gmail.com", os.environ.get("EMAIL_PASSWORD")) 
        server.send_message(msg)
        print("Email sent successfully")
        server.close()
    except Exception as e:
        print(f"Fail to send mail to {user} cuz {e}")