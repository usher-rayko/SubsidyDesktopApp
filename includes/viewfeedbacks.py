from kivy.uix.relativelayout import RelativeLayout
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout

Builder.load_string("""
<ViewFeedbacks>:
    canvas:
        Color:
            rgba: 0, .5, .8, 0.2
        RoundedRectangle:
            # radius: (40, 40)
            pos: self.pos
            size: self.size   
    MDLabel:
        id: message
        font_size: 16
        bold: True
        theme_text_color: "Primary"
        size_hint: (.90, 0.70)
        pos_hint: {"center_x": .56, "center_y": .9}
    MDLabel:
        id: from_user
        font_size: 16
        theme_text_color: "Primary"
        size_hint: (.90, 0.70)
        pos_hint: {"center_x": .57, "center_y": .7}
    
    OneLineIconListItem:
        id: date_sent
        pos_hint: {"center_x": .48, "center_y": .6}
        size_hint: (.90, 0.70)
        font_size: 12
        IconLeftWidget:
            icon: "assets/img/opt_icon.png"

""")

class ViewFeedbacks(RelativeLayout):
    def __init__(self, **kw):
        super().__init__()
        self.ids.from_user.text = kw['from_user']
        self.ids.message.text = kw['message']

        self.from_ = kw['from_user']
        self.text = kw['message']
        self.date = kw['date_sent']

        self.ids.from_user.text = f"From: {self.from_}"
        self.ids.message.text = f"Message: {self.text}"
        self.ids.date_sent.text = f"Date Sent: {self.date}"

