from mycroft import MycroftSkill, intent_handler
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

class LedControl(MycroftSkill):
    
    def __init__(self):
        MycroftSkill.__init__(self)
        

    @intent_handler('led_skill.intent')
    def handle_led_skill(self, message):
        self.speak_dialog('led_skill')
        GPIO.output(7,True)

def create_skill():
    return LedControl()

