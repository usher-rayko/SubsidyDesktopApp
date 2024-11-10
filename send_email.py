from main_imports import Screen
import smtplib
from email.message import EmailMessage
from tkinter import messagebox

class Notification_Screen(Screen):
 def send_email(self, receiver, subject, msg_body):
        sender = "optichemfertilizersubsidy@gmail.com"
        password = "easas2021"

        msg = EmailMessage()
        msg['from'] = sender
        msg['to'] = receiver
        msg['subject'] = subject
        msg.set_content(msg_body)
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(sender, password)
                smtp.send_message(msg)
                messagebox.showinfo('Success', 'Email Sent!')
        except Exception as ep:
            messagebox.showerror('Failed','Something is Incorrect or Try Turning ON Less Secure Apps!')
            