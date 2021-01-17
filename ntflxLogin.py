from selenium import webdriver
from checkIn import *
import json
import os
from mailFdbck import communicate
# import time

def main():

	os.chdir("/home/pi/Documents/attendance_automation")

#DRIVER_PATH='/Users/anino1996/Python/attendance_automation/chromedriver'
	options=webdriver.ChromeOptions()
	options.headless=True

	with open('credentials.json', 'r') as file:
		cred=json.load(file)

	mail=cred.get('mail', None)
	pwrd=cred.get('pwrd', None)

	browserDriver=webdriver.Chrome(options=options)

	browserDriver.get("https://www.bootcampspot.com")
	
	if browserDriver.current_url[-5:]=="login":
		emailElement=browserDriver.find_element_by_name("emailAddress")
		emailElement.send_keys(mail)
		passElement=browserDriver.find_element_by_name("password")
		passElement.send_keys(pwrd)
		btn=browserDriver.find_element_by_tag_name("button")
		if btn.text=="SIGN IN":
			prev=browserDriver.current_url
			btn.click()
		
	
			if not load_confirmed(browserDriver, prev):
				fdbck='Login Failed!'
				
				
			
			else:
				print("Login Successful!")
				check_in_element,fdbck=find_check_in_url(browserDriver)
				if check_in_element:
					fdbck=check_into_class(check_in_element, browserDriver)
					
			communicate(fdbck)
				
if __name__=='__main__':
	main()
