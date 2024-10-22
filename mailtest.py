import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders

from config import GMAIL_ADDRESS, GMAIL_PASSWORD

def send_email(subject, body):

    # 이메일 구성
    msg = MIMEMultipart()
    msg['From'] = GMAIL_ADDRESS
    msg['To'] = GMAIL_ADDRESS
    msg['Subject'] = subject

    # 이메일 본문 추가
    msg.attach(MIMEText(body, 'plain'))

    # 이메일 서버를 통해 이메일 전송
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(GMAIL_ADDRESS, GMAIL_PASSWORD)
    text = msg.as_string()
    server.sendmail(GMAIL_ADDRESS, GMAIL_ADDRESS, text)
    server.quit()
    
if __name__ == "__main__":
    send_email("축하합니다. 이제 메일을 사용할 수 있겠네요.","발생한 문제는 제가 책임지지 않습니다~")