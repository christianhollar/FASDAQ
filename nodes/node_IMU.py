#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float32
import serial



def talker():
    arduino = serial.Serial('/dev/ttyACM0',9600)
    rospy.init_node('arduino_node_IMU_x', anonymous=True)
    rate = rospy.Rate(100) # 10hz

    while not rospy.is_shutdown():
        data = arduino.readline()
        if 'Euler' in data:
            current = data.split(',')

            pub = rospy.Publisher('/Euler_X',Float32,queue_size=1)
            msg = Float32();
            msg.data = float(current[1])
            pub.publish(msg)
            
            pub = rospy.Publisher('/Euler_Y',Float32,queue_size=1)
            msg = Float32();
            msg.data = float(current[2])
            pub.publish(msg)

            pub = rospy.Publisher('/Euler_Z',Float32,queue_size=1)
            msg = Float32();
            msg.data = float(current[3])
            pub.publish(msg)
        if 'Gyro' in data:
            current = data.split(',')

            pub = rospy.Publisher('/Gyro_X',Float32,queue_size=1)
            msg = Float32();
            msg.data = float(current[1])
            pub.publish(msg)
            
            pub = rospy.Publisher('/Gyro_Y',Float32,queue_size=1)
            msg = Float32();
            msg.data = float(current[2])
            pub.publish(msg)

            pub = rospy.Publisher('/Gyro_Z',Float32,queue_size=1)
            msg = Float32();
            msg.data = float(current[3])
            pub.publish(msg)
        if 'Acc' in data:
            current = data.split(',')

            pub = rospy.Publisher('/Acc_X',Float32,queue_size=1)
            msg = Float32();
            msg.data = float(current[1])
            pub.publish(msg)
            
            pub = rospy.Publisher('/Acc_Y',Float32,queue_size=1)
            msg = Float32();
            msg.data = float(current[2])
            pub.publish(msg)

            pub = rospy.Publisher('/Acc_Z',Float32,queue_size=1)
            msg = Float32();
            msg.data = float(current[3])
            pub.publish(msg)


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass