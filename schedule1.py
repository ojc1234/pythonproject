import schedule
import time
import os
def job():
    os.system('D:\pythonproject\pythonproject\main0.1.py')
schedule.every(10).seconds.do(job)
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)