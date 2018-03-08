import RPi.GPIO as GPIO
import SimpleMFRC522
import time
import threading

from time import sleep
from pygame import mixer
from enum import Enum

class Language(Enum):
    ENG = "English"
    SPA = "Spanish"
    NONE = "None"

class Animatronic(self):

    def __init__:
        # Initialize GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        # Hydraulics GPIO pins
        GPIO.setup(20,GPIO.OUT)
        GPIO.setup(21,GPIO.OUT)
        GPIO.output(21, GPIO.HIGH)

        # Lights GPIO pins
        GPIO.setup(13,GPIO.OUT)
        GPIO.setup(19,GPIO.OUT)

        # Mouth (servo) GPIO pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(26, GPIO.OUT)
        p = GPIO.PWM(26,100)

        # Head (servo) GPIO pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4, GPIO.OUT)
        p2 = GPIO.PWM(4,100)
        
        # Arm (servo) GPIO pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(5, GPIO.OUT)
        p3 = GPIO.PWM(5,100)

        # Back-toggle-switch GPIO pin
        #
        # - To be implemented in the future
        #
        GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)


        # Instance variables

        # Testing mode
        self.testing_mode = False

        # Language mode
        self.lang = Language.NONE

        # Motor counter variable
        self.motor_time = 0.0

        # Time (in secs) for sleep mode
        self.sleep_threshold = 10
        
        # Hydraulics motor state
        motor_state = GPIO.LOW

        # Light 1 status
        self.light_one_status = GPIO.LOW
        
        # Light 2 status
        self.light_two_status = GPIO.LOW

        # RFID Reader
        self.reader = SimpleMFRC522.SimpleMFRC522()


    # Hydraulic methods

    def switch_motor_state(self):
        if self.motor_state == GPIO.LOW:
            GPIO.output(21, GPIO.HIGH)
            self.motor_state = GPIO.HIGH
            return
        if self.motor_state == GPIO.HIGH:
            GPIO.output(21, GPIO.LOW)
            self.motor_state = GPIO.LOW
            return

    def switch_cylinder_direction():
        global cylinder_direction
        if cylinder_direction == GPIO.LOW:
            GPIO.output(20, GPIO.HIGH)
            cylinder_direction = GPIO.HIGH
            return
        if cylinder_direction == GPIO.HIGH:
            GPIO.output(20, GPIO.LOW)
            cylinder_direction = GPIO.LOW
            return

    # Light methods

    def toggle_light_one(self):
        if self.light_one_status == GPIO.LOW:
            GPIO.output(13, GPIO.HIGH)
            light_one_status = GPIO.HIGH
            return
        if light_one_status == GPIO.HIGH:
            GPIO.output(13, GPIO.LOW)
            light_one_status = GPIO.LOW
            return

    def toggle_light_two():
        global light_two_status
        if light_two_status == GPIO.LOW:
            GPIO.output(19, GPIO.HIGH)
            light_two_status = GPIO.HIGH
            return
        if light_two_status == GPIO.HIGH:
            GPIO.output(19, GPIO.LOW)
            light_two_status = GPIO.LOW
            return

# NOTE TO MYSELF: Study referencing in python to see if you can simplify the toggle_light_... methods to a single method that updates an instance variable given two parameters!



class ThreadCounter:
    def __init__(self, interval = 1):
        self.interval = interval
        self.counter = 0.0
        self.on = False
        self.sleep_threshold = 60

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            if self.on:
                self.counter += 1
                print "Thread counter is " + str(self.counter) + " AND THRESHOLD IS " + str(self.sleep_threshold)
                if self.counter >= self.sleep_threshold:
                    blinker()
                    time.sleep(2)
                    sleep_voice()
                    raise_ramp()
                    self.counter = 0
                    self.on = False
            time.sleep(self.interval)



reader = SimpleMFRC522.SimpleMFRC522()

# LED Status (ON)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Switch
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Hydraulics setup
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.output(21, GPIO.HIGH)

# Lights setup
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)

# Mouth
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
p = GPIO.PWM(26,100)

# Head
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
p2 = GPIO.PWM(4,100)

# Arm
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
p3 = GPIO.PWM(5,100)

#Initialize mixer
mixer.init()

testing = False
lang = "NONE"
motor_time = 0

counter = 0.0
sleep_threshold = 10

ask_lang = True
counter_thread = ThreadCounter()

cylinder_direction = GPIO.LOW
motor_state = GPIO.LOW

light_one_status = GPIO.LOW
light_two_status = GPIO.LOW

def sleep_monkey():
    raise_ramp()

def raise_arm():
    p3.start(2)
    sleep(3)
    p3.stop()

def lower_arm():
    p3.start(88)
    sleep(2.5)
    p3.stop()

def sleep_voice():
    global lang
    move_mouth()
    playSong("sleep_"+lang, False)
    sleep(3)
    stop_mouth()

def blinker():
    toggle_light_one()
    toggle_light_two()
    sleep(1)
    toggle_light_one()
    toggle_light_two()
    sleep(1)
    toggle_light_one()
    toggle_light_two()

def play_background():
    print "RUNNING BACKGROUND"
    playSong("background", True)

def stop_background():
    print("STOP!")
    stopSong(1)

def set_lang(text):
    print "Setting lang to " + text
    global lang
    global ask_lang
   
    lang = text
    stop_background()
    move_mouth()
    toggle_light_one()
    toggle_light_two()
    playSong("intro_" + lang, False)
    sleep(7)
    stop_mouth()
    lower_ramp()
    ask_lang = False
    print "Status of the lang is " + str(ask_lang)
    global counter_thread
    counter_thread.on = True
    runTagLoop()

