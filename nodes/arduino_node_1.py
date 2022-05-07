#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float32
import serial



def talker():
    arduino = serial.Serial('/dev/ttyACM0',115200)
    pub = rospy.Publisher('/arduino_rand', Float32, queue_size=1)
    rospy.init_node('arduino_node_1', anonymous=True)
    rate = rospy.Rate(100) # 10hz
    while not rospy.is_shutdown():
        data = arduino.readline()
        rospy.logerr(data)
        data = data.strip()
        data = data.split('\t')
        print(data)
        floatdata = []
        if(len(data)>0):
            for k in range(0,len(data)):
                if(data[k] is not ''):
                    try:
                        floatdata.append(float(data[k]))
                    except:
                        pass

            #set first one to our message
            msg = Float32()
            if(len(floatdata)>0):
                msg.data = floatdata[0]

                # rospy.loginfo(hello_str)
                pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:

        talker()
    except rospy.ROSInterruptException:
        pass