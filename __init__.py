from adapt.intent import IntentBuilder 
from mycroft import MycroftSkill, intent_handler
from os import system as run


class Launcher(MycroftSkill):

    def __init__(self):
        super().__init__()

    def initialize(self):
        self.register_intent("launch.intent", self.handle_launch_intent)
        self.register_entity("app.entity")
        
    @intent_handler(IntentBuilder("LaunchIntnet").require("launch.voc"))
    def handle_launch_intent(self, app):
        self.speak(f"app is {app}")
        application = apps.get(app)
        self.speak(f"launching {application}")
        run(application)
        
    def stop(self):
        pass


def create_skill():
    return Launcher()

create_skill()
