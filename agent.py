import os
import smtplib
import requests
from email.mime.text import MIMEText
from datetime import datetime

EMAIL = os.environ["EMAIL_SENDER"]
PASSWORD = os.environ["EMAIL_PASSWORD"]

TAVILY_KEY = os.environ.get("TAVILY_KEY")


def fetch_awards():
    query = "innovation awards fintech business technology awards June July 2026 deadlines"

    response = requests.post(
        "https://api.tavily.com/search",
        json={
            "api_key": TAVILY_KEY,
            "query": query,
            "max_results": 15
    
def fetch_awards():
    query = "..."

    response = requests.post(...)
    data = response.json()
    raw_results = data.get("results", [])

    awards = []

    for r in raw_results:
        title = r.get("title", "")
        url = r.get("url", "")
        content = r.get("content", "")

        if content and any(month in content.lower() for month in ["june", "july", "aug", "2026", "deadline"]):
            awards.append({
                "title": title,
                "url": url
            })

    return awards[:15]   ✅ ← IMPORTANT: inside function



def format_email(awards):
    html = "<h2>Weekly Awards Digest</h2>"
    html += "<h3>Financial Services & Innovation Awards</h3><ul>"

    if not awards:
        html += "<li>No relevant future awards found this week</li>"

  
for a in awards:
    html += f"<li>{a['title']} - {a['url']}</li>"

   

    html += "</ul>"
    return html
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
    print("✅ RUNNING LIVE AWARDS FETCH ✅")

    awards = fetch_awards()
    email_content = format_email(awards)
    send_email(email_content)


if __name__ == "__main__":
    main()



