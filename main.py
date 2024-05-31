import servo_pos
import read_from_serial
from time import sleep

#Servo Limits
#x_min = 5.5
#x_max = 11
#y_min = 2
#y_max = 12.2
#Create servo objects
servo1 = servo_pos.servo(8, 50, "servo1", 5.5, 11)
servo2 = servo_pos.servo(10, 50, "servo2", 2, 12.5)

#Start servos
servo1.start()
servo2.start()

#Create Serial object
ser = read_from_serial.serial_port('/dev/ttyACM0')

#Data Range Limits
raw_data_range_max = 20
raw_data_range_min = 0

while True:
    #Get data from accelerometer

    #read a '\n' terminated line
    ser.read_line()

    #Position servos using data
    servo1.position_servos(ser.raw_data_x, raw_data_range_max, raw_data_range_min)
    servo2.position_servos(ser.raw_data_y, raw_data_range_max, raw_data_range_min)
