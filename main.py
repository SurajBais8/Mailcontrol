from voice_recognition import recognize_speech
from text_to_speech import speak
from email_handler import read_emails, send_email, reply_to_email
from authentication import authenticate_google
import os

def voice_menu():
    speak("Welcome to your voice email system.")
    speak("Please say a command: Read my emails, Send an email, Reply to an email, or Exit.")

    while True:
        command = recognize_speech()

        if "read" in command:
            speak("Reading your latest emails.")
            read_emails()

        elif "send" in command:
            speak("Starting the email sending process.")
            send_email()

        elif "reply" in command:
            speak("Replying to your latest email.")
            reply_to_email()

        elif "exit" in command:
            speak("Exiting the application. Goodbye!")
            break

        else:
            speak("Sorry, I didn't understand. Please say Read my emails, Send an email, Reply to an email, or Exit.")

if __name__ == "__main__":
    credentials = authenticate_google()
    voice_menu()
