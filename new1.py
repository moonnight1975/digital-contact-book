from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivy.lang import Builder

KV = '''
MDScreen:

    MDBoxLayout:
        orientation: "vertical"

        ScrollView:

            MDBoxLayout:
                id: card_container
                orientation: "vertical"
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(20)
                padding: dp(10)
                 

        

        MDTopAppBar:
            title: "Label"
            left_action_items: [["menu", lambda x: None]]
            right_action_items: [["account", lambda x: None]]
            md_bg_color: app.theme_cls.primary_color
'''

class ContactCard(MDCard):
    def __init__(self, user_name, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, None)
        self.height = "100dp"
        self.padding = "10dp"
        self.radius = [50]
        self.md_bg_color = (0.6, 0.2, 0.2, 1)  # Custom reddish background

        layout = MDBoxLayout(orientation="horizontal", spacing=10)
        
        image = MDIconButton(
            icon="account-circle",
            font_size="48sp"
        )

        label = MDLabel(
            text=user_name,
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_style="H6"
        )
        
        layout.add_widget(image)
        layout.add_widget(label)
        self.add_widget(layout)

class ContactApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.theme_style = "Dark"  # or "Light" if you prefer
        screen = Builder.load_string(KV)

        container = screen.ids.card_container
        for i in range(1, 9):
            card = ContactCard(f"USER {i}")
            container.add_widget(card)

        return screen

ContactApp().run()
