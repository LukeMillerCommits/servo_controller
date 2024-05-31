from MPU6050 import MPU6050
import time
from machine import Pin
from time import sleep_ms

VCC = Pin(13, Pin.OUT)
GND = Pin(12, Pin.OUT)
VCC.value(1)
GND.value(0)
time.sleep(.2)

mpu = MPU6050()

num_samples = 100  # adjust as required

x_accel_sum = 0
y_accel_sum = 0
x_gyro_sum = 0
y_gyro_sum = 0

while True:
    for i in range(num_samples):
        # Accelerometer Data
        accel = mpu.read_accel_data() # read the accelerometer [ms^-2]
        aX = accel["x"]
        x_accel_sum += aX
        aY = accel["y"]
        y_accel_sum += aY
        aZ = accel["z"]
        
        gyro = mpu.read_gyro_data() # read the accelerometer [ms^-2]
        gX = gyro["x"]
        x_gyro_sum += gX
        gY = gyro["y"]
        y_gyro_sum += gY
        gZ = gyro["z"]
    x_accel_average = x_accel_sum / num_samples
    y_accel_average = y_accel_sum / num_samples
    x_gyro_average = x_gyro_sum / num_samples
    y_gyro_average = y_gyro_sum / num_samples

    print(x_accel_average, y_accel_average)


    x_accel_sum = 0
    y_accel_sum = 0
    x_gyro_sum = 0
    y_gyro_sum = 0

    sleep_ms(100)
