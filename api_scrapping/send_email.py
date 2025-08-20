import smtplib
from email.message import EmailMessage


EMAIL_ADDRESS = "automationtasks12@gmail.com"
PASSWORD = "jdza recz sjng fzqp"
msg = EmailMessage()
msg["Subject"] = "Jobs Updates from Remote ok"
msg["From"] = EMAIL_ADDRESS
msg["To"] = ", ".join(["freelancer.task1@gmail.com"])
msg["Cc"] = ", ".join(["zainyyy70@gmail.com"])
msg["Bcc"] = ", ".join(["am2202855@gmail.com"])
msg.set_content(
"""
Assalam o Alaikum!
Here is are the jobs updates after completing web scrapping from remoteok.com.
The attachments are also given below.
"""
)
attachment_path = "Jobs_Data.xlsx"

with open(attachment_path, "rb") as file:
    msg.add_attachment(file.read(),
                       maintype="application",
                       subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                       filename="Jobs_Data.xlsx")
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ADDRESS, PASSWORD)
        recipients = (
                msg['To'].split(", ") +
                msg.get('Cc', '').split(", ") +
                msg.get('Bcc', '').split(", ")
        )
        server.sendmail(EMAIL_ADDRESS, recipients, msg.as_string())
        print("Emails sent successfully.")
except Exception as e:
    print(f"failed to send email: {e}")
