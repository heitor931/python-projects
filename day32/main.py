import smtplib

my_email = 'heitorino1@gmail.com'
recipient = "principeheitor70@hotmail.com"
password = 'zjqz hqos hwpr nbks'
message = 'Subject: Test from python\n\n Life has more content in it than we could ever imagine!'

try:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=recipient, msg=message)
except smtplib.SMTPAuthenticationError:
    print("There was an authentication error")
except smtplib.SMTPConnectError:
    print("There was a connection error")
else:
    print("Email sent successfully")

