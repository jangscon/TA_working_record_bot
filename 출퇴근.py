from selenium import webdriver # 동적 사이트 수집
# from webdriver_manager.chrome import ChromeDriverManager # 크롬 드라이버 설치 
# from selenium.webdriver.chrome.service import Service # 자동적 접근
# from selenium.webdriver.chrome.options import Options # 크롭 드라이버 옵션 지정
from selenium.webdriver.common.by import By # find_element 함수 쉽게 쓰기 위함
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from time import sleep
from datetime import datetime
import schedule 

from config import WORK_DETAILS, START_TIME, END_TIME
from mailtest import send_email

def login_and_go_page(driver):
    driver.get("https://appfn.knu.ac.kr/login.knu?agentId=4")  # 여기에 로그인할 사이트의 URL을 넣음

    # 로그인 폼 채우기 (예시)
    username = driver.find_element(By.ID, "idpw_id")  # 아이디 필드 요소 찾기
    password = driver.find_element(By.ID, "idpw_pw")  # 비밀번호 필드 요소 찾기

    username.send_keys("")  # 사용자명 입력
    password.send_keys("")  # 비밀번호 입력

    # 로그인 버튼 클릭
    login_button = driver.find_element(By.ID, "btn-login")  # 로그인 버튼 요소 찾기
    login_button.click()

    # 로그인 이후 작업
    sleep(3)  # 페이지가 로드될 시간을 기다림 (필요에 따라 조정)

    
    popup_close = driver.find_element(By.XPATH, '//*[@title="창닫기"]')
    popup_close.click()
    sleep(1)


    # 예시로 특정 버튼 클릭
    some_button = driver.find_element(By.ID, "mainSnb_title_level2_acc_MNU0010728")
    some_button.click()
    sleep(1)
    some_button = driver.find_element(By.ID, "mainSnb_level3_snbList_button_MNU0010815")
    some_button.click()
    sleep(1)
    some_button = driver.find_element(By.ID, "mainSnb_level3_snbList_ul_MNU0010815")
    some_button.click()
    sleep(1)

def go_to_work():
    driver = webdriver.Chrome()

    login_and_go_page(driver)
    try:
        # 5 = 출근버튼, 8 = 퇴근버튼, 12 = 근무내용입력칸
        tr_tag = driver.find_element(By.XPATH,'//*[@id="tabContentMain_contents_tabPgmMNU0012812_body_grid02_body_tbody"]')
        columns = tr_tag.find_elements(By.TAG_NAME, "tr")

        today = int(datetime.today().day)
        if today < 7:
            column = columns[today-1].find_elements(By.TAG_NAME, "td")
        else:
            column = columns[-1].find_elements(By.TAG_NAME, "td")

        for i in column:
            if not i.text:
                print(0,end="")
            else :
                print(i.text,end="")
        print()
        btn = column[5].find_element(By.TAG_NAME, "button")
        print(btn)
        print(btn.text)
        #btn.send_keys(Keys.ENTER)
        #driver.execute_script("arguments[0].click();", btn)
        
    except Exception as e:
        print(f"입력 실패!! / Error: {e}")
        msg_text = "TA 출근을 실패하였습니다! 꼭 웹사이트에 들어가서 확인해주세요!!!"
        send_email("☢️ 비상 비상 TA출근 실패!!!! ☢️", msg_text)
        
    
    driver.quit()

def leave_work():
    driver = webdriver.Chrome()

    login_and_go_page(driver)
    
    try:
        # 5 = 출근버튼, 8 = 퇴근버튼, 12 = 근무내용입력칸
        tr_tag = driver.find_element(By.XPATH,'//*[@id="tabContentMain_contents_tabPgmMNU0012812_body_grid02_body_tbody"]')
        columns = tr_tag.find_elements(By.TAG_NAME, "tr")

        today = int(datetime.today().day)
        if today < 7:
            column = columns[today-1].find_elements(By.TAG_NAME, "td")
        else:
            column = columns[-1].find_elements(By.TAG_NAME, "td")

        btn = column[8].find_element(By.TAG_NAME, "button")
        work_details = column[12].find_element(By.TAG_NAME, "input")
        sleep(2)
        driver.execute_script("arguments[0].click();", btn)
        
    except Exception as e:
        print(f"입력 실패!! / Error: {e}")
        msg_text = "TA 퇴근을 실패하였습니다! 꼭 웹사이트에 들어가서 확인해주세요!!!"
        send_email("☢️ 비상 비상 TA퇴근 실패!!!! ☢️", msg_text)
    
    driver.quit()



# schedule.every().monday.at(START_TIME[0]).do(go_to_work)
# schedule.every().tuesday.at(START_TIME[0]).do(go_to_work)
# schedule.every().wednesday.at(START_TIME[0]).do(go_to_work)
# schedule.every().thursday.at(START_TIME[0]).do(go_to_work)
# schedule.every().friday.at(START_TIME[0]).do(go_to_work)

# schedule.every().monday.at(END_TIME[0]).do(leave_work)
# schedule.every().tuesday.at(END_TIME[0]).do(leave_work)
# schedule.every().wednesday.at(END_TIME[0]).do(leave_work)
# schedule.every().thursday.at(END_TIME[0]).do(leave_work)
# schedule.every().friday.at(END_TIME[0]).do(leave_work)

# schedule.every().monday.at(START_TIME[1]).do(go_to_work)
# schedule.every().tuesday.at(START_TIME[1]).do(go_to_work)
# schedule.every().wednesday.at(START_TIME[1]).do(go_to_work)
# schedule.every().thursday.at(START_TIME[1]).do(go_to_work)
# schedule.every().friday.at(START_TIME[1]).do(go_to_work)

# schedule.every().monday.at(END_TIME[1]).do(leave_work)
# schedule.every().tuesday.at(END_TIME[1]).do(leave_work)
# schedule.every().wednesday.at(END_TIME[1]).do(leave_work)
# schedule.every().thursday.at(END_TIME[1]).do(leave_work)
# schedule.every().friday.at(END_TIME[1]).do(leave_work)

#참고 : https://jimmy-ai.tistory.com/451

# while True:
#     try:
#         print(1)
#         schedule.run_pending()
#     except:
#         pass
#     sleep(1)

go_to_work()