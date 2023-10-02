import smtplib

source_email = "ashwinalexandertest@gmail.com"
source_password = "blah"
destination_email = "ashwinalexandertest@yahoo.com"


connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=source_email, password=source_password)
connection.sendmail(from_addr=source_email, to_addrs=destination_email, msg="test email")
connection.close()
