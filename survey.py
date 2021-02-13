import random
from checkIn import load_confirmed
id_range_radio=(212,221)
choices=['4','5']
id_txt_dict={'221': "Great learning experience, knowledgeable teachers", '222':"Weekend sessions, Office hours and breakout rooms"}
id_radio_dict={str(i):random.choice(choices) for i in range(*id_range_radio)}
id_radio_dict['213']='3'

def start_survey(driver):
	if 'feedback' in driver.current_url:
		btn=driver.find_element_by_tag_name('button')
		click_state=safe_click(btn, driver)
		return click_state

def complete_survey(driver):
	for id in id_radio_dict:
		button=driver.find_element_by_id(f'{id}-{id_radio_dict.get(id, "4")}')
		button.click()

	for id in id_txt_dict:
		field=driver.find_element_by_id(id)
		field.send_keys(id_txt_dict[id])

	submission=driver.find_element_by_tag_name('button')
	prev=driver.current_url
	if submission.text!='SUBMIT FEEDBACK':
		btns=driver.find_elements_by_tag_name('button')
		submission=next(filter(lambda x:x.text=='SUBMIT FEEDBACK'), btns)
		submission.click()

	submission.click()
	complete_status=load_confirmed(driver, prev)
	print("Survey completed" if complete_status else f"Survey could not be completed, please try manually by visiting {prev}")

	return 'Success' if complete_status else f"Survey could not be completed, please try manually by visiting {prev}"

