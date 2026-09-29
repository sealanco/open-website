from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class HelloWorldApp(App):
    def build(self):
        # Main layout container
        layout = BoxLayout(
            orientation='vertical',
            padding=30,
            spacing=20
        )

        # Label widget
        self.label = Label(
            text='Hello, World!',
            font_size='28sp',
            color=(1, 1, 1, 1)  # RGBA: White
        )

        # Button widget
        button = Button(
            text='Click Me!',
            size_hint=(1, 0.3),
            font_size='20sp'
        )
        # Bind button press to event handler
        button.bind(on_press=self.on_button_click)

        # Add widgets to layout
        layout.add_widget(self.label)
        layout.add_widget(button)

        return layout

    def on_button_click(self, instance):
        self.label.text = 'Button Clicked!'


if __name__ == '__main__':
    HelloWorldApp().run()
    
