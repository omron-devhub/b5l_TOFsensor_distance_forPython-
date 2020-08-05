------------------------------------------------------------
 TOF-Sensor Sample code for get result.  (for Python)
------------------------------------------------------------

(1) Contents
  This code provides TOF-Sensor Python sample code for get result.
  With this sample code, you can execute "Start Measurement" , "Stop Measurement" , "Get Result".

(2) File description
  The following files exist in the TOFSensorSampleGetResult/ folder.

    TOFSensorSampleGetResult.py         Sample code main
    tof_serial.py                       Serial Port send/receive class
    connect_usb0.sh                     Shell script to connect /dev/ttyUSB0(only for Ubuntu18)

(3) Environment for this sample code
  The sample code is coded to run in Python2.7 environment on both Windows10 and Ubuntu18.
  A module named "pyserial" is needed to run this sample code.

(4）Prepare to execute sample code

  [Setting /dev/ttyUSB0]

  Type as follow lines in shell.

    sudo modprobe usbserial vendor=0x0590 product=0x00ca[Enter]
    sudo chmod o+wr /dev/ttyUSB0[Enter

  Or give execute permission to the following file and execute it.

    connect_usb0.sh

(5）Executing sammple code

  Move to the folder of sample code in shell, 
  and type following line to execute sammple code.

  python TOFSensorSampleGetResult.py[Enter]
  (Refer to "ExecutableFileDescription.txt" for detail information)

[NOTES ON USAGE]
* This sample code and documentation are copyrighted property of OMRON Corporation
* This sample code does not guarantee proper operation
* This sample code is distributed in the Apache License 2.0.

----
OMRON Corporation 
Copyright 2020 OMRON Corporation, All Rights Reserved.
