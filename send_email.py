import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

from daily_report_form import daily_report_form

EMAIL_HOST = os.environ['EMAIL_ADDRESS']
EMAIL_TARGET = os.environ['EMAIL_TARGET']
EMAIL_APPKEY = os.environ['EMAIL_APP_KEY']

def send_email(daily_report_data):
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()  # TLS 사용시 필요
    smtp.login(EMAIL_HOST, EMAIL_APPKEY)

    msg = MIMEMultipart('related')
    msg['Subject'] = '[테스트] 백화점 디지털플랫폼 데일리레포트'
    msg['To'] = EMAIL_TARGET

    msg_alternative = MIMEMultipart('alternative')
    msg.attach(msg_alternative)
    msg_text = MIMEText(daily_report_form, 'html')
    msg_alternative.attach(msg_text)

    image_id_list = ['<cpu_credit>', '<cpu_utilization>']

    for index, singleData in enumerate(daily_report_data):
        image = singleData
        msg_image = MIMEImage(image)
        image_id = image_id_list[index]
        msg_image.add_header('Content-ID', image_id)
        msg.attach(msg_image)


    smtp.sendmail(EMAIL_HOST, EMAIL_TARGET, msg.as_string())

    smtp.quit()