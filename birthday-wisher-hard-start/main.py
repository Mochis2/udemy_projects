import smtplib
import datetime as dt
import pandas
import random

MY_EMAIL = "morriseberhard11@gmail.com"
PASSWORD = "in google"


data = pandas.read_csv('./birthdays.csv')


now = dt.datetime.now()
today = now.day
this_month = now.month
today_tuple = (this_month, today)

data = pandas.read_csv('./birthdays.csv')
random_letter = random.randint(1,3)


birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
birthday_email = birthdays_dict[today_tuple]['email']
# print(birthdays_dict)
if today_tuple in birthdays_dict:
    birthday_name = birthdays_dict[today_tuple]['name']
    with open(f'./letter_templates/letter_{random_letter}.txt', 'r') as file:
        letter_text = file.read()
        content = letter_text.replace('[NAME]', f'{birthday_name}')
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=f'{birthday_email}', msg=f"Subject:HappyBirthday\n\n{content}")





##################### Hard Starting Project ######################


# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



