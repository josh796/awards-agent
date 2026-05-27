
import requests
from openai import OpenAI
import os
import smtplib
from email.mime.text import MIMEText

# 🔐 Load secrets from GitHub
OPENAI = os.environ["OPENAI_KEY"]
TAVILY = os.environ["TAVILY_KEY"]
EMAIL = os.environ["EMAIL_SENDER"]
PASSWORD = os.environ["EMAIL_PASSWORD"]

client = OpenAI(api_key=OPENAI)

# 🔍 Step 1: REAL web search
def search_awards():
    queries = [
        "fintech innovation awards Europe 2026 deadline",
        "proptech awards UK Europe 2026 application deadline",
        "lawtech innovation awards Europe 2026"
    ]

    results = []

    for q in queries:
        res = requests.post("https://api.tavily.com/search", json={
            "api_key": TAVILY,
            "query": q,
            "max_results": 5
        })

        data = res.json()

        for r in data.get("results", []):
            results.append(r["content"])

    return results


# 🤖 Step 2: Extract structured awards
def extract(data):
    text = " ".join(data)

    prompt = f"""
    Extract REAL fintech, proptech, and lawtech innovation awards.

    RULES:
    - Only FUTURE awards (next 12 months)
    - Minimum 10 awards
    - Include title, location, date, and link
    - Do NOT make up fake events

    Return CLEAN HTML:
    <ul>
      <li>
        <strong>Title:</strong> ...<br>
        <strong>Location:</strong> ...<br>
        <strong>Date:</strong> ...<br>
        <strong>Link:</strong> URL
      </li>
    </ul>

    TEXT:
    {text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


# 📧 Step 3: Send email
def send_email(content):

    msg = MIMEText(f"""
    <h2>Weekly Innovation Awards Digest</h2>
    <p>Automatically generated list of upcoming awards:</p>
    {content}
    """, "html")

    msg["Subject"] = "Weekly Awards Digest"
    msg["From"] = EMAIL
    msg["To"] = EMAIL

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL, PASSWORD)
    server.send_message(msg)
    server.quit()


# 🚀 Step 4: Main pipeline
def main():
    data = search_awards()
    result = extract(data)
    send_email(result)


# ▶️ Run automatically
if __name__ == "__main__":
    main()
