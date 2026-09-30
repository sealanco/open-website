import webbrowser
from kivy.app import App
from kivy.uix.widget import Widget

class MainApp(App):
    def build(self):
        # Open the webpage automatically when the app builds
        webbrowser.open("https://ocw.mit.edu/")
        
        # Stop the application immediately
        App.get_running_app().stop()
        
        # Kivy requires build() to return a widget
        return Widget()

if __name__ == "__main__":
    MainApp().run()
    
