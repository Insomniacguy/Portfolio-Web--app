import smtplib
import ssl

host = "smtp.gmail.com"
port = 465
# unsecure way to store passwords. The more secure way is to store it in env variables
username = "r00t7h3ll@gmail.com"
password = "trgixhavcuiffxdh"
receiver = "rahulchandan1991@gmail.com"
subject = "Python rocks"
# host, port, context

# backslash indicates there is no new line. For subject
message = """\
Subject: Python indeed rocks
Does this work??
Testing
Bye!
"""

context = ssl.create_default_context()

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)

