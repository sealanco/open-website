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
                # 1. Set the Android status bar background to black
                window = activity.getWindow()
                window.addFlags(0x80000000)  # FLAG_DRAWS_SYSTEM_BAR_BACKGROUNDS
                window.clearFlags(0x04000000)  # CLEAR FLAG_TRANSLUCENT_STATUS
                window.setStatusBarColor(Color.BLACK)

                # 2. Create parent container and set background to solid black
                layout = LinearLayout(activity)
                layout.setOrientation(LinearLayout.VERTICAL)
                layout.setBackgroundColor(Color.BLACK)  # Sets top margin area to black

                # 3. Calculate status bar / notch height
                resource_id = activity.getResources().getIdentifier("status_bar_height", "dimen", "android")
                status_bar_height = activity.getResources().getDimensionPixelSize(resource_id) if resource_id > 0 else 80

                # 4. Apply top padding
                layout.setPadding(0, status_bar_height, 0, 0)

                # 5. Initialize WebView
                webview = WebView(activity)
                webview.getSettings().setJavaScriptEnabled(True)
                webview.setWebViewClient(WebViewClient())
                webview.loadUrl("https://ocw.mit.edu/")

                # Add WebView to fill remaining space
                params = LayoutParams(-1, -1)
                layout.addView(webview, params)

                # Display full layout
                activity.setContentView(layout)

            create_webview()
            return Label(text="Loading WebView...")
        else:
            webbrowser.open("https://ocw.mit.edu/")
            return Label(text="Opened in external browser (Desktop mode)")

if __name__ == "__main__":
    MainApp().run()
    
