from adapt.intent import IntentBuilder 
from mycroft import MycroftSkill, intent_handler
from os import system as run


class Launcher(MycroftSkill):

    def __init__(self):
        super().__init__()
        #self.initialize()
        #self.apps = self.settings
        
    def initialize(self):
        self.register_entity_file("app.entity")
        #self.register_intent_file("launch.intent", self.handle_launch_intent)
        #self.apps = self.settings
        
    @intent_handler("launch.intent")
    def handle_launch_intent(self, app):
        application = self.settings.get(app.data.get("app").replace("web browser", "browser"))
        self.acknowledge()
        try:
            run(application)
        except:
            run(f'echo "got error when running :  {app.__dict__}\nsettings :  {type(self.settings)}\nsettings :  {self.settings}" > ~/mycroft_launcher_error.txt')
            run('notify-send "Mycroft" "Error opening application. Do you have it installed? Was it spelled correctly? Check ~/mycroft_launcher_error.txt for more details." -t 5000')
            
    def stop(self):
        pass


def create_skill():
    return Launcher()
