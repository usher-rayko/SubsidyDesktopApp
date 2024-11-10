# Import the main imports
from main_imports import Screen, Clock
from includes.feedbacks_not_found import *
import requests
import json
import plyer
from includes.viewfeedbacks import *

class ShowFeedbackScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
    
    def list_available(type_request):
        get_request = requests.get(f'https://agriculturalsubsidy-default-rtdb.firebaseio.com/feedback/.json')
        data = json.loads(get_request.content.decode())
        return data

    def on_pre_enter(self, *args):
        self.load_data()

    def load_data(self):
        feedback_data = self.list_available()
        self.ids.show_feedbacks.clear_widgets()
        self.refresh_feedbacks(feedback_data)
   
    def refresh_feedbacks(self, feedback_data):
        try :
            for Message, data in feedback_data .items():
                self.ids.show_feedbacks.add_widget(ViewFeedbacks(
                    from_user=data['SentFrom'],
                    message=data['Message'],
                    date_sent=data['DateSent'],
                    reload_data=self.load_data
                ))
                plyer.notification.notify(title="Success!", message = "Feedbacks are updated!")
        except :
            temp = no_alert_message()
            self.ids.show_feedbacks.add_widget(temp)

    def refresh_callback(self, *args):
        def refresh_callback(interval):
            self.ids.refresh_layout.refresh_done()

        self.load_data()
        Clock.schedule_once(refresh_callback, 1.5)