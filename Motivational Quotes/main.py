import smtplib
import datetime as dt
import random

MY_EMAIL = "auscultarem@gmail.com"
MY_PASSWORD = "12345" 

now = dt.datetime.now()
weekday = now.weekday()

# check the weekday, you will not see nothing if there is not coincidence
if weekday == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

        print(quote)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL,MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f"Subject:Day Motivation\n\n{quote}"
                                )
# import smtplib
#
# my_email = "auscultarem@gmail.com"
# password = "12345"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="auscultarem@hotmail.com",
#                         msg="Subject:Hello\n\nThis is the body of my email."
#                         )

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# day_of_weak = now.weekday()
# print(now)
# print(year)
# print(day_of_weak)

