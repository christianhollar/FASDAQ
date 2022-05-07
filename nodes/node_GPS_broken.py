#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float32
from std_msgs.msg import String
import serial

def talker():
    
    arduino = serial.Serial('/dev/ttyACM0',115200)
    rospy.init_node('arduino_node_1', anonymous=True)
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
            # pub = rospy.Publisher('/N_or_S',Float32,queue_size=1)
            # msg = String()
            # msg.data = String(current[3]);
            # pub.publish(msg);

            #Longitude
            pub = rospy.Publisher('/Longitude',Float32,queue_size=1)
            msg = Float32();
            msg.data = float(current[4]);
            pub.publish(msg);

            #East or West
            # pub = rospy.Publisher('/E_or_W',Float32,queue_size=1)
            # msg = String();
            # msg.data = String(current[5]);
            # pub.publish(msg);

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

        # if "GPRMC" in data:

        #     current = data.split(',');

        #     pub = rospy.Publisher('/Time_Stamp')
        #     msg = Float32()
        #     msg.data = float(current[1])
        #     pub.publish(msg);

        #     pub = rospy.Publisher('/Time_Validity')
        #     msg = Float32()
        #     msg.data = float(current[2])
        #     pub.publish(msg);

        #     pub = rospy.Publisher('/Current_Latitude')
        #     msg = Float32()
        #     msg.data = float(current[3])
        #     pub.publish(msg);

        #     pub = rospy.Publisher('/North_South_1')
        #     msg = String()
        #     msg.data = String(current[4])
        #     pub.publish(msg);

        #     pub = rospy.Publisher('/Current_Longitude')
        #     msg = Float32()
        #     msg.data = float(current[5])
        #     pub.publish(msg)

        #     pub = rospy.Publisher('/East_West_1')
        #     msg = String()
        #     msg.data = String(current[6])
        #     pub.publish(msg);

        #     pub = rospy.Publisher('/Speed_in_Knots')
        #     msg.data = current[7];
        #     pub.publish(msg);

        #     pub = rospy.Publisher('/True_Course')
        #     msg.data = current[8];
        #     pub.publish(msg);

        #     pub = rospy.Publisher('/Date_Stamp')
        #     msg.data = current[9];
        #     pub.publish(msg);

        #     pub = rospy.Publisher('/Variation')
        #     msg.data = current[10];
        #     pub.publish(msg);

        #     pub = rospy.Publisher('/East_West_2')
        #     msg.data = current[11];
        #     pub.publish(msg);

        #     pub = rospy.Publisher('/Checksum')
        #     msg.data = current[12];
        #     pub.publish(msg);


        # if "GPGSV" in data:
        #     current = data.split(',');

        #     pub = rospy.Publisher('/Checksum')
        #     msg.data = current[1];
        #     pub.publish(msg);

        #     pub = rospy.Publisher('/Checksum')
        #     msg.data = current[2];
        #     pub.publish(msg);

        #     pub = rospy.Publisher('/Checksum')
        #     msg.data = current[3];
        #     pub.publish(msg);

        #     pub = rospy.Publisher('/SV1_PRN')
        #     msg.data = current[4];
        #     pub.publish(msg);

        #     pub = rospy.Publisher('/SV1_Elevation')
        #     msg.data = current[5];
        #     pub.publish(msg);

        #     pub = rospy.Publisher('/SV1_Azimuth')
        #     msg.data = current[6];
        #     pub.publish(msg);

        #     pub = rospy.Publisher('/SV1_SNR')
        #     msg.data = current[7];
        #     pub.publish(msg);

        #     pub = rospy.Publisher('/SV2_PRN')
        #     msg.data = current[8];
        #     pub.publish(msg);

        #     pub = rospy.Publisher('/SV2_Elevation')
        #     msg.data = current[9];
        #     pub.publish(msg);

        #     pub = rospy.Publisher('/SV2_Azimuth')
        #     msg.data = current[10];
        #     pub.publish(msg);

        #     pub = rospy.Publisher('/SV2_SNR')
        #     msg.data = current[11];
        #     pub.publish(msg);

        #     pub = rospy.Publisher('/SV3_PRN')
        #     msg.data = current[12];
        #     pub.publish(msg);

        #     pub = rospy.Publisher('/SV3_Elevation')
        #     msg.data = current[13];
        #     pub.publish(msg);

        #     pub = rospy.Publisher('/SV3_Azimuth')
        #     msg.data = current[14];
        #     pub.publish(msg);

        #     pub = rospy.Publisher('/SV3_SNR')
        #     msg.data = current[15];
        #     pub.publish(msg);

        #     pub = rospy.Publisher('/SV4_PRN')
        #     msg.data = current[16];
        #     pub.publish(msg);

        #     pub = rospy.Publisher('/SV4_Elevation')
        #     msg.data = current[17];
        #     pub.publish(msg);

        #     pub = rospy.Publisher('/SV4_Azimuth')
        #     msg.data = current[18];
        #     pub.publish(msg);

        #     pub = rospy.Publisher('/SV4_SNR')
        #     msg.data = current[19];
        #     pub.publish(msg);        

        # rospy.logerr(data)
        # data = data.strip()
        # data = data.split('\t')
        # print(data)
        # floatdata = []
        # if(len(data)>0):
        #     for k in range(0,len(data)):
        #         if(data[k] is not ''):
        #             try:
        #                 floatdata.append(float(data[k]))
        #             except:
        #                 pass

        #     #set first one to our message
        #     msg = Float32()
        #     if(len(floatdata)>0):
        #         msg.data = floatdata[0]

        #         # rospy.loginfo(hello_str)
        #         pub.publish(msg)
        # rate.sleep()

if __name__ == '__main__':
    try:

        talker()
    except rospy.ROSInterruptException:
        pass
