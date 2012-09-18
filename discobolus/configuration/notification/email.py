import smtplib

def send_test_email(obj):

    smtpserver = smtplib.SMTP(obj.smtp_server,obj.smtp_server_port, timeout=6)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.login(obj.account_name, obj.account_password)
    header = 'To: {0}\nFrom: {1}\nSubject:discobolus test\n'.format(obj.email_recipient, obj.email_sender)
    msg = header + '\nThis is test e-mail from discobolus\n\n'
    smtpserver.sendmail(obj.account_name, obj.email_recipient, msg)

