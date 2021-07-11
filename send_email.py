import os
import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "Scrapped Groups from Youtube"
body = "This is an email with attachment sent from Python"
sender_email = ENTER_SENDER_EMAIL
receiver_email = ENTER_RECEIVER_EMAIL
smtp_server = "smtp.gmail.com" #CONFIGURE SMTP
password = ENTER_PASSWORD


message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails

html = ""
files = ""


def send_email_with_files(html=html, files=files):

    part_html = MIMEText(html, "html")

    message.attach(part_html)

    for file in files:
        with open(file, "rb") as attachment:
            file_name = os.path.basename(file)
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            part.add_header("Content-Disposition", "attachment", filename=file_name)
            encoders.encode_base64(part)
            message.attach(part)

    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {file_name}",
    )

    message.attach(part)
    text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
