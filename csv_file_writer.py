import csv
import pandas as pd
from apscheduler.schedulers.blocking import BlockingScheduler
import bots.modules.timer as timer
import datetime 
from datetime import datetime,timezone,timedelta
from github import Github
import os

sched = BlockingScheduler()

GITHUB_ACCESS_TOKEN = os.environ.get('GITHUB_ACCESS_TOKEN')

# The first column is Date and the second is Email_count
# set a daily job that will insert a new row of email_count for the day
@sched.scheduled_job('cron', day_of_week='mon-sun', hour=6, timezone='Asia/Taipei')
def bot_work():
    if timer.check_date():
        # get the date
        time = datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S")
        date = time[:10]
        
        # connect to the email_count.csv on github
        github = Github(GITHUB_ACCESS_TOKEN)
        repo = github.get_user().get_repo("Temp_bot_landing_page")
        contents = repo.get_contents("email_count.csv")

        # decode the content
        contentsString = contents.decoded_content.decode()

        # get the last grid on the csv, which is the email count of the day
        newContents = f"{contentsString}\n{date},0"

        # update the csv
        repo.update_file(contents.path, "test", newContents, contents.sha)

sched.start()