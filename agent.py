import requests
import os
import smtplib
from email.mime.text import MIMEText

TAVILY = os.environ["TAVILY_KEY"]
EMAIL = os.environ["EMAIL_SENDER"]
PASSWORD = os.environ["EMAIL_PASSWORD"]


# 🔍 Categorised search
def search_awards():
    categories = {
        "Financial Services": "fintech banking awards Europe deadlines",
        "Business": "business innovation awards UK Europe",
        "Technology": "tech innovation awards Europe AI fintech proptech"
    }

    all_results = {}

    for category, query in categories.items():
        res = requests.post(
            "https://api.tavily.com/search",
            json={
                "api_key": TAVILY,
                "query": query,
                "max_results": 8
            }
        )

        data = res.json()
        all_results[category] = data.get("results", [])

    return all_results


# ✉️ Format like your example
def format_email(categorised_results):
    html = "<h2>Weekly Awards Digest</h2>"

    for category, results in categorised_results.items():
        html += f"<h3>{category}</h3><ul>"

        if not results:
            html += "<li>No results found</li>"

        for r in results:
            title = r.get("title", "No title")
            url = r.get("url", "#")

            html += f"""
            <li>
                <strong>{title}</strong> —
                <a href="{url}">View</a>
            </li>
            """

        html += "</ul>"

    return html


# 📧 Send email
def send_email(content):
    msg = MIMEText(content, "html")
    msg["Subject"] = "Weekly Awards Digest"
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
