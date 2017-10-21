import serial

def atoi(s):
    rtr=0
    for c in s:
        rtr=rtr*10 + ord(c) - ord('0')

    return rtr

ser = serial.Serial('/dev/ttyUSB0',9600, bytesize=8, stopbits=2, timeout=None, xonxoff=0, rtscts=0, dsrdtr=0)

while True:
	leitura = ser.read(5)
	if(leitura == 'start'):
		id = ord(ser.read(1))
		val = ser.read(2)
		volt = ord(val[0]) + ord(val[1])*256
		volt = (float(volt)/1024)*5		
		print "sensor ", id, ": ", volt, "V"

ser.close
