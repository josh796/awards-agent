import os
import smtplib
from email.mime.text import MIMEText

EMAIL = os.environ["EMAIL_SENDER"]
PASSWORD = os.environ["EMAIL_PASSWORD"]


# ✅ Structured award data (reliable, no empty emails)
def get_awards():
    return {
        "Financial Services": [
            ("Europe FinTech Awards", "6 Mar", "https://europefintechawards.com"),
            ("PayTech Awards", "13 Mar", "https://paytechawards.com"),
            ("Risk Technology Awards", "6 Mar", "https://risktechawards.com"),
        ],
        "Business": [
            ("UK Business Awards", "17 Apr", "https://ukbusinessawards.co.uk"),
            ("Startup Awards UK", "16 Mar", "https://startupawards.uk"),
            ("The British Business Awards", "13 Mar", "https://britishbusinessawards.co.uk"),
        ],
        "Technology": [
            ("National AI Awards", "20 Mar", "https://nationalaiawards.com"),
            ("Tech Awards UK", "30 Apr", "https://techawards.uk"),
            ("Cloud Security Awards", "20 Mar", "https://cloudsecurityawards.com"),
        ]
    }


# ✅ Format email EXACTLY like your example list
def format_email(data):
    html = "<h2>Weekly Awards Digest</h2>"

    for category, awards in data.items():
        html += f"<h3>{category}</h3><ul>"

        for name, date, link in awards:
            html += f"""
            <li>
                {name} – {date} –
                <a href="{link}">Visit</a>
            </li>
            """

        html += "</ul>"

    return html


# ✅ Send email
def send_email(content):
    msg = MIMEText(content, "html")
    msg["Subject"] = "Awards Digest"
    msg["From"] = EMAIL
    msg["To"] = EMAIL

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL, PASSWORD)
    server.send_message(msg)
    server.quit()


def main():
    data = get_awards()
    email_content = format_email(data)
    send_email(email_content)


if __name__ == "__main__":
    main()
