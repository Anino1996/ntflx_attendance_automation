
import time
def check_logged_in(driver):
	latest_class_card=driver.find_element_by_class_name("card-with-title")
	all_listed=latest_class_card.find_elements_by_tag_name("li")
	all_listed_text=[i.text for i in all_listed]

	if 'Check In To Class' in all_listed_text:
		target=next(filter(lambda x: x.text=='Check In To Class',all_listed))
		
		return target,all_listed_text

	else:
		return None,all_listed_text

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

def find_check_in_url(driver):
	target,listed_txt=check_logged_in(driver)
	if target:
		print('Target link found')
	else:
		print(listed_txt[-1])
	return target


def check_into_class(target, driver):
	target.click()
	time.sleep(5)
	check_logged=check_logged_in(driver)
	if not check_logged[0]:
		print("Check in successful")
	
	else:
		print("Error occurred. Check in unsuccessful!")




