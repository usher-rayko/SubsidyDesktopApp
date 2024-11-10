help_str = '''
#:import MapSource mapview.MapSource
#:import md_icons kivymd.icon_definitions.md_icons
ScreenManager:   
    WelcomeScreen:    
    LoginScreen: 
    HelpScreen:
    MainScreen:
    AddUserAccountScreen:
    TrackLocationScreen:
    Notification_Screen:
    SubsidyAnalysis:
    ShowFeedbackScreen:
    ManageRegisteredFarmers
    SettingsScreen:
    Push_Notification_Screen
        
<WelcomeScreen>:
    name:'welcomescreen'
    FitImage:
        source: "assets/img/malawi-3.jpg"
    Image:
        source: "assets/img/logo.png"
        pos_hint: {"center_x": .5, "center_y": .80}
        size_hint_y: .11
        size_hint_x: .86
    MDLabel:
        pos_hint: {"center_x": .5, "center_y": .65}
        size_hint_y: .11
        size_hint_x: .86
        halign: "center"
        font_name: "Roboto-BoldItalic.ttf"
        text: "SubsidyApp"
        font_size: 52
        bold: True
        # theme_text_color:'Custom'
        # text_color:1,1,1,1
    MDFloatingActionButton:
        id : welcome_skip
        icon: "arrow-right"
        md_bg_color:app.theme_cls.accent_color
        pos_hint: {'center_x':0.5,'center_y':0.25}
        user_font_size: "50sp"
        halign: "center"
        on_press: app.login_screen()

<LoginScreen>:
    name:'loginscreen'
    id: loginscreen
    FitImage:
        source: "assets/img/malawi-3.jpg"
    MDCard:
        size_hint: .4, .8
        pos_hint: {"center_x": .5, "center_y": .5}
        md_bg_color: 1, 1, 1, 0.8
        FloatLayout:
            MDLabel:
                text: "Welcome Admin!"
                font_name: 'fonts/materialdesignicons-webfont.ttf'
                halign: "center"
                pos_hint: {"center_x": .5, "center_y": .85}
                size_hint_x: .86
                font_style: "H4"
                bold: True
            MDLabel:
                text: "Please provide valid credentials to login."
                halign: "center"
                pos_hint: {"center_x": .5, "center_y": .77}
                size_hint_x: .86
                font_style: "Subtitle2"
            MDTextField:
                id:login_email
                hint_text: 'Enter your Email'
                helper_text:'Required'
                helper_text_mode:  'on_error'
                required: True
                size_hint_x: .86
                pos_hint: {"center_x": .5, "top": .7}
                theme_text_color:'Custom'
                text_color:0.3,0.3,0.3,1
            MDTextField:
                id:login_password
                hint_text: 'Enter your Password'
                helper_text:'Required'
                helper_text_mode:  'on_error'
                required: True
                size_hint_x: .86
                password: True
                pos_hint: {"center_x": .5, "top": .6}
                md_bg_color:0.3,0.3,0.3,1

            Button:
                id: login_btn
                text:'LOGIN'
                size_hint: .86 ,.062
                color: 1, 1, 1, 1 
                bold: True
                pos_hint: {"center_x": .5, "top": .48}
                on_press:
                    app.sign_in()
                    app.username_changer() 
                
            Button:
                text:'HELP!'
                size_hint: .86 ,.062
                color: 1, 1, 1, 1 
                bold: True
                pos_hint: {"center_x": .5, "top": .39}
                # on_press: app.gotohelp()
                on_press: app.login_now()
<HelpScreen>:
    name: 'helpscreen'
    MDBoxLayout:
        orientation:'vertical'
        MDToolbar:
            title: "HELP"
            left_action_items: [['arrow-left', lambda x: app.sign_out()]] 
            md_bg_color: 1, 1, 0, 0

        BoxLayout:
            orientation: 'vertical'
            MDLabel:
                text: "HOW TO USE THIS SYSTEM!"
                halign: "center"
                bold: True
            MDLabel:
                text: "1. Provide valid details to login into the system."
                pos_hint: {"center_x": .5, "top": .9}
            MDLabel:
                text: "2. After a success login, on the dashboard -> click User Accounts to create employee user account."
                pos_hint: {"center_x": .5, "top": .8}
            MDLabel:
                text: "3. To send email, click on Email Notification."
                pos_hint: {"center_x": .5, "top": .7}
            MDLabel:
                text: "4. To track location, click on Track Location."
                pos_hint: {"center_x": .5, "top": .6}
            MDLabel:
                text: "5. To view registered farmers, click on View Farmers."
                pos_hint: {"center_x": .5, "top": .5}
            MDLabel:
                text: "6. To view subsidy reports and analysis, click on Subsidy Analysis."
                pos_hint: {"center_x": .5, "top": .4}
<MainScreen>:
    name: 'mainscreen'
    md_bg_color:0,0,0,0.9
    ActionBar:
        pos_hint: {'top': 1.0}
        height: '37dp'
        ActionView:
            ActionPrevious:
                title: ''
                size_hint_x: None
                with_previous: False
                app_icon_width: 0.001
                width: 0

            ActionButton:
                text: 'Home'
                on_release: root.manager.current = 'mainscreen'
                md_bg_color: app.theme_cls.primary_color

            ActionButton:
                text: 'Manage Accounts'
                on_release: root.manager.current = 'useraccountscreen'

            ActionButton:
                text: 'Registered Farmers'
                on_release: root.manager.current = 'registeredfarmersscreen'

            ActionButton:
                text: 'Subsidy Analysis'
                on_release: root.manager.current = 'analysisscreen'

            ActionButton:
                text: 'Settings'
                on_release: root.manager.current = 'settingsscreen'

            ActionButton:
                text: 'Logout'
                on_release: app.sign_out()
    BoxLayout:
        Screen:
            do_default_tab: False
            size_hint_y: None
            height: root.height - dp(37)
            BoxLayout:
                
                ScrollView:
                    bar_width:0
                    MDBoxLayout:
                        orientation:'vertical'
                        adaptive_height:True
                        spacing:'12dp'
                        padding:'12dp'
                        # md_bg_color:0.3,0.3,0.3,1
                        MDLabel:
                            #id:username_info
                            #text:'Hello Main'
                            md_bg_color:0.2,0.2,0.2,1
                            specific_text_color:0,.6,.8,1
                            text:'DASHBOARD'
                            font_style:"Subtitle2"
                        MDGridLayout:
                            cols:1
                            size_hint_y:None
                            MDCard:
                                orientation: 'vertical'
                                size_hint_y: None
                                height: self.minimum_height
                                # md_bg_color: .9,.9,.9,.2
                                specific_text_color:0,.6,.8,1
                                TwoLineIconListItem:
                                    id:username_info
                                    text:'Welcome admin'
                                    secondary_text: "Click to view your account"
                                    IconLeftSampleWidget:
                                        icon: "assets/img/admin.png"
                                    Widget:
                                TwoLineIconListItem:
                                    text: "View Farmers"
                                    secondary_text: "7896 farmers registered"
                                    on_release: root.manager.current = 'registeredfarmersscreen'
                                    IconLeftSampleWidget:
                                        icon: "assets/img/logview.png"
                                Widget
                       
                            MDCard:
                                orientation: 'vertical'
                                size_hint_y: None
                                height: self.minimum_height
                                specific_text_color:0,.6,.8,1
                                TwoLineIconListItem:
                                    text: "Send Notifications"
                                    secondary_text: "Send push notifications to all users"
                                    on_release: root.manager.current = 'pushnotification'
                                    IconLeftSampleWidget:
                                        icon: "assets/img/bell.png"
                        MDLabel:
                        MDLabel:
                        MDLabel:
                        MDLabel:
                        MDLabel:
                        MDLabel:
                        MDLabel:
                        MDLabel:
                        MDLabel:
                        MDBoxLayout:
                            size_hint_y:None
                            height:'150dp'
                            spacing:'5dp'
                            MDCard: 
                                ripple_behavior:True
                                orientation:'vertical'
                                padding:'5dp'
                                md_bg_color:0.3,1,0.3,.3
                                adaptive_height:True
                                on_press: app.get_useraccounts()
                                MDIconButton:
                                    pos_hint:{'center_x':.5}
                                    icon: "assets/img/Add_User_Male_48px.png"
                                    on_press: app.get_useraccounts()
                                    color:1,1,1,1
                                MDLabel:
                                    text:'User Accounts'
                                    adaptive_height:True
                                    halign:'center'
                                    theme_text_color:'Custom'
                                    text_color:1,1,1,1
                                    bold: True
                                MDLabel:
                                    text:'Manage user accounts'
                                    adaptive_height:True
                                    font_style:'Caption'
                                    halign:'center'
                                    theme_text_color:'Custom'
                                    text_color:1,1,1,1
                                    bold: True
                            MDCard:
                                ripple_behavior:True
                                orientation:'vertical'
                                padding:'5dp'
                                md_bg_color:1,.6,0,.8
                                adaptive_height:True
                                on_press:
                                    root.manager.current = 'alertscreen'
                                    root.manager.transition.direction = 'left'
                                MDIconButton:
                                    pos_hint:{'center_x':.5}
                                    icon: "assets/img/Gmail_48px.png"
                                    on_press:
                                        root.manager.current = 'alertscreen'
                                        root.manager.transition.direction = 'left'
                                MDLabel:
                                    theme_text_color:'Custom'
                                    text_color:1,1,1,1
                                    bold: True
                                    text:'Email Notifications'
                                    adaptive_height:True
                                    halign:'center'
                                MDLabel:
                                    theme_text_color:'Custom'
                                    text_color:1,1,1,1
                                    bold: True
                                    text:'Send email notifications'
                                    adaptive_height:True
                                    font_style:'Caption'
                                    halign:'center'
                            MDCard:
                                ripple_behavior:True
                                orientation:'vertical'
                                padding:'5dp'
                                md_bg_color:1,0,0,.4
                                adaptive_height:True
                                on_press:
                                    root.manager.current = 'feedbackscreen'
                                    root.manager.transition.direction = 'left'
                                MDIconButton:
                                    pos_hint:{'center_x':.5}
                                    icon: "assets/img/Feedback_48px.png"
                                    on_press:
                                        root.manager.current = 'feedbackscreen'
                                        root.manager.transition.direction = 'left'
                                MDLabel:
                                    theme_text_color:'Custom'
                                    text_color:1,1,1,1
                                    bold: True
                                    text:'Received Feedbacks'
                                    adaptive_height:True
                                    halign:'center'
                                MDLabel:
                                    theme_text_color:'Custom'
                                    text_color:1,1,1,1
                                    text:'View Received feedback'
                                    adaptive_height:True
                                    font_style:'Caption'
                                    halign:'center'
                                    bold: True
                            MDCard:
                                ripple_behavior:True
                                orientation:'vertical'
                                padding:'5dp'
                                md_bg_color:0,.6,.8,1
                                adaptive_height:True
                                on_press:
                                    root.manager.current = 'tracklocationscreen'
                                    root.manager.transition.direction = 'left'
                                MDIconButton:
                                    pos_hint:{'center_x':.5}
                                    icon: "assets/img/Marker_48px.png"
                                    on_press:
                                        root.manager.current = 'tracklocationscreen'
                                        root.manager.transition.direction = 'left'
                                MDLabel:
                                    text:'Track Locations'
                                    adaptive_height:True
                                    halign:'center'
                                    theme_text_color:'Custom'
                                    text_color:1,1,1,1
                                    bold: True
                                MDLabel:
                                    text:'View locations'
                                    adaptive_height:True
                                    font_style:'Caption'
                                    halign:'center'
                                    theme_text_color:'Custom'
                                    text_color:1,1,1,1
                                    bold: True
                        MDBoxLayout:
                            size_hint_y:None
                            spacing:'5dp'
                            adaptive_height:True
                            MDCard:
                                ripple_behavior:True
                                orientation:'vertical'
                                padding:'5dp'
                                adaptive_height:True
                                MDLabel:
                                    text: "Malawian Fertilizer Subsidy Statistics"
                                    bold: True
                                Widget:
                                MDLabel:
                                    text: "Registered Farmers           60%"
                                MDProgressBar:
                                    value: 60
                                    color: 0,.6,.8,1
                                Widget:
                                MDLabel:
                                    text: "Purchased Inputs          57%"
                                MDProgressBar:
                                    value: 57
                                    color: 0,.6,.8,1
                                Widget:
                                MDLabel:
                                    text: "Fertilizer Available           90%"
                                MDProgressBar:
                                    value: 90
                                    color: 0,.6,.8,1
                                Widget:
                            MDCard:
                                size_hint_y:None
                                height:'300dp'
                                ripple_behavior:True
                                orientation:'vertical'
                                padding:'5dp'
                                adaptive_height:True
                                MDBoxLayout:
                                    size_hint_y:None
                                    height:'180dp'
                                    canvas.after:
                                        Color:
                                            rgba:.2,.2,.2,.6
                                        Line:
                                            width:dp(5)
                                            circle:(self.center_x,self.parent.center_y+dp(35),min(self.width,self.height)/2)
                                        Color:
                                            rgba:.4,.77,.6,1
                                        Line:
                                            width:dp(8)
                                            circle:(self.center_x,self.parent.center_y+dp(35),min(self.width,self.height)/2,0,120)

                                        Color:
                                            rgba:.2,.2,.2,.6
                                        Line:
                                            width:dp(5)
                                            circle:(self.center_x,self.parent.center_y+dp(35),min(self.width,self.height)/3.5,)

                                        Color:
                                            rgba:.77,.8,.4,1
                                        Line:
                                            width:dp(8)
                                            circle:(self.center_x,self.parent.center_y+dp(35),min(self.width,self.height)/3.5,0,34)
                                    MDBoxLayout:
                                        adaptive_height:True
                                        padding:'10dp'
                                        orientation:'vertical'
                                    MDLabel:
                                        markup:True
                                        adaptive_height:True
                                        pos_hint: {"center_y": .3}
                                        text:f"[font=Icons][color=#66C499]{md_icons['card']}[/color][/font]Feedbacks Received (40%)"
                                    Widget:
                                    MDLabel:
                                        markup:True
                                        adaptive_height:True
                                        pos_hint: {"center_y": .3}
                                        text:f"[font=Icons][color=#C4CC66]{md_icons['card']}[/color][/font]Sent Notifications (9%)"
                    
                        MDBoxLayout:
                            size_hint_y:None
                            spacing:'5dp'
                            adaptive_height:True    
                            MDCard:
                                size_hint: 1, 1
                                radius: 10, 10
                                elevation: -1
                                padding: 15
                                BoxLayout:
                                    size_hint_x: .7
                                    orientation: 'vertical'
                                    Label:
                                    MDLabel:
                                        text: "Fertilizer Sales Since 2000 Summary"
                                        bold: True
                                    MDLabel:
                                        text: "32.1 Billion Kwacha Made"
                                        bold: True
                                        color: 0,0,1,1
                                    MDLabel:
                                        markup: True
                                        text: "[b]+5.7%[/b] Profit"
                                    MDLabel:
                                        markup: True
                                        text: "[b]+2.92%[/b] Loss"
                                    MDLabel:
                                        markup: True
                                        text: "[b]+0.109%[/b] Other"
                                    Label:
                                BoxLayout:
                                    size_hint_x: .3
                                    MDIconButton:
                                        icon: "finance"
                                        user_font_size: '50sp'
                                        theme_text_color: "Custom"
                                        text_color: 0,0,1,1
                                        pos_hint: {'y': .2}

                            MDCard:
                                size_hint_y:None
                                height:'255dp'
                                padding:'15dp'
                                spacing:'10dp'
                                orientation:'vertical'
                                MDBoxLayout:
                                    spacing:'15dp'
                                    Image:
                                        source:'assets/img/bell.png'
                                MDBoxLayout:
                                    orientation:'vertical'
                                    spacing:'10dp'
                                    MDLabel:
                                        text:'Send notifications to users'
                                        adaptive_height:True
                                        font_style:'H6'
                                        halign:'center'
                                    MDLabel:
                                        text:'All users will be notified'
                                        font_style:'Caption'
                                        adaptive_height:True
                                        halign:'center'
                                    MDRectangleFlatButton:
                                        markup:True
                                        pos_hint:{'center_x':.5,'center_y':.5}
                                        text:f"Send Notifications[font=Icons]{md_icons['arrow-right']}[/font]"
                                        on_release: root.manager.current = 'pushnotification'

<CustomImageTile@SmartTileWithLabel>:
    size_hint_y:None
    size_hint_x:None
    height:'200dp'
    width:'320dp'
<GridCard@MDCard>:
    ripple_behavior:True
    orientation:'vertical'
    image:''
    folder_size:''
    text:''
    items_count:""
    padding:'5dp'
    spacing:'5dp'
    size_hint_y:None
    height:'280dp'
    Image:
        source:root.image
    MDBoxLayout:
        orientation:'vertical'
        adaptive_height:True
        MDLabel:
            text:root.folder_size
            adaptive_height:True
            halign:'center'
            font_style:'Caption'
            bold: True
            # color: 0,0,1,1
            font_size: 20
        MDLabel:
            text:root.text
            adaptive_height:True
            halign:'center'
        MDLabel:
            halign:"center"
            text:root.items_count 

<AddUserAccountScreen>:
    name: "useraccountscreen"
    ActionBar:
        pos_hint: {'top': 1.0}
        height: '37dp'
        ActionView:
            ActionPrevious:
                title: ''
                size_hint_x: None
                with_previous: False
                app_icon_width: 0.001
                width: 0

            ActionButton:
                text: 'Home'
                on_release: root.manager.current = 'mainscreen'
                md_bg_color: app.theme_cls.primary_color

            ActionButton:
                text: 'Manage Accounts'
                on_release: root.manager.current = 'useraccountscreen'

            ActionButton:
                text: 'Registered Farmers'
                on_release: root.manager.current = 'registeredfarmersscreen'

            ActionButton:
                text: 'Subsidy Analysis'
                on_release: root.manager.current = 'analysisscreen'

            ActionButton:
                text: 'Settings'
                on_release: root.manager.current = 'settingsscreen'

            ActionButton:
                text: 'Logout'
                on_release: app.sign_out()
    BoxLayout:
        Screen:
            do_default_tab: False
            size_hint_y: None
            height: root.height - dp(37)
            FloatLayout:
                MDLabel:
                    text: "Create User Account"
                    font_style: "H2"
                    halign: "center"
                    bold: True
                    font_name: "Roboto-BoldItalic.ttf"
                    pos_hint: {"center_y": .8}
                MDLabel:
                    text: "Provide valid email and password to create user account"
                    font_style: "H6"
                    halign: "center"
                    bold: True
                    pos_hint: {"center_y": .7}
                
                MDTextFieldCustom:
                    id: email
                    pos_hint: {"center_x": .5, "center_y": .6}
                    hint_text: "Enter User Email"
                    size_hint: .5, .05
                    icon_left: 'email'
                    on_text_validate: password.focus = True

                MDTextFieldCustom:
                    id: password
                    pos_hint: {"center_x": .5, "center_y": .5}
                    hint_text: "Enter User Password"
                    password: True
                    size_hint: .5, .05
                    icon_left: 'key-variant'

                Button:
                    id: sign_up_button
                    text: "Create User Account"
                    size_hint: .53, .05
                    pos_hint: {"center_x": .5, "center_y": .4}
                    color: 1, 1, 1, 1 
                    md_bg_color:app.theme_cls.accent_color
                    bold: True
                    on_release:
                        root.create_user_account(email.text, password.text)

<MDTextFieldCustom@MDTextFieldRound>
    pos_hint: {"center_x": .5}
    normal_color: 1, 1, 1, 1
    color_active: 0, .5, 1, .5

<TrackLocationScreen>:
    name: "tracklocationscreen"
    MDBoxLayout:
        orientation:'vertical'
        MDToolbar:
            title: "Track Location"
            left_action_items: [['arrow-left', lambda x: app.go_back()]] 
            right_action_items: [['magnify', lambda x: app.search_menu.open()]]
            # md_bg_color: 1, 1, 0, 0
            # md_bg_color:0,0,0,0.9
            # theme_text_color:'Custom'
            # text_color:1,1,1,1
            # md_bg_color:1,0,0,.4
            md_bg_color: app.theme_cls.accent_color
            elevation: 5 
        MDBoxLayout:
            orientation:'vertical'
            Toolbar:
                MDFillRoundFlatButton:
                    size_hint_x:None
                    height:40
                    md_bg_color:0.3,1,0.3,.3
                    font_size:16
                    bold: True
                    text: "Blantyre, Makata"
                    # on_release: mapview.center_on(-15.7849456, 35.0249239)
                    on_release: mapview.center_on(-15.786699761047174, 35.02936482382054)
                MDFillRoundFlatButton:
                    size_hint_x:None
                    height:40
                    width: 80
                    font_size:16
                    md_bg_color:1,.6,0,.8
                    bold: True
                    text: "Blantyre, Madziabango"
                    # on_release: mapview.center_on(-15.75328, 35.00245)
                    on_release: mapview.center_on(-15.967405863415127, 34.91093510059491)
                MDFillRoundFlatButton:
                    size_hint_x:None
                    height:40
                    width: 80
                    font_size:16
                    md_bg_color:1,0,0,.4
                    bold: True
                    text: "Mangochi District Hospital"
                    on_release: mapview.center_on(-14.482165891057775, 35.26500916014098)
                MDFillRoundFlatButton:
                    size_hint_x:None
                    height:40
                    width: 80
                    font_size:16
                    md_bg_color:0,.6,.8,1
                    bold: True
                    text: "Nsanje, East Bank"
                    on_release: mapview.center_on(-16.920593, 35.253304)
                MDFillRoundFlatButton:
                    size_hint_x:None
                    height:40
                    md_bg_color:0.3,1,0.3,.3
                    font_size:16
                    bold: True
                    text: "Karonga TTC"
                    on_release: mapview.center_on(-9.954627077117166, 33.91088325225857)
                MDFillRoundFlatButton:
                    size_hint_x:None
                    height:40
                    width: 80
                    font_size:16
                    md_bg_color:1,.6,0,.8
                    bold: True
                    text: "Nkhotakota, Farmers World Shop"
                    on_release: mapview.center_on(-12.92772809750683, 34.28345289485932)
                Spinner:
                    text: "Mulanje, Nansadi"
                    md_bg_color:1,.6,0,.8
                    values: MapSource.providers.keys()
                    on_text: mapview.map_source = self.text
            MapView:
                id: mapview
                # lat: -15.8017858
                # lon: 35.0274508
                lat: -15.8033379281171567 
                lon: 35.0469356769454147
                zoom: 20

                MapMarker:
                    lat: 50.6394
                    lon: 3.057

                MapMarker:
                    lat: -33.867
                    lon: 151.206

            Toolbar:
                md_bg_color:0.3,0.3,0.3,1
                Label:
                    text: "Longitude: {}".format(mapview.lon)
                Label:
                    text: "Latitude: {}".format(mapview.lat)

<Toolbar@BoxLayout>:
    size_hint_y: None
    height: '48dp'
    padding: '4dp'
    spacing: '4dp'
    canvas:
        Color:
            rgba: .2, .2, .2, .6
        Rectangle:
            pos: self.pos
            size: self.size

<ShadedLabel@Label>:
    size: self.texture_size
    canvas.before:
        Color:
            rgba: .2, .2, .2, .6
        Rectangle:
            pos: self.pos
            size: self.size

<Push_Notification_Screen>:
    name: "pushnotification"
    MDBoxLayout:
        orientation:'vertical'
        MDToolbar:
            title: "Send Push Notifications"
            left_action_items: [['arrow-left', lambda x: app.go_back()]] 
            # md_bg_color: 1, 1, 0, 0
            md_bg_color: app.theme_cls.accent_color
            elevation: 5 

        FloatLayout:
            MDTextFieldCustom:
                id: title
                pos_hint: {"center_x": .5, "center_y": .9}
                size_hint: .53, .1
                icon_left: 'format-title'
                hint_text: "Enter Title"
            TextInput:
                id: description
                hint_text: "Enter Description"
                size_hint: .59, .20
                pos_hint: {"center_x": .5, "center_y": .7}

            Button:
                text: "Send Push Notification"
                size_hint: .59, .1
                pos_hint: {"center_x": .5, "center_y": .52}
                color: 1, 1, 1, 1 
                md_bg_color:app.theme_cls.accent_color
                bold: True
                on_release:
                    root.send_push_notification(title.text, description.text)

<Notification_Screen>:
    name: "alertscreen"
    MDBoxLayout:
        orientation:'vertical'
        MDToolbar:
            title: "Send Email Notification"
            left_action_items: [['arrow-left', lambda x: app.go_back()]] 
            # md_bg_color: 1, 1, 0, 0
            md_bg_color: app.theme_cls.accent_color
            elevation: 5 

        FloatLayout:
            MDLabel:
            MDTextFieldCustom:
                id: receiver
                pos_hint: {"center_x": .5, "center_y": .8}
                size_hint: .53, .07
                icon_left: 'email-send'
                hint_text: "Send Email To"
            MDTextFieldCustom:
                id: subject
                pos_hint: {"center_x": .5, "center_y": .7}
                size_hint: .53, .07
                icon_left: 'text-subject'
                hint_text: "Subject"
            TextInput:
                id: msg_body
                hint_text: "Body"
                size_hint: .57, .20
                pos_hint: {"center_x": .5, "center_y": .53}

            Button:
                text: "Send Email Notification"
                size_hint: .57, .07
                pos_hint: {"center_x": .5, "center_y": .36}
                color: 1, 1, 1, 1 
                bold: True
                on_release:
                    root.send_email(receiver.text, subject.text, msg_body.text)

<SubsidyAnalysis>:
    name: "analysisscreen"
    ActionBar:
        pos_hint: {'top': 1.0}
        height: '37dp'
        ActionView:
            ActionPrevious:
                title: ''
                size_hint_x: None
                with_previous: False
                app_icon_width: 0.001
                width: 0

            ActionButton:
                text: 'Home'
                on_release: root.manager.current = 'mainscreen'
                md_bg_color: app.theme_cls.primary_color

            ActionButton:
                text: 'Manage Accounts'
                on_release: root.manager.current = 'useraccountscreen'

            ActionButton:
                text: 'Registered Farmers'
                on_release: root.manager.current = 'registeredfarmersscreen'

            ActionButton:
                text: 'Subsidy Analysis'
                on_release: root.manager.current = 'analysisscreen'

            ActionButton:
                text: 'Settings'
                on_release: root.manager.current = 'settingsscreen'

            ActionButton:
                text: 'Logout'
                on_release: app.sign_out()
    BoxLayout:
        orientation: "vertical"
        id: data_graph
        Screen:
            do_default_tab: False
            size_hint_y: None
            height: root.height - dp(37)
            ScrollView:
                bar_width:0
                MDBoxLayout:
                    padding:'10dp'
                    spacing:'10dp'
                    adaptive_height:True
                    orientation: "vertical"
                    MDCard:
                        id: data_graph
                        size_hint_y:None
                        height:"80dp"
                        orientation:"vertical"
                        padding:"10dp"
                        Button:
                            color: 1, 1, 1, 1 
                            text:'VIEW RECENT ANALYSIS'
                            size_hint: .86 ,.062 
                            bold: True
                            pos_hint: {"center_x": .5, "top": .8}
                            on_release: app.generate_report()
                        
                    MDCard:
                        id: data_graph
                        size_hint_y:None
                        height:"80dp"
                        orientation:"vertical"
                        padding:"10dp"
                        Button:
                            color: 1, 1, 1, 1 
                            text:'TODAYS REPORT'
                            size_hint: .86 ,.062 
                            bold: True
                            pos_hint: {"center_x": .5, "top": .6}
                            on_release: app.generate_report()
<ShowFeedbackScreen>:
    name: "feedbackscreen"
    MDBoxLayout:
        orientation:'vertical'
        MDToolbar:
            title: "Received Feedbacks"
            left_action_items: [['arrow-left', lambda x: app.go_back()]] 
            right_action_items: [['refresh', lambda x: root.refresh_callback()]] 
            # md_bg_color: 1, 1, 0, 0
            md_bg_color: app.theme_cls.accent_color
            elevation: 5 

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(10)
            MDScrollViewRefreshLayout:
                id: refresh_layout
                refresh_callback: root.refresh_callback
                root_layout: root
                MDGridLayout:
                    id: show_feedbacks
                    cols: 1
                    padding: 10, 10
                    spacing: 10, 10
                    adaptive_height: True
                    row_default_height: 140  

<ManageRegisteredFarmers>:
    name: "registeredfarmersscreen"
    ActionBar:
        pos_hint: {'top': 1.0}
        height: '37dp'
        ActionView:
            ActionPrevious:
                title: ''
                size_hint_x: None
                with_previous: False
                app_icon_width: 0.001
                width: 0

            ActionButton:
                text: 'Home'
                on_release: root.manager.current = 'mainscreen'
                md_bg_color: app.theme_cls.primary_color

            ActionButton:
                text: 'Manage Accounts'
                on_release: root.manager.current = 'useraccountscreen'

            ActionButton:
                text: 'Registered Farmers'
                on_release: root.manager.current = 'registeredfarmersscreen'

            ActionButton:
                text: 'Subsidy Analysis'
                on_release: root.manager.current = 'analysisscreen'

            ActionButton:
                text: 'Settings'
                on_release: root.manager.current = 'settingsscreen'

            ActionButton:
                text: 'Logout'
                on_release: app.sign_out()
    MDBoxLayout:
        Screen:
            do_default_tab: False
            size_hint_y: None
            height: root.height - dp(37)
            MDScrollViewRefreshLayout:
                id: refresh_layout
                refresh_callback: root.refresh_callback
                root_layout: root
                # size_hint: 1, .8
                MDGridLayout:
                    id: show_registered_farmers
                    cols: 1
                    spacing: 5, 5
                    padding: 5, 5
                    size_hint_y: None
                    height: self.minimum_height
                    row_default_height: '130dp'
                    row_force_default: True

<SettingsScreen>:
    name: "settingsscreen"
    ActionBar:
        pos_hint: {'top': 1.0}
        height: '37dp'
        ActionView:
            ActionPrevious:
                title: ''
                size_hint_x: None
                with_previous: False
                app_icon_width: 0.001
                width: 0

            ActionButton:
                text: 'Home'
                on_release: root.manager.current = 'mainscreen'
                md_bg_color: app.theme_cls.primary_color

            ActionButton:
                text: 'Manage Accounts'
                on_release: root.manager.current = 'useraccountscreen'

            ActionButton:
                text: 'Registered Farmers'
                on_release: root.manager.current = 'registeredfarmersscreen'

            ActionButton:
                text: 'Subsidy Analysis'
                on_release: root.manager.current = 'analysisscreen'

            ActionButton:
                text: 'Settings'
                on_release: root.manager.current = 'settingsscreen'

            ActionButton:
                text: 'Logout'
                on_release: app.sign_out()
    BoxLayout:
        orientation: "vertical"
        Screen:
            do_default_tab: False
            size_hint_y: None
            height: root.height - dp(37)
            ScrollView:
                bar_width:0
                MDBoxLayout:
                    padding:'10dp'
                    spacing:'10dp'
                    adaptive_height:True
                    orientation: "vertical"
                    MDLabel:
                    MDLabel:
                        text:"SETTINGS"
                        adaptive_height:True
                        bold: True
                    MDCard:
                        size_hint_y:None
                        height:"80dp"
                        orientation:"vertical"
                        padding:"10dp"
                        TwoLineIconListItem:
                            text: "About SubsidyApp"
                            secondary_text: "Optichem . Status . Legal information"
                            divider:None
                            IconLeftWidget:
                                icon: "assets/img/info.png"
                    MDCard:
                        size_hint_y:None
                        height:"80dp"
                        orientation:"vertical"
                        padding:"10dp"
                        TwoLineIconListItem:
                            text: "By Raymond Kondowe"
                            secondary_text: "Questions? Need help?"
                            divider:None
                            IconLeftWidget:
                                icon: "assets/img/About_Me.png"
                    MDCard:
                        size_hint_y:None
                        height:"80dp"
                        orientation:"vertical"
                        padding:"10dp"
                        TwoLineIconListItem:
                            text: "Updates"
                            secondary_text: "Check for updates"
                            divider:None
                            IconLeftWidget:
                                icon: "assets/img/updates.png"         
    MDBoxLayout:   
        MDLabel:
            text:"Subsidy Desktop App V1"  
            halign: "center"
            pos_hint: {"center_y": .4}

'''