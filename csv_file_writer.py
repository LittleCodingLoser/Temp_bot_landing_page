import csv
import pandas as pd
from apscheduler.schedulers.blocking import BlockingScheduler
import bots.modules.timer as timer
import datetime 
from datetime import datetime,timezone,timedelta

sched = BlockingScheduler()

filename = "email_count.csv"

# The first column is Date and the second is Email_count
# set a daily job that will insert a new row of email_count for the day
@sched.scheduled_job('cron', day_of_week='mon-sun', hour=6, timezone='Asia/Taipei')
def bot_work():
    if timer.check_date():
        with open (filename, "w", newline = "") as csvfile:
            email_count = csv.writer(csvfile)
            time = datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S")
            date = time[:10]
            email_count.writerow((date, 0))

sched.start()