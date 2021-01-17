import smtplib
import os
import datetime

def adminAlert(fdbck):
	server=smtplib.SMTP("smtp.gmail.com",587)
	server.starttls()
	server.ehlo()

	server.login("oforiaalbert@gmail.com","Pythonist@96")
	message=f"From: Netflix Bootcamp Login\r\nTo:anino1996.ao@gmail.com\r\nSubject: Login Attempted\r\n\r\n Hello Anino,\nAn automated class check-in just completed.\n Result: {fdbck}\n\n"
	server.sendmail("oforiaalbert@gmail.com","anino1996.ao@gmail.com",message)
	server.close()


def logData(fdbck):
	old=''
	if 'loginLogs.log' in os.listdir('/home/pi/Documents/logs'):
		with open('/home/pi/Documents/logs/loginLogs.log','r') as file:
			old=file.read()
	with open('/home/pi/Documents/logs/loginLogs.log','w') as file:
		file.write(f'{datetime.datetime.now()} - {fdbck}\n{old}')

def communicate(fdbck):
	adminAlert(fdbck)
	logData(fdbck)
