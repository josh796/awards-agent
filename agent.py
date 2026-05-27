import requests
import os
import smtplib
from email.mime.text import MIMEText

TAVILY = os.environ["TAVILY_KEY"]
EMAIL = os.environ["EMAIL_SENDER"]
PASSWORD = os.environ["EMAIL_PASSWORD"]


def search_awards():
    queries = [
        "fintech awards Europe 2026 deadlines",
        "business innovation awards UK Europe",
        "technology innovation awards Europe"
    ]

    results = []

    for q in queries:
        res = requests.post(
            "https://api.tavily.com/search",
            json={
                "api_key": TAVILY,
                "query": q,
                "max_results": 10
            }
        )

        data = res.json()

        for r in data.get("results", []):
            results.append(r)

    return results


def format_email(results):
    html = "<h2>Weekly Awards Digest</h2>"
    html += "<p>Latest awards:</p><ul>"

    if not results:
        html += "<li>No awards found this run (check API later)</li>"

    for r in results:
        title = r.get("title", "Unknown award")
        url = r.get("url", "#")

        html += f"""
        <li>
            <strong>{title}</strong><br>
            <a href="{url}">Visit Website</a>
        </li><br>
        """

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
    email_content = format_email(results)
    send_email(email_content)


if __name__ == "__main__":
    main()
``
