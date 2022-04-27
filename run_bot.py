from apscheduler.schedulers.blocking import BlockingScheduler
from bots.bot import activate_bot
from bots.bot_2 import activate_bot_2
import bots.modules.timer as timer

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=9, timezone='Asia/Taipei')
def bot_work():
    if timer.check_date():
        activate_bot()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=10, timezone='Asia/Taipei')
def bot_work():
    if timer.check_date():
        activate_bot()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=10, minute=10, timezone='Asia/Taipei')
def bot_2_work():
    if timer.check_date():
        activate_bot_2()

sched.start()