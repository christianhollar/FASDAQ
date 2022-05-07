# FASDAQ 

## Introduction
FASDAQ is a data acquisition ROS package built by the Lafayette College FSAE Senior Design team for the Motorsports Club. The goal of the Lafayette College Motorsports Club is to build a vehicle to compete at, and ultimately win, the [Formula Hybrid](https://www.formula-hybrid.org/) racing competition. The vehicle must abide by the rules linked [here](https://drive.google.com/file/d/1o8XuRjvxqnI4e_mCsQp9KGfgsLE2E60C/view), and the competition includes three different dynamic events: the Acceleration Event, the Autocross Event, and the Endurance Event. The FASDAQ data acquisiton subsystem has been implemented into the car to help improve both driver and vehicle performance.

There are three main components to the package: [arduino code](https://github.com/christianhollar/FASDAQ/tree/main/arduino), [python nodes](https://github.com/christianhollar/FASDAQ/tree/main/nodes), and [rqt perspectives](https://github.com/christianhollar/FASDAQ/tree/main/rqt_perspective). Data is acquired from four seperate sensors: [AOS](https://github.com/christianhollar/FASDAQ/wiki/AOS-Tutorial), [GPS](https://github.com/christianhollar/FASDAQ/wiki/GPS-Tutorial), [LIDAR](https://github.com/christianhollar/FASDAQ/wiki/LIDAR-Tutorial), and [String Potentiometer](https://github.com/christianhollar/FASDAQ/wiki/String-Potentiometer-Tutorial). The arduino code is responsible for bringing sensor data to the PC which the FASDAQ package is operating on. The python nodes are responsible for organizing the data, through the use of ROS topics, so that it can be displayed or combined to for cross-sensor measurements. Lastly, perspectives are saved versions of displaying the gathered data through the use of the ROS GUI [rqt_gui](http://wiki.ros.org/rqt_gui).

The remaining code includes various [launch]() files, which allow a user to perform all of the previously mentioned processes through a single command. 

Motorsports Team Start here:  
[First Day on the Job](https://github.com/christianhollar/FASDAQ/wiki/First-Day-on-the-Job)

The rest of this README document serves as a directory for remaining wiki pages. The purpose of the wiki pages is to dive deeper into the processes included in the "First Day on the Job" tutorial.

## Sensor Tutorials:

#### Included Information:
1. Sensors & Micro-controllers Name, Image
2. Wiring
3. Sensor Capabilities
4. Sensor Measurements
5. Relevant Topics & Perspectives

- [AOS Tutorial](https://github.com/christianhollar/FASDAQ/wiki/AOS-Tutorial)  
- [GPS Tutorial](https://github.com/christianhollar/FASDAQ/wiki/GPS-Tutorial)  
- [LIDAR Tutorial](https://github.com/christianhollar/FASDAQ/wiki/LIDAR-Tutorial)
- [String Potentiometer Tutorial](https://github.com/christianhollar/FASDAQ/wiki/String-Potentiometer-Tutorial)

## Measurements & Derivation Key:

#### Included Information:
- Measurements
- 

## ROS Tutorials:

### Preview

#### Included Information:
1. Purpose of ROS Specific Structures
2. Implementation Guides
 
- [Launch File Tutorial](https://github.com/christianhollar/FASDAQ/wiki/Launch-File-Tutorial)
- [Custom Messages](https://github.com/christianhollar/FASDAQ/wiki/Custom-Messages-ROS)
- [Topics]()

## Linux Tutorials:

#### Preview
1. Purpose of linux tutorial.
2. 
- [Udev Rules Tutorial]()
- [Misc. Linux Commands]()

## Misc Tutorials:
- [Git Tutorial]()

## Lafayette Deliverables:
- [Testing Deliverable]()



