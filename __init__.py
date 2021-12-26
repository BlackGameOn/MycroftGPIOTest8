from mycroft import MycroftSkill, intent_handler
import RPi.GPIO as GPIO

GPIO.setup(14,GPIO.OUT)

class LedControl(MycroftSkill):
    
    def __init__(self):
        MycroftSkill.__init__(self)
        

    @intent_handler('led_skill.intent')
    def handle_led_skill(self, message):
        self.speak_dialog('led_skill')
        GPIO.output(14,True)

def create_skill():
    return LedControl()

