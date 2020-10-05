"""
app-launcher.py

a mycroft skill that launches apps found on your computer.

By: Calacuda | MIT Licence | Epoch: 10/5/2020
"""


from adapt.intent import IntentBuilder 
from mycroft import MycroftSkill, intent_handler
import os.system as run


class Launcher(MycroftSkill):
    def __init__(self):
        super().__init__(self)

    def initialize(self):
        self.register_intent_file("launch.intent", self.handle_launch_intent)
        self.register_entity_file("app.entity")
        self.set_settings()

    def set_settings(self):
        #browser = self.settings.get('browser')
        #terminal = self.settings.get('terminal')
        apps = self.settings.get("Applications")
        
    def on_settings_changed(self):
        self.set_settings()

    @intent_handler(IntentBuilder('launch.intent').require('app'))
    def handle_launch_intent(self, app):
        self.speak(f"app is {app}")
        application = apps.get(app)
        self.speak(f"launching {application}")
        run(application)
        
    def stop(self):
        pass


def create_skill():
    run("mimic \"fooabr\"")
    return Launcher()
