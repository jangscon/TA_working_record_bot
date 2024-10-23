from 출퇴근 import *
import schedule 

schedule.every().wednesday.at("13:15").do(go_to_work)

while True:
    try:
        schedule.run_pending()
    except:
        pass
    sleep(1)