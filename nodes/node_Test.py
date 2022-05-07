#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float32
import serial

def talker():
    arduino = serial.Serial('/dev/ttyACM0',9600)
    rospy.init_node('arduino_node_IMU_x', anonymous=True)
    #rate = rospy.Rate(100) # 10hz

    while not rospy.is_shutdown():

        data = arduino.readline()
        print(data)

        if 'Euler' in data:

            current = data.split(',')
            topic_list = ["Euler_X","Euler_Y","Euler_Z"]

            for i in range(3):

                if current[i+1] is not None:
                    pub = rospy.Publisher(topic_list[i],Float32,queue_size=1)
                    msg = Float32();
                    msg.data = float(current[i+1])
                    pub.publish(msg)
        
        i = 0

        if 'Gyro' in data:
            current = data.split(',')

            topic_list = ["Gyro_X","Gyro_Y","Gyro_Z"]

            for i in range(3):

                if current[i+1] is not None:
                    pub = rospy.Publisher(topic_list[i],Float32,queue_size=1)
                    msg = Float32();
                    msg.data = float(current[i+1])
                    pub.publish(msg)   

        if 'Acc' in data:
            current = data.split(',')

            topic_list = ["Acc_X","Acc_Y","Acc_Z"]

            for i in range(3):

                if current[i+1] is not None:
                    pub = rospy.Publisher(topic_list[i],Float32,queue_size=1)
                    msg = Float32();
                    msg.data = float(current[i+1])
                    pub.publish(msg) 

        if 'LinAcc' in data:
            current = data.split(',')

            topic_list = ["LinAcc_X","LinAcc_Y","LinAcc_Z"]

            for i in range(3):

                if current[i+1] is not None:
                    pub = rospy.Publisher(topic_list[i],Float32,queue_size=1)
                    msg = Float32();
                    msg.data = float(current[i+1])
                    pub.publish(msg)          

        if 'GNRMC' in data:
            current = data.split(',')

            for i in range(12):

                if i + 1 == 2 or 4 or 6 or 11 or 12:
                    continue

                print(current[i+1])
                topic_list = ["Time_Stamp","Latitude","Longitude","Speed","Course","Date","Variation"]
                if current[i+1] is not None:
                    pub = rospy.Publisher(topic_list[i],Float32,queue_size=1)
                    msg = Float32();
                    msg.data = float(current[i+1])
                    pub.publish(msg)     

            

if __name__ == '__main__':
    try:
        talker()
    except:
        talker()
        pass