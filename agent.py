import requests
import os
import smtplib
from email.mime.text import MIMEText

# ✅ Load secrets
TAVILY = os.environ["TAVILY_KEY"]
EMAIL = os.environ["EMAIL_SENDER"]
PASSWORD = os.environ["EMAIL_PASSWORD"]


# 🔍 Search awards using Tavily
def search_awards():
    queries = [
        "fintech awards Europe 2026",
        "proptech awards UK 2026",
        "lawtech awards Europe 2026"
    ]

    results = []

    for q in queries:
        res = requests.post(
            "https://api.tavily.com/search",
            json={
                "api_key": TAVILY,
                "query": q,
                "max_results": 5
            }
        )

        data = res.json()

        for r in data.get("results", []):
            results.append(r)

    return results


# ✉️ Clean HTML email formatting (FIXED)
def format_email(results):
    html = "<h2>Weekly Awards Digest</h2>"
    html += "<p>Latest fintech, proptech and lawtech awards:</p>"
    html += "<ul>"

    for r in results[:10]:
        title = r.get('title', 'No title')
        url = r.get('url', '#')
        content = r.get('content', '')[:120]

        html += f"""
        <li>
            <strong>{title}</strong><br>
            <a href="{url}">Visit Website</a><br>
            <small>{content}...</small>
        </li><br>
        """

    html += "</ul>"
    return html


# 📧 Send email
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


# 🚀 Main function
def main():
    results = search_awards()
    email_content = format_email(results)
    send_email(email_content)


if __name__ == "__main__":
    main()
