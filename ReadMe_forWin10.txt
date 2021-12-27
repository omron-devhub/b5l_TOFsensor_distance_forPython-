------------------------------------------------------------
 TOF-Sensor Sample code for get result.  (for Python)
------------------------------------------------------------

(1) Contents
  This code provides TOF-Sensor Python sample code for get result.
  With this sample code, you can execute "Start Measurement" , "Stop Measurement" and "Get Result" .

  Note:This sample code is made for code reference.
       The response data of Get result command can't be output as file.
       It is possible to display response data in screen,
       if the code of TOFSensorSampleGetResult.py is modified as follows, but output speed is very slow.
           Line 97 : data = ser.log_shape(False)　⇒　data = ser.log_shape(True)
           Line 120 :  ser.log_shape(False)　⇒　data = ser.log_shape(True)
       
       For checking performance, please download evaluation software from following URL and use it.
       https://components.omron.com/sensors/displacement-sensors_ranging-sensors/3D-TOF-sensor-module/B5L_licence

(2) File description
  The following files exist in the TOFSensorSampleGetResult/ folder.

    TOFSensorSampleGetResult.py         Sample code main
    tof_serial.py                       Serial Port send/receive class
    connect_usb0.sh                     Shell script to connect /dev/ttyUSB0(only for Ubuntu18)

(3) Environment for this sample code
  The sample code is coded to run in Python2.7 environment on both Windows10 and Ubuntu18.
  A module named "pyserial" is necessary to run this sample code.

(4）Executing sammple code
  Move to the TOFSensorSampleGetResult/ folder by command prompt or power shell, 
  and type following line to execute sammple code.

    python TOFSensorSampleGetResult.py[Enter]
    (Refer to "ExecutableFileDescription.txt" for detail information.)

[NOTES ON USAGE]
* This sample code and documentation are copyrighted property of OMRON Corporation
* This sample code does not guarantee proper operation
* This sample code is distributed in the Apache License 2.0.

----
OMRON Corporation 
Copyright 2020-2021 OMRON Corporation, All Rights Reserved.
