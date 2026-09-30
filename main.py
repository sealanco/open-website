from kivy.app import App
from kivy.utils import platform
from kivy.uix.label import Label
import webbrowser

class MainApp(App):
    def build(self):
        if platform == "android":
            from android.runnable import run_on_ui_thread
            from jnius import autoclass

            WebView = autoclass('android.webkit.WebView')
            WebViewClient = autoclass('android.webkit.WebViewClient')
            activity = autoclass('org.kivy.android.PythonActivity').mActivity

            @run_on_ui_thread
            def create_webview():
                webview = WebView(activity)
                webview.getSettings().setJavaScriptEnabled(True)
                webview.setWebViewClient(WebViewClient())
                webview.loadUrl("https://ocw.mit.edu/")
                activity.setContentView(webview)

            create_webview()
            return Label(text="Loading WebView...")
        else:
            # Fallback for desktop during development
            webbrowser.open("https://ocw.mit.edu/")
            return Label(text="Opened in external browser (Desktop mode)")

if __name__ == "__main__":
    MainApp().run()
    
