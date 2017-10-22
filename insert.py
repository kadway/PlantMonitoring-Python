#!/usr/bin/python
 
import psycopg2
from datetime import datetime as timestamp
from config import config
 
def insert_data(sensor_id, alias, voltage, percent):
	conn = None
	vendor_id = None
	try:
		# read database configuration
		params = config()
		# connect to the PostgreSQL database
		conn = psycopg2.connect(**params)
		# create a new cursor
		cur = conn.cursor()
		# execute the INSERT statement
		# {:%Y-%m-%d %H:%M:%S}
		time=timestamp.now()
		cur.execute("INSERT INTO soil VALUES (%s,%s,%s,%s,%s);", (time,sensor_id,alias,voltage,percent))	
		# commit the changes to the database
		conn.commit()
		#print added values
		#cur.execute('select * from people')
		#results = cur.fetchall()
		#for result in results:
		#	print(result)
		# close communication with the database
		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
	return
