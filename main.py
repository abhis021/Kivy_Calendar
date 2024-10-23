from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
# from kivymd.uix.dialog import MDDialog
from kivymd.uix.pickers import MDDatePicker
from kivy.core.window import Window

# setting the window size for testing on desktop
Window.size = (300,500)

class CalendarApp(MDApp):
    def build(self):
        # Create the main screen
        screen = Screen()

        #Add a label to display selected date
        self.date_label = MDLabel(
            text = "Select a Date",
            halign = "center",
            pos_hint = {"center_x": 0.5, "center_y":0.7},
            theme_text_color="Primary"
        )
        screen.add_widget(self.date_label)

        #create a button to open date picker
        date_button = MDRaisedButton(
            text="Open Calendar",
            pos_hint={"center_x": 0.5,"center_y": 0.5},
            on_release=self.show_date_picker
        )
        screen.add_widget(date_button)

        return screen
    
    def show_date_picker(self, *args):
        # Create and open the date picker
        date_picker = MDDatePicker()
        date_picker.bind(on_save=self.on_date_selected, on_cancel=self.on_cancel)
        date_picker.open()

    def on_date_selected(self, instance, value, date_range):
        # Update label with the selected date
        self.date_label.text = f"Selected Date: {value}"

    def on_cancel(self, instance, value):
        # Handle the cancel event (optional)
        self.date_label.text = "Date selection canceled"

if __name__== "__main__":
    CalendarApp().run()