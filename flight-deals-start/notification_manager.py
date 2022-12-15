import smtplib

MY_EMAIL = "morriseberhard11@gmail.com"
PASSWORD= "on replit"

class NotificationManager:
    
    def send_email(self):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=f'{None}', msg=f"Subject:HappyBirthday\n\n{None}")
