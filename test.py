import schedule
import time

def job():
    print("자연, 우리의 미래...")

schedule.every().tuesday.at("19:51").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)


