# Import the main imports
from main_imports import Screen, toast, json, requests
import plyer
import datetime
from tkinter import messagebox


class Push_Notification_Screen(Screen):
    def send_push_notification(self, title, description):
        self.url  = "https://agriculturalsubsidy-default-rtdb.firebaseio.com/pushnotifications/.json"
        date = datetime.datetime.now()

        if title.split() == [] or description.split() == []:
            messagebox.showerror('Failed','Please enter valid inputs!')

        else:
            push_notification_info = str({f'\"{date}\":{{"Title":\"{title}\","Description":\"{description}\","DateSent":\"{date.strftime("%Y-%m-%d %H:%M:%S")}\"}}'})
            push_notification_info = push_notification_info.replace(".","-")
            push_notification_info = push_notification_info.replace("\'","")
            send_to_database = json.loads(push_notification_info)
            print((send_to_database))
            requests.patch(url = self.url,json = send_to_database)
            # self.strng.get_screen('pushnotification').manager.current = 'pushnotification'
            messagebox.showinfo('Success', 'Push Notification has been sent!!!')
            plyer.notification.notify(title="Success!", message = "Push Notification has been sent!!!")
            toast("Push Notification has been sent!!!")


