import serial

class serial_port:

    def __init__(self, port):
        self.port = serial.Serial(port)  # open serial port
        self.raw_data_x = 0
        self.raw_data_y = 0

    def read_line(self):

        line = self.port.readline().decode("utf-8")   # read a '\n' terminated line
        self.raw_data_x = float(line.split()[0]) + 10
        self.raw_data_y = float(line.split()[1]) + 10
