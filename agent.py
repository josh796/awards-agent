
import osimport osText

# ✅ Load credentials from GitHub Secrets
EMAIL = os.environ["EMAIL_SENDER"]
PASSWORD = os.environ["EMAIL_PASSWORD"]


def send_email():
    # ✅ Debug line to confirm correct file is running
    print("✅ THIS IS THE FILE BEING EXECUTED ✅")

    # ✅ FULL VALID HTML (no broken tags, no escaped characters)
    html = """
    <html>
        <body>
            <h2>Weekly Awards Digest</h2>

            <h3>Financial Services</h3>
            <ul>
                <li>Europe FinTech Awards – 6 Mar – <a href="https://europefintechawards.com">Visit</a></li>
                <li>PayTech Awards – 13 Mar – <a href="https://paytechawards.com">Visit</a></li>
                <li>Risk Technology Awards – 6 Mar – <a href="https://risktechawards.com">Visit</a></li>
            </ul>

            <h3>Business</h3>
            <ul>
                <li>UK Business Awards – 17 Apr – <a href="https://ukbusinessawards.co.uk">Visit</a></li>
                <li>Startup Awards UK – 16 Mar – <a href="https://startupawards.uk">Visit</a></li>
                <li>British Business Awards – 13 Mar – <a href="https://britishbusinessawards.co.uk">Visit</a></li>
            </ul>

            <h3>Technology</h3>
            <ul>
                <li>National AI Awards – 20 Mar – <a href="https://nationalaiawards.com">Visit</a></li>
                <li>Cloud Security Awards – 20 Mar – <a href="https://cloudsecurityawards.com">Visit</a></li>
                <li>UK Tech Awards – 30 Apr – <a href="https://techawards.uk">Visit</a></li>
            </ul>

        </body>
    </html>
    """

    # ✅ Print HTML so you can see it in GitHub logs
    print("-------- EMAIL CONTENT --------")
    print(html)
    print("------------------------------")

    # ✅ Create email
    msg = MIMEText(html, "html")
    msg["Subject"] = "Awards Digest"
    msg["From"] = EMAIL
    msg["To"] = EMAIL

    # ✅ Send email
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL, PASSWORD)
    server.send_message(msg)
    server.quit()


if __name__ == "__main__":
    send_email()

import smtplib
