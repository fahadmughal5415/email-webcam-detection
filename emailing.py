import imghdr
from email.message import EmailMessage
import smtplib
import os


SENDER = "fahadmughal5415@gmail.com"
RECEIVER = "fahadmughal5415@gmail.com"
PASSWORD = os.getenv("PASSWORD")
HOST = "smtp.gmail.com"
PORT = 587
def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New Customer Showed Up!"
    email_message.set_content = "Hey, we just saw a new customer"

    with open(image_path, "rb") as file:
        content = file.read()

    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    try:
        gmail = smtplib.SMTP(HOST, PORT)
        gmail.ehlo()
        gmail.starttls()
        gmail.login(SENDER, PASSWORD)
        gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
        gmail.quit()
    except smtplib.SMTPAuthenticationError as e:
        print(f"Failed to send email: {e.smtp_code} - {e.smtp_error.decode()}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    send_email("images/1.jpg")