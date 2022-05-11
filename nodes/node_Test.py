#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float32,String
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
        elif 'Gyro' in data:
            current = data.split(',')
            topic_list = ["Gyro_X","Gyro_Y","Gyro_Z"]
            for i in range(3):
                if current[i+1] is not None:
                    pub = rospy.Publisher(topic_list[i],Float32,queue_size=1)
                    msg = Float32();
                    msg.data = float(current[i+1])
                    pub.publish(msg)
        elif 'LinAcc' in data:
            current = data.split(',')
            topic_list = ["LinAcc_X","LinAcc_Y","LinAcc_Z"]
            for i in range(3):
                if current[i+1] is not None:
                    pub = rospy.Publisher(topic_list[i],Float32,queue_size=1)
                    msg = Float32();
                    msg.data = float(current[i+1])
                    pub.publish(msg)
        elif 'Acc' in data:
            current = data.split(',')
            topic_list = ["Acc_X","Acc_Y","Acc_Z"]
            for i in range(3):
                if current[i+1] is not None:
                    pub = rospy.Publisher(topic_list[i],Float32,queue_size=1)
                    msg = Float32();
                    msg.data = float(current[i+1])
                    pub.publish(msg)
        elif 'GNRMC' in data:
            print(data)
        	# https://openrtk.readthedocs.io/en/latest/communication_port/nmea.html
            current = data.split(',')
            print(len(current))
            for i in range(11):
            	topic_list = ["Time_Stamp","Position_Status","Latitude","Latitude_Hemisphere","Longitude","Longitude_Hemisphere","Speed","Course","Date","Magnetic_Declination","Magnetic_Declination_Direction","Mode_Indication"]
            	try:
                    if i + 1 in [2, 4, 6, 11, 12]:
                        if current[i+1] is not "":
                            pub = rospy.Publisher(topic_list[i],String,queue_size=1)
                            pub.publish(String(current[i+1]))
    	            	continue
                    if current[i+1] is not "":
                        print(i+1)
                        pub = rospy.Publisher(topic_list[i],Float32,queue_size=1)
                        msg = Float32()
                        msg.data = float(current[i+1])
                        pub.publish(msg)
                except:
                    continue
        else:
			pub = rospy.Publisher('Other',String,queue_size=1)
			pub.publish(String(data))


if __name__ == '__main__':
    try:
        talker()
    except:
        talker()
        pass