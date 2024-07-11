# import smtplib
#
# my_mail = "sharyuadsul19@gmail.com"
# password = "jlufobupeorayteq"
#
# with smtplib.SMTP("smtp.gmail.com", 587) as conn:
#     conn.starttls()
#     conn.login(user= my_mail, password=password)
#     conn.sendmail(from_addr=my_mail,
#                   to_addrs="gellerrmon002@gmail.com",
#                   msg="Subject: Hello\n\nThis is the body of the mail")


import datetime as dt

now= dt.datetime.now()
# print(now)
# print(now.year)
# print(now.weekday())

my_bday = dt.datetime(year=2003, month=3, day=19)
print(my_bday)

