#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float32
from std_msgs.msg import String
import serial

def talker():
    arduino = serial.Serial('/dev/ttyACM0',9600)
    rospy.init_node('arduino_node_IMU_x', anonymous=True)
    rate = rospy.Rate(100) # 10hz

    while not rospy.is_shutdown():

        data = arduino.readline()

        if "GPGGA" in data:

            current = data.split(',')

            #UTC of Position
            pub = rospy.Publisher('/UTC_of_Position',Float32,queue_size=1)
            msg = Float32()
            msg.data = float(current[1])
            pub.publish(msg)

            #Latitude
            pub = rospy.Publisher('/Latitude',Float32,queue_size=1)
            msg = Float32();
            msg.data = float(current[2]);
            pub.publish(msg);

            #North or South
            pub = rospy.Publisher('/N_or_S',Float32,queue_size=1)
            msg = String()
            msg.data = String(current[3]);
            pub.publish(msg);

            #Longitude
            pub = rospy.Publisher('/Longitude',Float32,queue_size=1)
            msg = Float32();
            msg.data = float(current[4]);
            pub.publish(msg);

            #East or West
            pub = rospy.Publisher('/E_or_W',Float32,queue_size=1)
            msg = String();
            msg.data = String(current[5]);
            pub.publish(msg);

            #GPS Quality Indicator
            pub = rospy.Publisher('/GPS_Quality_Indicator',Float32,queue_size=1)
            msg = Float32();
            msg.data = float(current[6]);
            pub.publish(msg);

            #Number of Satellites
            pub = rospy.Publisher('/Number_of_Satellites',Float32,queue_size=1)
            msg = Float32();
            msg.data = float(current[7]);
            pub.publish(msg);

            #Horizontal Dilution of Position
            pub = rospy.Publisher('/Horizontal_Dilution_of_Position',Float32,queue_size=1)
            msg = Float32()
            msg.data = float(current[8])
            pub.publish(msg)

            #Antenna Altitude 
            pub = rospy.Publisher('/Antenna_Altitude_AboveBelow_Mean_Sea_Level',Float32,queue_size=1)
            msg = Float32()
            msg.data = float(current[9])
            pub.publish(msg)

            #Meters Antenna Height
            pub = rospy.Publisher('/Meters_Antenna_Height',Float32,queue_size=1)
            msg = Float32()
            msg.data = float(current[10])
            pub.publish(msg)

            #Geoidal Seperation
            pub = rospy.Publisher('/Geoidal_Seperation',Float32,queue_size=1)
            msg = Float32()
            msg.data = float(current[11])
            pub.publish(msg)

            #Meters Geoidal Seperation
            pub = rospy.Publisher('/Meters_Geoidal_Seperation',Float32,queue_size=1)
            msg = Float32()
            msg.data = float(current[12])
            pub.publish(msg)

            #Age in Seconds
            pub = rospy.Publisher('/Age_In_Seconds_Since_Last_Update_From_Diff_Reference_Station',Float32,queue_size=1)
            msg = Float32()
            msg.data = float(current[13])
            pub.publish(msg)

            #Difference in Reference Station ID
            pub = rospy.Publisher('/Diff_Reference_Station_ID',Float32,queue_size=1)
            msg = Float32()
            msg.data = float(current[14])
            pub.publish(msg)

        if "GNRMC" in data:

            current = data.split(',');
            print(current)

            if(current[1]!=''):
                pub = rospy.Publisher('/UTC_Time',Float32,queue_size=1)
                msg = Float32()
                msg.data = float(current[1])
                rospy.logerr(msg.data)
                pub.publish(msg);

            if(current[2]!=''):
                pub = rospy.Publisher('/Positioning_Status',String,queue_size=1)
                msg = String()
                msg.data = String(current[2])
                pub.publish(msg);

            if(current[3]!=''):
                pub = rospy.Publisher('/Current_Latitude',Float32,queue_size=1)
                msg = Float32()
                msg.data = float(current[3])
                pub.publish(msg);

            if(current[4]!=''):
                pub = rospy.Publisher('/North_South_1',String,queue_size=1)
                msg = String()
                msg.data = String(current[4])
                pub.publish(msg);

            if(current[4]!=''):
                pub = rospy.Publisher('/Current_Longitude',Float32,queue_size=1)
                msg = Float32()
                msg.data = float(current[5])
                pub.publish(msg)

            if(current[5]!=''):
                pub = rospy.Publisher('/East_West_1',String,queue_size=1)
                msg = String()
                msg.data = String(current[6])
                pub.publish(msg)

            # pub = rospy.Publisher('/Speed_in_Knots',Float32,queue_size=1)
            # msg = Float32()
            # msg.data = float(current[7])
            # pub.publish(msg)

            # pub = rospy.Publisher('/True_Course',Float32,queue_size=1)
            # msg = Float32()
            # msg.data = float(current[8])
            # pub.publish(msg)

            # pub = rospy.Publisher('/Date_Stamp',Float32,queue_size=1)
            # msg = Float32()
            # msg.data = float(current[9])
            # pub.publish(msg)

            # pub = rospy.Publisher('/Variation',Float32,queue_size=1)
            # msg = Float32()
            # msg.data = float(current[10])
            # pub.publish(msg)

            # pub = rospy.Publisher('/East_West_2',String,queue_size=1)
            # msg = String()
            # msg.data = String(current[11])
            # pub.publish(msg)

            # pub = rospy.Publisher('/Checksum',Float32,queue_size=1)
            # msg = Float32
            # msg.data = float(current[12])
            # pub.publish(msg)


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass