from adapt.intent import IntentBuilder 
from mycroft import MycroftSkill, intent_handler
from os import system

run = system

class Launcher(MycroftSkill):
    def __init__(self):
        super().__init__()

    def initialize(self):
        self.register_intent("launch.intent", self.handle_launch_intent)
        self.register_entity("app.entity")
        self.set_settings()

    def set_settings(self):
        #browser = self.settings.get('browser')
        #terminal = self.settings.get('terminal')
        apps = self.settings.get("Applications")
        
    def on_settings_changed(self):
        self.set_settings()

    @intent_handler('launch.intent')
    def handle_launch_intent(self, app):
        self.speak(f"app is {app}")
        application = apps.get(app)
        self.speak(f"launching {application}")
        run(application)
        
    def stop(self):
        pass


def create_skill():
    return Launcher()
