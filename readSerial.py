#! /usr/bin/python3

import serial
import time
import psycopg2
from insert import insert_data

#-----------------------------------------------------------------------       
def openSerial (port,baud,bytesize,parity,stopbits,timeout,xonxoff,rtscts,writetimeout,dsrdtr,interchartimeout,message,length):		
	try:
		ser = serial.Serial(port,baud,8,parity,stopbits,timeout,xonxoff,rtscts,writetimeout,dsrdtr,interchartimeout)  # open serial port   
		#ser = serial.Serial('/dev/ttyUSB1',9600, bytesize=8, stopbits=2, timeout=None, xonxoff=0, rtscts=0, dsrdtr=0)		
		time.sleep(2) # required on RPi to allow the bootloader to time out
		print (ser.portstr+" opened")       # check which port was really used
		print ("Port %s set to %d %s%s%s (%ds timeout)" % (port,baud,bytesize,parity,stopbits,timeout))
		#print ("sending '%s'"%message)     
		#ser.write(bytes(message, encoding="ascii"))      # write a string
		while True:
			s=ser.read(5)
			if(str(s,"ascii") == 'start'):
				id = int.from_bytes(ser.read(1), byteorder='big', signed=False)
				val = ser.read(2)
				volt = val[0] + val[1]*256
				volt = (float(volt)/1024)*5
				percent = volt*100/5
				percent=float(str(round(percent, 0)))		
				insert_data(id, "sensor", volt, percent)
				#print("sensor ", id, ": ", volt, "V")        
		#ser.close()             # close port
		#print ("port closed")
	except serial.SerialException:
		print("failed to open %s"%port)
		pass
   
#-----------------------------------------------------------------------
def main():
   
	#raspberrypi
	openSerial('/dev/ttyUSB1',9600,8,serial.PARITY_NONE,1,2,False,False,2,True,None,'^WHORU$',11)
	#windows
	#openSerial('COM3',9600,8,serial.PARITY_NONE,1,2,False,False,2,True,None,'^WHORU$',11)

#-----------------------------------------------------------------------
if __name__=="__main__":
	main()
