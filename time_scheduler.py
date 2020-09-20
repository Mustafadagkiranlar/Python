import schedule
import time

def job():
    print("one hour passed")

schedule.every(1 ).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(10)
