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
            LinearLayout = autoclass('android.widget.LinearLayout')
            LayoutParams = autoclass('android.widget.LinearLayout$LayoutParams')
            Color = autoclass('android.graphics.Color')
            activity = autoclass('org.kivy.android.PythonActivity').mActivity

            @run_on_ui_thread
            def create_webview():
                # 1. Create a root container layout
                layout = LinearLayout(activity)
                layout.setOrientation(LinearLayout.VERTICAL)
                layout.setBackgroundColor(Color.BLACK)

                # 2. Get status bar height dynamically in pixels
                resource_id = activity.getResources().getIdentifier("status_bar_height", "dimen", "android")
                status_bar_height = activity.getResources().getDimensionPixelSize(resource_id) if resource_id > 0 else 80

                # 3. Add top padding to the layout (Left, Top, Right, Bottom)
                # You can add extra pixels to status_bar_height if your notch/camera is larger (e.g., status_bar_height + 20)
                layout.setPadding(0, status_bar_height, 0, 0)

                # 4. Initialize WebView and expand it to fill remaining space
                webview = WebView(activity)
                webview.getSettings().setJavaScriptEnabled(True)
                webview.setWebViewClient(WebViewClient())
                webview.loadUrl("https://ocw.mit.edu/")

                # Add WebView to layout with MATCH_PARENT width/height (-1 = MATCH_PARENT)
                params = LayoutParams(-1, -1)
                layout.addView(webview, params)

                # Set activity view to container layout
                activity.setContentView(layout)

            create_webview()
            return Label(text="Loading WebView...")
        else:
            webbrowser.open("https://ocw.mit.edu/")
            return Label(text="Opened in external browser (Desktop mode)")

if __name__ == "__main__":
    MainApp().run()
    
