##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import pandas as pd
import datetime as dt
import random as rd

source_email = "ashwinalexandertest@gmail.com"
source_password = "nothereanymore"

def wish_happy_birthday():
    """ Read birthday info off of the list if birthday, send random birthday wish """
    df_birthdays = pd.read_csv("birthdays.csv")
    birthday_note = get_birthday_note()
    for index, row in df_birthdays.iterrows():
        is_birthday = check_birthday_today(row)
        if is_birthday:
            sendEmail(birthday_note.replace("[NAME]",row["name"]), row["email"])


def get_birthday_note():
    """pick a random birthday message template is all that is happening here, no big deal"""
    letterFile = rd.choice(["letter_1.txt","letter_2.txt","letter_3.txt"])
    with open(f"letter_templates/{letterFile}") as f:
        full_message = f.read()
        return full_message

def check_birthday_today(row):
    """only checks if the record features a day that is today"""
    now = dt.datetime.now()
    m_o_y = now.month
    d_o_m = now.day

    return row["month"] == m_o_y and row["day"] == d_o_m

def sendEmail(birthdayNote, birthdayEmail):
    """only sends email with a note to the destinateur"""
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=source_email, password=source_password)
        connection.sendmail(
            from_addr=source_email,
            to_addrs=birthdayEmail,
            msg=birthdayNote)
    print("email sent")

# start the process of wishing people in the list
wish_happy_birthday()

