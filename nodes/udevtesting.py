import serial
ser = serial.Serial('/dev/IMU')
print(ser.readLine)