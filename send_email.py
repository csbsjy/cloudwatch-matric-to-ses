import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from datetime import datetime


EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_APP_KEY = os.environ['EMAIL_APP_KEY']
EMAIL_TARGET = os.environ['EMAIL_TARGET']


def send_email(daily_report_data):
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()  # TLS 사용시 필요
    smtp.login(EMAIL_HOST, EMAIL_APP_KEY)

    now = datetime.now()
    nowDate = now.strftime('%Y-%m-%d')

    msg = MIMEMultipart('related')
    msg['Subject'] = '['+nowDate+'] 백화점 디지털플랫폼 데일리리포트'

    msg_alternative = MIMEMultipart('alternative')
    msg.attach(msg_alternative)
    with open('template/daily-report.html', 'r') as f:
        html_string = f.read()
    msg_text = MIMEText(html_string, 'html')
    msg_alternative.attach(msg_text)

    image_id_list = ['<bdp_cpu_utilization>', '<bmt_cpu_utilization>', '<bpn_cid_cpu_utilization>',
                     '<cms_cpu_utilization>',
                     '<dbot_inf_cpu_utilization>', '<vip_cpu_utilization>', '<voc_waf_cpu_utilization>',
                     '<bdp_memory_utilization>', '<bpn_cid_memory_utilization>', '<cms_memory_utilization>',
                     '<dbot_inf_memory_utilization>', '<vip_memory_utilization>',
                     '<bdp_cid_cms_rds_utilization>', '<dbt_log_mdp_rds_utilization>', '<mis_rts_trd_rds_utilization>',
                     '<bdp_cid_cms_dbt_write_iops>', '<log_mdp_mis_rts_trd_write_iops>', '<bdp_cid_cms_dbt_read_iops>',
                     '<log_mdp_mis_rts_trd_read_iops>',
                     '<bdp_cid_cms_dbt_write_latency>', '<log_mdp_mis_rts_trd_write_latency>',
                     '<bdp_cid_cms_dbt_read_latency>', '<log_mdp_mis_rts_trd_read_latency>',
                     '<leader_0123_cpu_utilization>', '<4567_cpu_utilization>']

    for index, singleData in enumerate(daily_report_data):
        image = singleData
        msg_image = MIMEImage(image)
        image_id = image_id_list[index]
        msg_image.add_header('Content-ID', image_id)
        msg.attach(msg_image)

    email_target_list = EMAIL_TARGET.replace(' ', '').split(',')

    for emailTarget in email_target_list:
        msg['To'] = emailTarget
        smtp.sendmail(EMAIL_HOST, emailTarget, msg.as_string())

    smtp.quit()
