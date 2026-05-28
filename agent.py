import os
import smtplib
from email.mime.text import MIMEText

EMAIL = os.environ["EMAIL_SENDER"]
PASSWORD = os.environ["EMAIL_PASSWORD"]


def send_email():
    print("Starting email job...")

    html = """
    <html>
      <body>
        <h2>Weekly Awards Digest</h2>

        <h3>Financial Services</h3>
        <ul>
          <li>
            Europe FinTech Awards - 6 Mar -
            <a href="https://example.com">View</a>
          </li>
          <li>
            PayTech Awards - 13 Mar -
            <a href="https://example.com">View</a>
          </li>
        </ul>

        <h3>Business</h3>
        <ul>
          <li>
            UK Business Awards - 17 Apr -
            <a href="https://example.com">View</a>
          </li>
          <li>
            Startup Awards UK - 16 Mar -
            <a href="https://example.com">View</a>
          </li>
        </ul>

        <h3>Technology</h3>
        <ul>
          <li>
            Tech Excellence Awards - 22 Apr -
            <a href="https://example.com">View</a>
          </li>
        </ul>
      </body>
    </html>
    """

    msg = MIMEText(html, "html")
    msg["Subject"] = "Weekly Awards Digest"
    msg["From"] = EMAIL
    msg["To"] = EMAIL

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.send_message(msg)

        print("Email sent successfully.")

    except Exception as e:
        print(f"Email failed: {e}")
        raise


if __name__ == "__main__":
    send_email()
