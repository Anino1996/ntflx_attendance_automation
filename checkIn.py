import time


################################################
# Utility functions used in navigating website #
#	and performing key functions	       #
################################################

# Check if class check-in was successful
def check_logged_in(driver):
	
	# Look for the check into class link and return it if present else return None
	latest_class_card=driver.find_element_by_class_name("card-with-title")
	all_listed=latest_class_card.find_elements_by_tag_name("li")
	all_listed_text=[i.text for i in all_listed]

	if 'Check In To Class' in all_listed_text:
		target_item=next(filter(lambda x: x.text=='Check In To Class',all_listed))
		target=target_item.find_element_by_tag_name('a')
		

	else:
		target=None

	return target,all_listed_text


# Check to ensure that new page has loaded
# Check if current url is different from the saved url. 
# Wait 5 seconds to account for slower internet connections
def load_confirmed(driver, prev):
	status=False
	cnt=0
	while cnt<10 and not status:
		status= prev!=driver.current_url
		if not status:
			cnt+=1
			time.sleep(1)
	time.sleep(5)
	return status

# Locate and return check-in link and text
def find_check_in_url(driver):
	target,listed_txt=check_logged_in(driver)
	if target:
		print('Target link found')
	else:
		print(listed_txt[-1])
	return target, listed_txt[-1]


# Click on the located link
def check_into_class(target, driver):
	tries=2
	while tries>0:
		target.click()
		time.sleep(5)
		check_logged=check_logged_in(driver)
		if not check_logged[0]:
			return 'Check in successful!'
		tries-=1
	
	return "Error occurred. Check in unsuccessful!"


# Start weekly survey 
# Click on start survey button
def safe_click(target, driver):
	tries=2
	curr=driver.current_url
	while tries>0:
		print(f'Try {2-tries+1}')
		target.click()
		time.sleep(2)
		if load_confirmed(driver, curr):
			print("Survey started")
			return True
		tries-=1
	print("Survey start unsuccessful")
	return False


