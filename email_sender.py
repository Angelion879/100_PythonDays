import smtplib
from credentials import tester_login, tester_password
from email.message import EmailMessage

test_mail = EmailMessage()

test_mail['from'] = 'Myself'
test_mail['to'] = 'receiver@gmail.com'
test_mail['subject'] = 'First test on mailing!'

test_mail.set_content('This is me testing this!\nHello there!!')

with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465) as smtp:
  smtp.ehlo()
  smtp.login(tester_login, tester_password)
  smtp.send_message(test_mail)

  print('Mail Delivered!')
