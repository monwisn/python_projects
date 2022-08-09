# simple sending emails with subject and description (gmail)
import smtplib


# set your email and generated gmail password for third party apps
gmail_user = 'your gmail.com'
gmail_password = 'your password'

email_text = f"""

Subject: %s

%s
""" % ("subject", "description")

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user, "gmail.com", email_text)
    server.close()

except Exception as e:
    print(e)
    print('Something went wrong...')
