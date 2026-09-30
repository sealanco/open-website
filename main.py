from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from plyer import webbrowser

class MainApp(App):
    def build(self):
        # Schedule browser launch slightly after app initialization
        Clock.schedule_once(self.open_and_close, 0.5)
        return Widget()

    def open_and_close(self, dt):
        # Plyer automatically handles Android/iOS/Desktop intent systems
        webbrowser.open("https://ocw.mit.edu/")
        self.stop()

if __name__ == "__main__":
    MainApp().run()
    
