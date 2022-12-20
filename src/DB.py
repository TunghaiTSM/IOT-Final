# import MySQLdb
import mysql.connector
import boto3
from mysql.connector.locales.eng import client_error
# import pymysql

class AWS_DB:
	username = "admin"
	password = "tL738x7BX9RqWL6"
	host = "mqtt.cv04k5yhpw98.us-east-1.rds.amazonaws.com"
	port = 3306
	dbname = "MQTT"
	tbname = "identify"
	__description = "Sent from my RPI 3."

	def __init__ (self):
		self.dbconnection = mysql.connector.connect(host = self.host, 
								user = self.username, 
								password = self.password, 
								database = self.dbname)
		self.query = self.dbconnection.cursor ()

	def write_data (self, user, photo):
		cmd = "INSERT INTO " + self.tbname + "(username, photo) VALUES ('" + str (user) + "','" + str (photo)  + "');"
#print (cmd)
		self.query.execute (cmd)
		#print (self.query.fetchall ())
#while (1):
		self.dbconnection.commit ()
		self.query.execute("SELECT * FROM identify;")
		#print (self.query.fetchall ())

		

	def __del__ (self):
		#print ("Cleaning up...")
		self.dbconnection.close ()

# AWS_DB().write_data("Talen", "HAHAHAHAHAHAHAHAHAHA")
