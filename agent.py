import os
import smtplib
from email.mime.text import MIMEText

# ✅ Load email credentials
EMAIL = os.environ["EMAIL_SENDER"]
PASSWORD = os.environ["EMAIL_PASSWORD"]

def send_email():
    print("✅ RUNNING WORKING VERSION ✅")

    html = """
    <h2>Weekly Awards Digest</h2>

    <h3>Financial Services</h3>
    <ul>
        <li>Europe FinTech Awards – 6 Mar – github.com</li>
        <li>PayTech Awards – 13 Mar – github.com</li>
    </ul>

    <h3>Business</h3>
    <ul>
        <li>UK Business Awards – 17 Apr – github.com</li>
        <li>Startup Awards UK – 16 Mar – github.com</li>
    </ul>
    """

    msg = MIMEText(html, "html")
    msg["Subject"] = "Awards Digest"
    msg["From"] = EMAIL
    msg["To"] = EMAIL

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL, PASSWORD)
    server.send_message(msg)
    server.quit()
    
if __name__ == "__main__":
    send_email()


