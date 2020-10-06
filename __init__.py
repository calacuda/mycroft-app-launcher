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
        self.apps = self.settings
        
    @intent_handler("launch.intent")
    def handle_launch_intent(self, app):
        #self.speak(f"app is {app}")
        #print("app : ", app)
        #run(f'echo "msg-type {app.msg_type}" >> ~/out.txt')
        #run(f'echo "data {app.data}" >> ~/out.txt')
        #run(f'echo "context {app.context}" >> ~/out.txt')
        #a = "app"
        # run(f'echo "{self.settings}" > ~/settings.txt')
        #try:
        #    run(f'echo "apps :  {apps}" > ~/apps.txt')
        #except:
        #    run(f'echo "apps not assigned" > ~/apps.txt')
        #application = "sterminal"
        #try:
            #application = self.apps.get(app)
        #    application = "urxvt"
        #except:
        #    run(f'echo "application is sterminal" >> ~/apps.txt')
        #    application = "sterminal"
        #self.speak(f"launching {application}")
        application = self.settings.get(app.replace("web browser", "browser"))
        self.acknowledge()
        try:
            run(application)
        except:
            run(f'echo "got error when running :  {app}\nsettings :  {type(self.settings)}\nsettings :  {self.settings}" > ~/apps.txt')
            run("sterminal")
            
    def stop(self):
        pass


def create_skill():
    #Launcher().handle_launch_intent("literally fucking anything")
    return Launcher()

#create_skill()