def lower_ramp():
    global lang
    switch_cylinder_direction()
    switch_motor_state()
    move_head()
    sleep(1.5)
    stop_head()
    sleep(3.5)
    switch_motor_state()
    move_mouth()
    playSong("choose_" + lang ,False)
    sleep(4.5)
    stop_mouth()
    play_background()

def raise_ramp():
    switch_cylinder_direction()
    switch_motor_state()
    sleep(5)
    switch_motor_state()
    global ask_lang
    ask_lang = True

def move_mouth():
    p.start(2)

def stop_mouth():
    p.stop()

def move_head():
    p2.start(2)

def stop_head():
    p2.stop()

def get_time():
    return int(round(time.time() * 1000))

def playSong(song_name, repeat):
    mixer.init()
    mixer.music.load("/home/pi/MFRC522-python/" + song_name + ".mp3")
    
    print "Running song %s" %(song_name)
    if repeat:
        mixer.music.play(loops = -1)
    else:
        mixer.music.play()

def stopSong(fadeout_time):
    sleep(fadeout_time)
    mixer.music.fadeout(fadeout_time)
    mixer.music.stop()
    mixer.quit()


def toggle_light_one():
    global light_one_status
    if light_one_status == GPIO.LOW:
        GPIO.output(13, GPIO.HIGH)
        light_one_status = GPIO.HIGH
        return
    if light_one_status == GPIO.HIGH:
        GPIO.output(13, GPIO.LOW)
        light_one_status = GPIO.LOW
        return

def toggle_light_two():
    global light_two_status
    if light_two_status == GPIO.LOW:
        GPIO.output(19, GPIO.HIGH)
        light_two_status = GPIO.HIGH
        return
    if light_two_status == GPIO.HIGH:
        GPIO.output(19, GPIO.LOW)
        light_two_status = GPIO.LOW
        return


def switch_cylinder_direction():
    global cylinder_direction
    if cylinder_direction == GPIO.LOW:
        GPIO.output(20, GPIO.HIGH)
        cylinder_direction = GPIO.HIGH
        return
    if cylinder_direction == GPIO.HIGH:
        GPIO.output(20, GPIO.LOW)
        cylinder_direction = GPIO.LOW
        return

def refresh_counter():
    global counter_thread
    counter_thread.counter = 0

def runFirst():
    print "Runnning first tag"
    refresh_counter()
    global lang
    stop_background()
    move_mouth()
    playSong("1" + lang, False)
    raise_arm()
    lower_arm()
    sleep(0.5)
    stop_mouth()
    refresh_counter()
    play_background()
    
    

def runSecond():
    print "Runnning second tag"
    refresh_counter()
    global lang
    stop_background()
    move_mouth()
    playSong("2" + lang, False)
    raise_arm()
    lower_arm()
    sleep(0.5)
    stop_mouth()
    refresh_counter()
    play_background()

def runThird():
    print "Runnning third tag"
    refresh_counter()
    global lang
    stop_background()
    move_mouth()
    playSong("3" + lang, False)
    sleep(3)
    raise_arm()
    lower_arm()
    sleep(3)
    move_head()
    sleep(1.5)
    stop_head()
    sleep(15)
    #sleep(28)
    stop_mouth()
    refresh_counter()
    play_background()

def runFourth():
    print "Runnning fourth tag"
    refresh_counter()
    global lang
    stop_background()
    move_mouth()
    playSong("4" + lang, False)
    raise_arm()
    lower_arm()
    sleep(5.5)
    stop_mouth()
    refresh_counter()
    play_background()

def animation(delay):
    move_head()
    sleep(delay)
    stop_head()

def switch_motor_state():
    global motor_state
    if motor_state == GPIO.LOW:
        GPIO.output(21, GPIO.HIGH)
        motor_state = GPIO.HIGH
        return
    if motor_state == GPIO.HIGH:
        GPIO.output(21, GPIO.LOW)
        motor_state = GPIO.LOW
        return

play_background()
switch_motor_state()
switch_cylinder_direction()
loop_counter = 0

def runTagLoop():
    while(True):
        global loop_counter
        global testing
        global motor_time 
        global ask_lang

        loop_counter += 1
        print "Current loop #" + str(loop_counter)
        if testing:
            input = raw_input("> ")
            if input == "cyl":
                switch_cylinder_direction()
            elif input == "motor":
                switch_motor_state()
                if motor_time != 0:
                    print "Lenght: %s" % str(get_time() - motor_time)
                motor_time = get_time()
            elif input == "both":
                switch_motor_state()
                switch_cylinder_direction()
            elif input == "exit":
                testing = False
            elif input == "toggle_light_one()":
                toggle_light_one()
            elif input == "toggle_light_two()":
                toggle_light_two()
            elif input == "lall":
                toggle_light_one()
                toggle_light_two()
            elif input == "m1":
                move_mouth()
            elif input == "m2":
                stop_mouth()
            elif input == "h1":
                move_head()
            elif input == "h2":
                stop_head()
            elif input == "raise":
                raise_ramp()
            elif input == "lower":
                lower_ramp()
            elif input == "a1":
                lower_arm()
            elif input == "a2":
                raise_arm()
            elif input == "cat":
                animation(3)
            continue

        try:
            id, text = reader.read()
            cat = str(text).replace(" ", "")
            print "Reading " + cat + " and raw is " + text
            print "Ask lang is " + str(ask_lang)            

            if ask_lang:
                if cat == "s" or cat == "e":
                    print "Busy state: " + str(mixer.music.get_busy())
                    set_lang(cat)
                    break

            else:
                print "STUFF??"
                if cat == "1":
                    runFirst()
                elif cat == "2":
                    runSecond()
                elif cat == "3":
                    runThird()
                elif cat == "4":
                    runFourth()
            print "Card %s" %text
        finally:
            print "Maybe crash?"
    sleep(0.5)

runTagLoop()
