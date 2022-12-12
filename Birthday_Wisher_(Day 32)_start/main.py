# import smtplib

# my_email = "morriseberhard11@gmail.com"
# password = "in google"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="morriseberhard44@gmail.com", msg="Subject:LOLE\n\nDini MAMI ISCH FETT HEHE")


# import datetime as dt

# now = dt.datetime.now()             #----- datetime obj
# year = now.year                      #----- int
# month = now.month
# day_of_week = now.weekday()


# date_of_birth = dt.datetime(year=2002, month=1, day=3)
# print(date_of_birth)

import smtplib
import datetime as dt
import random



with open('./quotes.txt', 'r') as file:
    quotes = file.readlines()

new_quotes = []
for line in quotes:
    lines_stripped = line.strip()
    new_quotes.append(lines_stripped)

random_quote = random.choice(new_quotes)

today = dt.datetime.now()
weekday = today.weekday()


# if weekday == 4:
#     my_email = "morriseberhard11@gmail.com"
#     password = "in google"

#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(from_addr=my_email, to_addrs="morriseberhard44@gmail.com", msg=f"Subject:Depressing Quotes :(\n\n {random_quote}")
