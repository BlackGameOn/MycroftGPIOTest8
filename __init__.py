from mycroft import MycroftSkill, intent_handler


class LedControl(MycroftSkill):
    
    def __init__(self):
        MycroftSkill.__init__(self)
        

    @intent_handler('led_skill.intent')
    def handle_led_skill(self, message):
        python //home//pi/kerems//LED_AC.py
        self.speak_dialog('led_skill')

def create_skill():
    return LedControl()

