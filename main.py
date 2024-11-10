#--[Start platform specific code]
from kivy.utils import platform
import os, sys
import os.path
os.environ['KIVY_GL_BACKEND'] = 'sdl2'
if platform != 'windows':
    from kivy.config import Config
    Config.set("graphics","width",800)
    Config.set("graphics","height",600)
    Config.set('graphics', 'multisamples', '0')  # sdl error
    Config.set('kivy', 'window_icon', 'assets/img/subsidy-icon.png')  # the icon in top-left of window
#--[End platform specific code]

# Import the main imports
from main_imports import MDApp, MDScreen, MDIconButton, ILeftBodyTouch, Builder, ScreenManager, Screen, toast, requests, MDTapTargetView
from kv import help_str
import pandas as pd
import kivymd.font_definitions
import matplotlib.pyplot as plt
from tkinter import messagebox

from create_user_account import AddUserAccountScreen
from send_email import Notification_Screen
from show_feedbacks import ShowFeedbackScreen
from show_registered_farmers import ManageRegisteredFarmers
from send_push_notifications import Push_Notification_Screen


class SubsidyAnalysis(Screen):
    pass

class MainScreen(Screen):
    pass

class WelcomeScreen(MDScreen):
    pass

class LoginScreen(Screen):
    pass

class TrackLocationScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class HelpScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(WelcomeScreen(name = 'welcomescreen'))
sm.add_widget(LoginScreen(name = 'loginscreen'))
sm.add_widget(LoginScreen(name = 'helpscreen'))
sm.add_widget(MainScreen(name = 'mainscreen'))
sm.add_widget(AddUserAccountScreen(name = 'useraccountscreen'))
sm.add_widget(Notification_Screen(name = 'alertscreen'))
sm.add_widget(TrackLocationScreen(name = 'tracklocationscreen'))
sm.add_widget(ManageRegisteredFarmers(name = 'registeredfarmersscreen'))
sm.add_widget(SettingsScreen(name = 'settingssscreen'))
sm.add_widget(Push_Notification_Screen(name = "pushnotification"))
sm.add_widget(ShowFeedbackScreen(name = "feedbackscreen"))


class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass

class SubsidyDesktopApp(MDApp):
    data = pd.read_csv('data.csv')
  
    df = pd.DataFrame(data)
  
    X = list(df.iloc[:, 0])
    Y = list(df.iloc[:, 1])
  
    # Plot the data using bar() method
    plt.bar(X, Y, color='b')
    plt.title("Subsidy Analysis over 11 Years")
    plt.xlabel("Years")
    plt.ylabel("Registered Farmers")
    plt.title('Subsidy Analysis Report')
  
    # API Key
    api_key = 'AIzaSyCMQG6gKrBNbwRRewW8yu6_K3FhPEXlzbo'

    def build(self):
        self.title = "SubsidyApp"
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.accent_palette = "Red"
        self.theme_cls.accent_hue = "700"
        self.theme_cls.theme_style = "Light"
        # Url + KV
        self.strng = Builder.load_string(help_str)
        self.skip_target_view = MDTapTargetView(
                                                widget=self.strng.get_screen('welcomescreen').ids.welcome_skip,
                                                title_text="PROCEED",widget_position="right_bottom",title_text_size="20sp",
                                                description_text="GO next",outer_radius='80dp',description_text_color=[1, 0, 0, 0]
                                                ,outer_circle_alpha = 0.40,target_radius='40dp')
        self.skip_target_view.start()
        self.url  = "https://agriculturalsubsidy-default-rtdb.firebaseio.com/.json"
        return self.strng
    
    def generate_report(self):
        try:
            self.strng.get_screen(plt.show())
        except:
            self.strng.get_screen('analysisscreen').manager.current = 'analysisscreen'
    
    # Method for admin logging in into system
    def sign_in(self):
        self.url  = "https://agriculturalsubsidy-default-rtdb.firebaseio.com/admin/.json"
        loginEmail = self.strng.get_screen('loginscreen').ids.login_email.text
        loginPassword = self.strng.get_screen('loginscreen').ids.login_password.text

        self.login_check = False
        supported_loginEmail = loginEmail.replace('.','-')
        supported_loginPassword = loginPassword.replace('.','-')
        request  = requests.get(self.url+'?api_key='+self.api_key)
        data = request.json()
        emails = set()
        for key, value in data.items():
            emails.add(key)
        if supported_loginEmail in emails and supported_loginPassword == data[supported_loginEmail]['Password']:
            self.username = data[supported_loginEmail]['Username']
            self.login_check = True
            messagebox.showinfo('Success', 'You have logged in Successfully!!')
            # toast("You have logged in successfully!")
            self.strng.get_screen('mainscreen').manager.current = 'mainscreen'
        else:
            toast("Sorry, Invalid Credentials!")
            messagebox.showerror('Failed','Please Enter Valid Credentials!')
    
    # After a successful login to show username
    def username_changer(self):
        if self.login_check:
            self.strng.get_screen('mainscreen').ids.username_info.text = f"Welcome {self.username}"

    def get_useraccounts(self):
        self.root.current = "useraccountscreen"
    
    def send_email_notification(self):
        self.root.current = "alertscreen"

    def go_back(self):
        self.root.current = "mainscreen"
    
    def login_screen(self):
        self.root.current = "loginscreen"
    
    def login_now(self):
        self.root.current = "mainscreen"

    def gotohelp(self):
        self.root.current = "helpscreen"

    def sign_out(self):
        self.root.current = "loginscreen"
        # Clear text fields
        self.strng.get_screen('loginscreen').ids.login_email.text = ''
        self.strng.get_screen('loginscreen').ids.login_password.text = ''


if __name__ == "__main__":
    # Start application from here.
    if not os.path.exists('subsidyreports.csv'):
	    sys.exit(0)
        
SubsidyDesktopApp().run() 


