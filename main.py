import kivy
kivy.require('1.0.7')

from kivy.animation import Animation
from kivy.app import App
from kivy.uix.button import Button
import autoclass

class TestApp(App):

    def light(self, instance):
        Camera = autoclass('android.hardware.Camera')
        CameraParameters = autoclass('android.hardware.Camera$Parameters')
        cam = Camera.open()
        params = cam.getParameters()
        params.setFlashMode(CameraParameters.FLASH_MODE_TORCH)
        cam.setParameters(params)
        cam.startPreview()

    def build(self):
        button = Button(size_hint=(None, None), text='plop', on_press=self.light)
        return button


if __name__ == '__main__':
    TestApp().run()