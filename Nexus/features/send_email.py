import smtplib


def mail(receiver_email, msg):
    sender_email = "meetnp007@gmail.com"
    sender_password = "M@082021"
    try:
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(sender_email, sender_password)
        mail.sendmail(sender_email, receiver_email, msg)
        mail.close()
        return True
    except Exception as e:
        print(e)
        return False