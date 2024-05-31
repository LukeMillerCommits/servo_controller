import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
#GPIO.setup(8, GPIO.OUT)

class servo:

    def __init__(self, pin, data_rate, name, servo_min, servo_max):
        self.pin = pin
        self.data_rate = data_rate
        self.name = name
        self.servo_min = servo_min
        self.servo_max = servo_max
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, self.data_rate)
    
    def start(self):
        self.pwm.start(0)

    def change_position(self, position):
        self.pwm.ChangeDutyCycle(position)
        sleep(1)

    def stop(self):
        self.pwm.stop()
        GPIO.cleanup()

    def position_servos(servo, raw_data, data_range_max, data_range_min):
        #Smooth down outlier data
        if (raw_data > data_range_max): raw_data = data_range_max
        if (raw_data < data_range_min): raw_data = data_range_min

        #Convert data within raw range be within servo positional range
        pos_data = raw_data * (servo.servo_max - servo.servo_min)/(data_range_max - data_range_min) + servo.servo_min
        print(servo.name, raw_data, pos_data)
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

        servo.change_position(pos_data)
