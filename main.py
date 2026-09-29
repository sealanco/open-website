import webbrowser
from kivy.app import App
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        btn = Button(
            text="Visit MIT OpenCourseWare",
            size_hint=(0.4, 0.2),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        btn.bind(on_press=self.open_url)
        return btn

    def open_url(self, instance):
        webbrowser.open("https://ocw.mit.edu/")
if __name__ == "__main__":
    MainApp().run()
    
