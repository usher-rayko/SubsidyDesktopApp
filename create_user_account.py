# Import the main imports
from main_imports import Builder, Screen, toast, BooleanProperty, StringProperty, UrlRequest, Factory, certifi, Clock
from json import dumps
from kivy.properties import ObjectProperty
from tkinter import messagebox

class AddUserAccountScreen(Screen):
    # API Key
    # api_key = 'AIzaSyCMQG6gKrBNbwRRewW8yu6_K3FhPEXlzbo'
    # api_key = 'AIzaSyBmNh6B0SP-CeYEw2KLw_SMAF0Ef_tk5vQ'
    # AIzaSyBmNh6B0SP-CeYEw2KLw_SMAF0Ef_tk5vQ
    # AIzaSyCMQG6gKrBNbwRRewW8yu6_K3FhPEXlzbo
    api_key = 'AIzaSyCMQG6gKrBNbwRRewW8yu6_K3FhPEXlzbo'
    # api_key = StringProperty()

    # Firebase Authentication Credentials
    localId = ""
    idToken = ""
    emailId = ""

    # Properties used to send events to update some parts of the UI
    sign_up_msg = StringProperty()
    email_exists = BooleanProperty(False)
    email_not_found = BooleanProperty(False)
    require_email_verification = BooleanProperty(True)
    remember_user = BooleanProperty(True)
    debug = False

    def create_user_account(self, email, password):
        if self.debug:
            print("Attempting to create a new account: ", email, password)
        signup_url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key=" + self.api_key
        signup_payload = dumps(
            {"email": email, "password": password, "returnSecureToken": "true"})

        UrlRequest(signup_url, req_body=signup_payload,
                   on_success=self.successful_sign_up,
                   on_failure=self.sign_up_failure,
                   on_error=self.sign_up_error, ca_file=certifi.where())

    def successful_sign_up(self, request, result):
        if self.debug:
            print("Successfully signed up a user: ", result)
        self.localId = result['localId']
        self.idToken = result['idToken']
        self.emailId = result['email']

        if self.require_email_verification:
            self.send_verification_email(result['email'])
            messagebox.showinfo('Success', 'User Account created successfully!!!')
            toast("User Account created successfully")
        else:
            messagebox.showerror('Failed','Account failed to create!!!')
            toast("Account failed to create")

    def sign_up_failure(self, urlrequest, failure_data):
        """Displays an error message to the user if their attempt to log in was invalid."""
        self.email_exists = False  # Triggers hiding the sign in button
        msg = failure_data['error']['message'].replace("_", " ").capitalize()
        toast(msg)
        if msg == "Email already exists":
            self.email_exists = True
        if self.debug:
            print("Couldn't sign the user up: ", failure_data)

    def sign_up_error(self, *args):
        if self.debug:
            print("Sign up Error: ", args)

    # Sends a verification email after a user account is created. The email will contain a code that must be entered back into the app
    def send_verification_email(self, email):
        if self.debug:
            print("Attempting to send a email verification email to: ", email)
        verify_email_url = "https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key=" + self.api_key
        verify_email_data = dumps(
            {"idToken": self.idToken, "requestType": "VERIFY_EMAIL"})

        UrlRequest(verify_email_url, req_body=verify_email_data,
                   on_success=self.successful_verify_email_sent,
                   on_failure=self.unsuccessful_verify_email_sent,
                   on_error=self.unsuccessful_verify_email_sent,
                   ca_file=certifi.where())

    def unsuccessful_verify_email_sent(self, *args):
        messagebox.showerror('Couldnt send email verification email')
        toast("Couldn't send email verification email")

    def successful_verify_email_sent(self, *args):
        toast("A verification email has been sent. User must check their email.")
        messagebox.showinfo('Success', 'A verification email has been sent. User must check their email!!!')