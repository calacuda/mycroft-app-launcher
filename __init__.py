from adapt.intent import IntentBuilder 
from mycroft import MycroftSkill, intent_handler
from os import system as cmd


class Launcher(MycroftSkill):

    def __init__(self):
        super().__init__()
        #self.initialize()
        #self.apps = self.settings

    def initialize(self):
        self.register_entity_file("app.entity")
        #self.register_intent_file("launch.intent", self.handle_launch_intent)
        #self.apps = self.settings

    def get_aliases(self, aliases):
        """
        splits the aliases setting into a a more computer friendly format.
        """
        # cmd(f"notify-send {self.settings}")
        print("settings : ", self.settings.keys())
        aliases = {}
        for alias in [(alias.split("=")[0].strip(" "), alias.split("=")[1].strip(" "))
                      for alias in self.settings.get("aliases").split(", ")]:
            aliases[alias[0]] = alias[1]
        return aliases

    def equivilency(self, app_name):
        aliases = self.get_aliases(self.settings.get("aliases"))
        print("aliases : ", aliases)
        if app_name in {"web browser", "browser", "google", "google machine", "internet", "internet program"}:
            return "browser"
        elif app_name in {"terminal", "terminals", "prompt", "prompts", "command prompt", "command prompts", "CLI", "CLI's"}:
            return "terminal"
        elif app_name == "minecraft":
            return "minecraft-launcher"
        elif app_name in aliases.keys():
            return aliases.get("app_name")
        else:
            return app_name

    def get_target_app(self, app_title):
        app_name = self.equivilency(app_title.lower())
        print("app_name : ", app_name)
        white_list = self.settings.get("white list").split(",")
        if app_name in self.settings.keys():
            return self.settings.get(app_title)
        #elif app_title not in white_list and app_title not in self.settings.keys():
        #    return 1
        elif (app_title in white_list) or (app_name in white_list):
            return app_name
        else:
            return 1

    @intent_handler("launch.intent")
    def handle_launch_intent(self, app):
        #cmd(f'notify-send "DEBUG" "{app.data.get("app")}"')
        self.acknowledge()
        print("app : ", app.data)
        if "app" in app.data.keys():
            key = "app"  # self.settings.get(self.equivilency(app.data.get("app")))
        elif "game" in app.data.keys():
            key = "game"
        else:
            key = "app"
        application = self.get_target_app(app.data.get(key))
        # application = self.get_target_app(app)
        print("application : ", application)
        #self.acknowledge()
        if application != 1:
            self.speak(f"running {application}")
            cmd(f'notify-send "Running" "{application}"')
            try:
                cmd(application)
                return True
            except:
                self.speak("bruh... I can't do that.")
                cmd(f'echo "got error when running :  {app.__dict__}\nsettings :  {type(self.settings)}\nsettings :  {self.settings}" > ~/mycroft_launcher_error.txt')
                cmd(f'notify-send "Mycroft" "Error opening application {application}. Do you have it installed? Was it spelled correctly whitelisted? Check ~/mycroft_launcher_error.txt for more details." -t 5000')
                return False
        else:
            cmd('notify-send "Mycroft" "I can\'t run that!"')
            self.speak_dialog("unknown_app")
            return False

    def stop(self):
        pass


def create_skill():
    #cmd('notify-send "debug" "making app launcher"')
    return Launcher()


if __name__ == "__main__":
    skill = Launcher()
    skill.handle_launch_intent("pulse audio")
