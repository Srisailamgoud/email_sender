import smtplib

def sendEmail():
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        # Use your app password here
        server.login("your_email", "yourpassword")
        sender_email="your_email"
        recipients=[ "Reicipents_emails"]
        subject="Test Mail"
        body="This is testing mail to multiple accounts"
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(sender_email,recipients, message)
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError as e:
        print("Failed to authenticate:", e)
    except Exception as e:
        print("An error occurred:", e)
    finally:
        server.quit()

sendEmail()