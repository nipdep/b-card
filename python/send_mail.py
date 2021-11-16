# 06-09-2020

import smtplib,ssl
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

root_path = "./banned_tickets/"
port = 465
smtp_server = "smtp.gmail.com"
sender_email = "deelaka1nipun@gmail.com"
sender_password = "96dela98nip"

msg = MIMEMultipart("alternative")
msg["Subject"] = "ticket"
msg["From"] = "moranrc@gmail.com"

html = """
<div id="output"></div>
<!-- Load Babel -->
<script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script> 
<script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
<!-- Your custom script here -->
<script type="text/babel">
const getMessage = () => "Hello World";
document.getElementById('output').innerHTML = getMessage();
</script>
"""


# Turn these into plain/html MIMEText objects
part2 = MIMEText(html, "html")

msg.attach(part2)

text = msg.as_string()

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, "nipun1deelaka@gmail.com", text)
    print("succefully send the mail.")

def sender(name,code,mail):
    reciever_email = mail
    msg["To"] = reciever_email
    # file_path = root_path+code+'.jpg'

    # with open(file_path, "rb") as attachment:
    #     part = MIMEBase("application", "octet-stream")
    #     part.set_payload(attachment.read())

    # encoders.encode_base64(part)

    # part.add_header(
    #     "Content-Disposition",
    #     f"attachment; filename= {file_path}",
    # )

    # msg.attach(part)
    text = msg.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, reciever_email, text)
        print("succefully send the mail.")
