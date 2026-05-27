import requests
import os
import smtplib
from email.mime.text import MIMEText

TAVILY = os.environ["TAVILY_KEY"]
EMAIL = os.environ["EMAIL_SENDER"]
PASSWORD = os.environ["EMAIL_PASSWORD"]


def search_awards():
    query = "fintech awards Europe business innovation awards deadlines"

    res = requests.post(
        "https://api.tavily.com/search",
        json={
            "api_key": TAVILY,
            "query": query,
            "max_results": 10
        }
    )

    data = res.json()

    # ✅ DEBUG: return raw results
    return data.get("results", [])


def format_email(results):
    html = "<h2>Weekly Awards Digest</h2>"
    html += "<p>Debug view of results:</p><ul>"

    if not results:
        html += "<li>❌ No data returned from Tavily</li>"

    for r in results:
        html += f"<li>{str(r)}</li><br>"

    html += "</ul>"
    return html


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
    results = search_awards()
    send_email(format_email(results))


if __name__ == "__main__":
    main()
