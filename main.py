import webbrowser
from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        # Open the webpage automatically when the app builds
        webbrowser.open("https://ocw.mit.edu/")
        
        # Kivy requires build() to return a widget
        return Label(text="Opening MIT OpenCourseWare...")

if __name__ == "__main__":
    MainApp().run()
    
