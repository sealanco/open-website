import webbrowser
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget

class MainApp(App):
    def build(self):
        # Schedule the web open and exit process after the app initializes
        Clock.schedule_once(self.open_and_close, 0.5)
        return Widget()

    def open_and_close(self, dt):
        webbrowser.open("https://ocw.mit.edu/")
        self.stop()

if __name__ == "__main__":
    MainApp().run()
    
