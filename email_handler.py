import smtplib
import imaplib
import email
from text_to_speech import speak
from voice_recognition import recognize_speech

def read_emails():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login("your_email@gmail.com", "your_password")  # Use OAuth method for security
    mail.select("inbox")

    _, message_numbers = mail.search(None, "ALL")
    messages = message_numbers[0].split()

    latest_email_id = messages[-1]
    _, msg_data = mail.fetch(latest_email_id, "(RFC822)")

    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            subject = msg["subject"]
            speak("Your latest email subject is: " + subject)

    mail.logout()

def send_email():
    speak("Please say the recipient's email address.")
    recipient = recognize_speech().replace(" ", "").lower()

    speak("What is the subject?")
    subject = recognize_speech()

    speak("What is the message?")
    message = recognize_speech()

    sender_email = "your_email@gmail.com"
    password = "your_password"  # Use OAuth instead of storing passwords

    msg = f"Subject: {subject}\n\n{message}"
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient, msg)

    speak("Email has been sent.")

def reply_to_email():
    speak("Replying to the latest email.")

    sender_email = "your_email@gmail.com"
    password = "your_password"  # Use OAuth2 authentication

    speak("What is your reply message?")
    reply_message = recognize_speech()

    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(sender_email, password)
    mail.select("inbox")

    _, message_numbers = mail.search(None, "ALL")
    messages = message_numbers[0].split()

    latest_email_id = messages[-1]
    _, msg_data = mail.fetch(latest_email_id, "(RFC822)")

    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            sender = msg["From"]

    msg = f"Subject: Re: {msg['Subject']}\n\n{reply_message}"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, sender, msg)

    speak("Reply has been sent.")
