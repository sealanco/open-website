import threading
import time
import webbrowser
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget

class MainApp(App):
    def build(self):
        # Schedule the browser thread to start after the UI mounts
        Clock.schedule_once(self.launch_browser_and_exit, 1.0)
        return Widget()

    def launch_browser_and_exit(self, dt):
        # Run browser launch in a separate thread so it doesn't block Kivy
        threading.Thread(target=self._worker, daemon=True).start()

    def _worker(self):
        # Open the webpage
        webbrowser.open("https://ocw.mit.edu/")
        
        # Give the operating system time to dispatch the URL to the browser
        time.sleep(1.5)
        
        # Gracefully shut down Kivy on the main thread
        Clock.schedule_once(lambda dt: App.get_running_app().stop(), 0)

if __name__ == "__main__":
    MainApp().run()
    
