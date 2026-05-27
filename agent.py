
import requests
import os
import smtplib
from email.mime.text import MIMEText

# ✅ Load secrets
TAVILY = os.environ["TAVILY_KEY"]
EMAIL = os.environ["EMAIL_SENDER"]
PASSWORD = os.environ["EMAIL_PASSWORD"]


# 🔍 Search for awards using Tavily (free)
def search_awards():
    queries = [
        "fintech awards Europe innovation 2026",
        "proptech awards UK Europe 2026 innovation",
        "lawtech awards Europe 2026 innovation"
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


# ✉️ Format email nicely
def format_email(results):
    html = """
    <h2>Weekly Innovation Awards Digest</h2>
    <p>Latest fintech, proptech, and lawtech awards:</p>
    <ul>
    """

    for r in results[:12]:
        html += f"""
        <li>
            <strong>{r.get('title', 'No title')}</strong><br>
            <a href="{r.get('url', '#')}">Visit Website</a><br>
            <small>{r.get('content', '')[:150]}...</small>
        </li><br>
        """

    html += "</ul>"
    return html


# 📧 Send email via Gmail
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


# 🚀 Main function
def main():
    results = search_awards()
    email_content = format_email(results)
    send_email(email_content)


if __name__ == "__main__":
    main()
``
