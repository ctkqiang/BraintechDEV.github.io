#!/usr/bin/env python3
######################################
# BRAINTECH PRIVATE LIMITED
# JOHN MELODY MELISSA
######################################
# यह स्क्रिप्ट John Melody द्वारा लिखा गया है।
# PYTHON में पूरी तरह  से द्वारा संचालित. सभी
# अधिकार सुरक्षित |  इस स्क्रिप्ट का कोई भी
# हिस्सा अनधिकृत पार्टी द्वारा
# पुनरुत्पादित किया जा सकता है।
######################################
from cmd import Cmd as Braintech
import serial.tools.list_ports
import serial
import os
import threading
from subprocess import Popen, PIPE
import time


class BraintechTERMINAL(Braintech):
    os.system("MODE 85, 45")
    os.system("title Braintech Serial Monitor")
    print("Copyright (C) BRAINTECH SDN BHD MALAYSIA")
    print("Type \"help\" for HELP on the usage.")

    def do_exit(self, inp):
        return True

    def do_add(self, inp):
        print("Adding '{}'".format(inp))

    def do_read_serial(self, inp):
        ports = list(serial.tools.list_ports.comports())
        for p in ports:
            if "USB-SERIAL CH340" in p[1] and "1" in p[0]:
                print(p[1])
                while 1:
                    with serial.Serial("COM1", 115200, timeout=1) as ser:
                        print(ser.readline(17))
                        time.sleep(0.1)
            elif "USB-SERIAL CH340" in p[1] and "2" in p[0]:
                print(p[1])
                while 1:
                    with serial.Serial("COM2", 115200, timeout=1) as ser:
                        print(ser.readline(17))
                        time.sleep(0.1)
            elif "USB-SERIAL CH340" in p[1] and "3" in p[0]:
                print(p[1])
                while 1:
                    with serial.Serial("COM3", 115200, timeout=1) as ser:
                        print(ser.readline(17))
                        time.sleep(0.1)
            elif "USB-SERIAL CH340" in p[1] and "4" in p[0]:
                print(p[1])
                while 1:
                    with serial.Serial("COM4", 115200, timeout=1) as ser:
                        print(ser.readline(17))
                        time.sleep(1)
            elif "USB-SERIAL CH340" in p[1] and "5" in p[0]:
                print(p[1])
                while 1:
                    with serial.Serial("COM5", 115200, timeout=1) as ser:
                        print(ser.readline(17))
                        time.sleep(0.1)
            elif "USB-SERIAL CH340" in p[1] and "6" in p[0]:
                print(p[1])
                while 1:
                    with serial.Serial("COM6", 115200, timeout=1) as ser:
                        print(ser.readline(17))
                        time.sleep(0.1)
            elif "USB-SERIAL CH340" in p[1] and "7" in p[0]:
                print(p[1])
                while 1:
                    with serial.Serial("COM7", 115200, timeout=1) as ser:
                        print(ser.readline(17))
                        time.sleep(0.1)
            elif "USB-SERIAL CH340" in p[1] and "8" in p[0]:
                print(p[1])
                while 1:
                    with serial.Serial("COM8", 115200, timeout=1) as ser:
                        print(ser.readline(17))
                        time.sleep(0.1)
            elif "USB-SERIAL CH340" in p[1] and "9" in p[0]:
                print(p[1])
                while 1:
                    with serial.Serial("COM9", 115200, timeout=1) as ser:
                        print(ser.readline(17))
                        time.sleep(0.1)
            elif "USB-SERIAL CH340" in p[1] and "10" in p[0]:
                print(p[1])
                while 1:
                    with serial.Serial("COM10", 115200, timeout=1) as ser:
                        print(ser.readline(17))
                        time.sleep(0.1)
            elif "USB-SERIAL CH340" in p[1] and "11" in p[0]:
                print(p[1])
                while 1:
                    with serial.Serial("COM11", 115200, timeout=1) as ser:
                        print(ser.readline(17))
                        time.sleep(0.1)
            elif "USB-SERIAL CH340" in p[1] and "12" in p[0]:
                print(p[1])
                while 1:
                    with serial.Serial("COM12", 115200, timeout=1) as ser:
                        print(ser.readline(17))
                        time.sleep(0.1)
            elif "USB-SERIAL CH340" in p[1] and "13" in p[0]:
                print(p[1])
                while 1:
                    with serial.Serial("COM13", 115200, timeout=1) as ser:
                        print(ser.readline(17))
                        time.sleep(0.1)
            elif "USB-SERIAL CH340" in p[1] and "14" in p[0]:
                print(p[1])
                while 1:
                    with serial.Serial("COM14", 115200, timeout=1) as ser:
                        print(ser.readline(17))
                        time.sleep(0.1)
            else:
                print("Try Again!")

    def do_clear(self, inp):
        os.system("cls")

    def do_help(self, inp):
        help = """
    +---------------------------------------------
    | COMMAND   |             USAGE              |
    +--------------------------------------------- 
    help                    --- Help Menu
    clear                   --- Clear screen
    read_serial             --- Read Serial data
    add                     --- Cloning
    echo                    --- Print String
    list                    --- List available ports
    exit                    --- Exit
    credit                  --- Credit / Copyright
    colour                  --- Colour of the Terminal
    fit                     --- Auto Adjust Window Size
    powershell              --- Activate Powershell
    python                  --- Activate iPython shell
    arduinoHOW              --- Arduino Source code for
                                serial communication
    mind_data               --- About Mind Data Module
    mind_data_protocol      --- Braintech Mind Data
                                protocol. 
    """
        print(help)


    def do_list(self, inp):
        ports = serial.tools.list_ports.comports()
        for port, desc, hwid in sorted(ports):
            print("$Available_Ports >>>" + "{}: {} [{}]".format(port, desc, hwid))


    def do_echo(self, inp):
        print("{}".format(inp))

    def do_credit(self, inp):
        credit = """  
 +---------------------------------------------------+
 | Braintech Brainwave Monitor CLI Community Edition |
 | Copyright (C) BRAINTECH SDN BHD MALAYSIA          |
 | POWERED BY PYTHON                                 |
 +---------------------------------------------------+
 | Developer Email:  John@braintechgroup.com         |
 | Donate : https://www.paypal.me/johnmelody         |
 +-------------------------- -------------------------+ 
        """
        print(credit)

    def do_colour(self, inp):
        os.system("color {}".format(inp))

    def do_fit(self, inp):
        os.system("MODE 90, 40")

    def do_powershell(self, inp):
        os.system("powershell")

    def do_braintech(selfself, inp):
        import credit as braintech
        return braintech()

    def do_python(self, inp):
        print("WELCOME TO PYTHON TERMINAL \n")
        os.system("ipython")

    def do_arduinoHOW(self, inp):
        arduinocode = """
const int analogInPin = A0;  // Analog input pin that the potentiometer is attached to
int sensorValue = 0;        // value read from the pot
void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(115200);
}
void loop() {
  // read the analog in value:
  sensorValue = analogRead(analogInPin);
  // print the results to the serial monitor:
  Serial.println(sensorValue);
  // wait 2 milliseconds before the next loop
  delay(5);
}
"""
        print(arduinocode)

    def do_mind_data(self, inp):
        #import webview
        #window = webview.create_window('Braintech Mind Data Module', 'http://www.mindatabci.com/en/index.aspx')
        #webview.start()
        os.system("start http://www.mindatabci.com/en/index.aspx")

    def do_mind_data_protocol(self, inp):
        info = """
This is a 2-Channel EEG Module;
This Module is used to collect EEG data for: 
16-bits time domain signal conversion;
{information} : {
        3.3v; (built-in 50hz filter circuit)
        serial OUTPUT config {
            check digit: NONE;
            Data bit: 8-bits;
            Stop bit: 1-bit
            BAUD rate: 115200
            }
    }
1: sync0;          # synchronisation byte 1 = 0xa5   ()
2: sync1;          # synchronisation byte 2 = 0x5a
3: version;        # version number = 2
4: count;          # packet counter. Increases by 1 each packet.
5: Chn1high        # channel 1 high byte
6: Chn1low         # channel 2 low byte
7: Chn2high        # channel 2 high byte
8: Chn2low         # ...
9: Chn3high
10: Chn3low
11: Chn4high
12: Chn4low
13: Chn5high
14: Chn5low
15: Chn6high
16: Chn6low        # channel 6 low byte
17: switches;      # State of PD5 to PD2, in bits 3 to 0.
====================================================
A5 5A 02 39 02 33 01 EB 02 22 01 B3 02 00  02 00 0F
====================================================
|  |  |  |   |     |     |     |     |     |
|  |  |  |   |     |     |     |     |     +-------- CH6
|  |  |  |   |     |     |     |     +-------------- CH5
|  |  |  |   |     |     |     +-------------------- CH4
|  |  |  |   |     |     +-------------------------- CH3
|  |  |  |   |     +-------------------------------- CH2
|  |  |  |   +-------------------------------------- CH1
|  |  |  +------------------------------------------ Packet counter. +=1
|  |  +--------------------------------------------- Version = {2}
|  +------------------------------------------------ Synchronisation byte 2 = 0x5a
+--------------------------------------------------- Synchronisation byte 1 = 0xa5 
        """
        print(info)

BraintechTERMINAL().cmdloop()
