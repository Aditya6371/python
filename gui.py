
import kivy
kivy.require('2.2.1')

from kivy.app import App
from kivy.uix.button import Label
  
# Inherit Kivy's App class which represents the window
# for our widgets
# HelloKivy inherits all the fields and methods
# from Kivy
class HelloKivy(App):
    
    # This returns the content we want in the window
    def build(self):
  
        # Return a label widget with Hello Kivy
        return Label(text ="hii")
  
helloKivy = HelloKivy()
helloKivy.run()