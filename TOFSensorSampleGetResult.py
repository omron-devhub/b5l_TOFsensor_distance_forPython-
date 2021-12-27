# -*- coding: UTF-8 -*-
# ---------------------------------------------------------------------------
# Copyright 2020  OMRON Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ---------------------------------------------------------------------------

#----------------------------------------------------
# Environment Ubuntu
#   Ubuntu 18.04.3 LTS
#   pyserial (3.4)
#   Python 2.7.15+ (default, Oct  7 2019, 17:39:04) 
#----------------------------------------------------

#-------------------------------------------------------
# Environment Windows10
#   Windows 10
#   pyserial (3.4)
#   Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:22:17) [MSC v.1500 32 bit (Intel)] on win32
#-------------------------------------------------------

import serial
import tof_serial as TS

def main():

    error_count = 0
    all_count = 0
    nodata_timeout = {"80":1.0, "81":1.0, "82":1.0}
    
    print "Enter send command No. and press enter key.:"
    print "80:Start measurement"
    print "81:Stop measurement"
    print "82:Get result"
    print "RR:Get result(repeat) (Stop by Ctrl + C)"
    print "XX:Exit"

    # Input send command
    input_send_cmd_all = raw_input()
    input_send_cmd = input_send_cmd_all[0:2]

    print ""
    print "Command entered:" + (input_send_cmd)

    send_cmd = ""

    # Command branch 
    if input_send_cmd == "80":
        print "Send 80:Start measurement command"
        send_cmd = "FE-80-00-00"
    if input_send_cmd == "81":
        print "Send 81:Stop measurement command"
        send_cmd = "FE-81-00-00"
    if input_send_cmd == "82":
        print "Send 82:Get result command"
        send_cmd = "FE-82-00-01-00"
    if input_send_cmd == "RR":
        print "RR:Send get result(repeat) command"
        send_cmd = "FE-82-00-01-00"
    if input_send_cmd == "XX":
        print "XX:Exit"
        send_cmd = ""

    ser = TS.tof_serial()

    time_nodata_timeout = nodata_timeout.get(input_send_cmd)            
    if time_nodata_timeout == None :    # could not find command
        time_nodata_timeout = 10        # 10 s

    # Transmission / reception processing
    try:
        if send_cmd == "":
            print "No transmission."
        else:
            #ser = TS.tof_serial()
            if input_send_cmd == "RR":
                while True:
                    print "Send data:" + send_cmd
                    ser.send_command(send_cmd)
                    
                    input_send_cmd_from_send_data = send_cmd[3:5]
                    time_nodata_timeout = nodata_timeout.get(input_send_cmd_from_send_data) # No data receivede timeout value            
                    if time_nodata_timeout == None :    # could not find command
                        time_nodata_timeout = 10        # 10 s
                    
                    result = ser.receive_command(time_nodata_timeout)
                    data = ser.log_shape(False)
                    print "Receive data:" + data

                    if result != 0:
                        error_count += 1
                        print "Receive Error! No." + str(result)
                        line = ser.receive_garbage_command()
                    
                    all_count += 1
                    print "error / all = " + str(error_count) + " / " + str(all_count)
                    print ""
                        
            else:
                time_nodata_timeout = nodata_timeout.get(input_send_cmd)    # No data receivede timeout value            
                if time_nodata_timeout == None :    # could not find command
                    time_nodata_timeout = 10        # 10 s
                
                print "Send data:" + send_cmd
                ser.send_command(send_cmd)
                result = ser.receive_command(time_nodata_timeout)
                
                data = ""
                if input_send_cmd == "82":
                    data = ser.log_shape(False)
                else:
                    data = ser.log_shape(True)
                print "Receive data:" + data
    except KeyboardInterrupt:
        print "Ctrl + C:KeyboardInterrupt"
        input_send_cmd = "XX"

    # Delete buffer
    if input_send_cmd == "XX":
        line = ser.receive_garbage_command()

    print "Finished."


#-------------------------------------------------------
# Execute main
#   input:  none
#   return: none
#-------------------------------------------------------
if __name__ == '__main__':
    main()

