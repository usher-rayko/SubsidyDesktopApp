# Import the main imports
from main_imports import Screen, Clock
import requests
import json
import plyer
from includes.viewfarmers import ViewFarmers
from includes.list_not_found import *

class ManageRegisteredFarmers(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
    
    def list_available(type_request):
        get_request = requests.get(f'https://agriculturalsubsidy-default-rtdb.firebaseio.com/registeredFarmer/.json')
        # get_request = requests.get(f'https://agriculturalsubsidy-default-rtdb.firebaseio.com/registeredFarmer/.json?orderBy="RegisteredDate"')
        data = json.loads(get_request.content.decode())
        return data

    def on_pre_enter(self, *args):
        self.load_data()

    def load_data(self):
        farmers_data = self.list_available()
        self.ids.show_registered_farmers.clear_widgets()
        self.refresh_available_registered_farmers(farmers_data)
   
    def refresh_available_registered_farmers(self, farmers_data ):
        try :
            for Details, data in farmers_data .items():
                self.ids.show_registered_farmers.add_widget(ViewFarmers(
                    # regBy=data[f"Registered By: 'RegisteredBy'"],
                    regBy=data['RegisteredBy'],
                    details=data['Details'],
                    regdate=data['RegisteredDate'],
                    reload_data=self.load_data

                ))
                plyer.notification.notify(title="Success!", message = "The list is updated!")
        except :
            temp = list_not_found()
            self.ids.show_registered_farmers.add_widget(temp)

    def refresh_callback(self, *args):
        def refresh_callback(interval):
            self.ids.refresh_layout.refresh_done()

        self.load_data()
        Clock.schedule_once(refresh_callback, 1.5)