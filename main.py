from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from jnius import autoclass

class VoiceAssistantApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20)
        self.lbl = Label(text="Jarvis Assistant Ready", font_size='22sp')
        btn = Button(text="Tap to Speak", size_hint=(1, 0.2))
        btn.bind(on_press=self.start_listening)
        layout.add_widget(self.lbl)
        layout.add_widget(btn)
        return layout

    def start_listening(self, instance):
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        Intent = autoclass('android.content.Intent')
        RecognizerIntent = autoclass('android.speech.RecognizerIntent')
        intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH)
        intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
        PythonActivity.mActivity.startActivityForResult(intent, 100)

if __name__ == "__main__":
    VoiceAssistantApp().run()
  
