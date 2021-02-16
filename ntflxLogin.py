from selenium import webdriver
from checkIn import *
import json
import os
from mailFdbck import communicate
from survey import *
# imort time

def main():
	options=webdriver.ChromeOptions()
	options.headless=True

	if os.environ['LOGNAME']=='anino1996':
		os.chdir('/Users/anino1996/Python/attendance_automation')
		DRIVER_PATH=os.path.join(os.getcwd(),'chromedriver')
		browserDriver=webdriver.Chrome(executable_path=DRIVER_PATH,options=options)
		
	else:
		os.chdir("/home/pi/Documents/attendance_automation")
		browserDriver=webdriver.Chrome(options=options)


	# DRIVER_PATH='/Users/anino1996/Python/attendance_automation/chromedriver'
	
	
	cred=json.loads(os.environ['NTFLX_LOGIN'])

	mail=cred.get('mail', None)
	pwrd=cred.get('pwrd', None)

	# browserDriver=webdriver.Chrome(executable_path=DRIVER_PATH,options=options)

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
				if 'feedback' in browserDriver.current_url:
					survey_started=start_survey(browserDriver)
					if survey_started:
						survey_fdbck=complete_survey(browserDriver)
						if survey_fdbck!='Success':
							fdbck=survey_fdbck
							communicate(fdbck)
							return 		
				check_in_element,fdbck=find_check_in_url(browserDriver)
				if check_in_element:
					fdbck=check_into_class(check_in_element, browserDriver)
			print(fdbck)
			communicate(fdbck)
				
if __name__=='__main__':
	main()
