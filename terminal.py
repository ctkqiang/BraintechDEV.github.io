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

class BraintechTERMINAL(Braintech):
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
            if "USB-SERIAL CH340" in p[1] and "4" in p[0]:
                print(p[1])
                with serial.Serial("COM4", 115200, timeout=1) as ser:
                    print(ser.readline())
            elif "USB-SERIAL CH340" in p[1] and "2" in p[0]:
                print(p[1])
                with serial.Serial("COM2", 115200, timeout=1) as ser:
                    print(ser.readline())
            elif "USB-SERIAL CH340" in p[1] and "3" in p[0]:
                print(p[1])
                with serial.Serial("COM3", 115200, timeout=1) as ser:
                    print(ser.readline())
            elif "USB-SERIAL CH340" in p[1] and "4" in p[0]:
                print(p[1])
                with serial.Serial("COM4", 115200, timeout=1) as ser:
                    print(ser.readline())
            elif "USB-SERIAL CH340" in p[1] and "5" in p[0]:
                print(p[1])
                with serial.Serial("COM5", 115200, timeout=1) as ser:
                    print(ser.readline())
            elif "USB-SERIAL CH340" in p[1] and "6" in p[0]:
                print(p[1])
                with serial.Serial("COM6", 115200, timeout=1) as ser:
                    print(ser.readline())
            elif "USB-SERIAL CH340" in p[1] and "7" in p[0]:
                print(p[1])
                with serial.Serial("COM7", 115200, timeout=1) as ser:
                    print(ser.readline())
            elif "USB-SERIAL CH340" in p[1] and "8" in p[0]:
                print(p[1])
                with serial.Serial("COM8", 115200, timeout=1) as ser:
                    print(ser.readline())
            elif "USB-SERIAL CH340" in p[1] and "9" in p[0]:
                print(p[1])
                with serial.Serial("COM9", 115200, timeout=1) as ser:
                    print(ser.readline())
            elif "USB-SERIAL CH340" in p[1] and "10" in p[0]:
                print(p[1])
                with serial.Serial("COM10", 115200, timeout=1) as ser:
                    print(ser.readline())
            elif "USB-SERIAL CH340" in p[1] and "11" in p[0]:
                print(p[1])
                with serial.Serial("COM11", 115200, timeout=1) as ser:
                    print(ser.readline())
            elif "USB-SERIAL CH340" in p[1] and "12" in p[0]:
                print(p[1])
                with serial.Serial("COM12", 115200, timeout=1) as ser:
                    print(ser.readline())
            elif "USB-SERIAL CH340" in p[1] and "13" in p[0]:
                print(p[1])
                with serial.Serial("COM13", 115200, timeout=1) as ser:
                    print(ser.readline())
            elif "USB-SERIAL CH340" in p[1] and "14" in p[0]:
                print(p[1])
                with serial.Serial("COM14", 115200, timeout=1) as ser:
                    print(ser.readline())
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
    
    """
        print(help)


    def do_list(self, inp):
        ports = serial.tools.list_ports.comports()
        for port, desc, hwid in sorted(ports):
            print("$Available_Ports >>>" + "{}: {} [{}]".format(port, desc, hwid))


    def do_echo(self, inp):
        print("$OUTPUT >>> "+"{}".format(inp))

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
        print("WELCOME TO PYTHON TERMINAL")
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



BraintechTERMINAL().cmdloop()
