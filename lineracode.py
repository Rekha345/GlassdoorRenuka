import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
path=r'C:\Users\Eerumalla Renuka\Downloads\chromedriver_win32\chromedriver.exe'
driver=webdriver.Chrome(path)
driver.get("https://www.glassdoor.co.in/member/home/index.htm")
driver.implicitly_wait(30)
driver.maximize_window()
#email
driver.find_element("xpath","//input[@title='Enter Email']").send_keys("sarveshkulkarni9545@gmail.com")
time.sleep(2)

#countinue button
driver.find_element("xpath","//button[@name='submit']").click()
time.sleep(2)


#password
driver.find_element("id","inlineUserPassword").send_keys("Sarveshbk@8")
time.sleep(2)

#submit button
driver.find_element("xpath",'//button[@type="submit"]').click()
time.sleep(2)
#
#salary
driver.find_element("xpath","(//span[@class='css-2etp8b evpplnh1'])[6]").click()
time.sleep(2)
#
#job title
driver.find_element("xpath","//input[@id='KeywordSearch']").send_keys("Data analyst")
time.sleep(2)
#
#search button
driver.find_element("xpath","//button[@type='submit']").click()
time.sleep(2)
#
#add review button
driver.find_element("xpath","//span[text()='Add Review or Salary']").click()
time.sleep(2)
#
#radio button
driver.find_element("xpath","(//div[@class='radioButtonBox'])[2]").click()
time.sleep(2)
#
#Rekha
driver.find_element("xpath","//input[@class='css-eyudwk e1h5k8h92']").send_keys("Data analyst")
time.sleep(2)
#
#suggessions
driver.find_element("xpath","//ul[@class='suggestions down']").click()
time.sleep(2)
#
#
#next button
driver.find_element("xpath","//span[@class='css-2etp8b evpplnh1']").click()
time.sleep(2)
#
# #year
driver.find_element('xpath',"//div[text()='Yearly']").click()
time.sleep(2)

#monthly
driver.find_element("xpath","//span[text()='Monthly']").click()
time.sleep(2)

#salary
driver.find_element("xpath","//input[@class='css-68nvdr e1h5k8h92']").send_keys("10000")
time.sleep(2)

#country rupees
driver.find_element("xpath","(//div[@class='selectedLabel'])[2]").click()
time.sleep(2)

#country
driver.find_element("xpath","//span[text()='Afghan Afghani (AFN)']").click()
time.sleep(2)

#year
driver.find_element("xpath","(//div[@class='selectedLabel'])[3]").click()
time.sleep(2)

#monthly
driver.find_element("xpath","(//span[text()='Monthly'])[2]").click()
time.sleep(2)

#bonus
driver.find_element("xpath","//input[@name='cashBonusAmount']").send_keys("100")
time.sleep(2)

#stock
driver.find_element("xpath","//input[@name='stockBonusAmount']").send_keys("1000")
time.sleep(2)

#profit
driver.find_element("xpath","//input[@name='profitSharingAmount']").send_keys("100")
time.sleep(2)

#sales
driver.find_element("xpath","//input[@id='salesCommissionAmount']").send_keys("10000")
time.sleep(2)

#tips
driver.find_element("xpath","//input[@id='tipsAmount']").send_keys("1200")
time.sleep(2)

#employer
employers_name = driver.find_element("xpath","(//div[@class=' css-j7qwjs ew8s0qn0'])[5]")
obj_ename = ActionChains(driver)
obj_ename.double_click(employers_name).perform()
obj_ename.send_keys_to_element(employers_name,' Capgemini').perform()
time.sleep(2)

#capgemini
suggestion = driver.find_element("xpath","//ul[@class='suggestions down']")
obj_sugg = ActionChains(driver)
obj_sugg.move_to_element(suggestion).perform()
obj_sugg.click(suggestion).perform()

#joblevel
driver.find_element("xpath","//input[@id='jobLevelInput']").send_keys("L1")
time.sleep(2)

#number
driver.find_element("xpath","//input[@type='number']").send_keys("1")
time.sleep(2)

# numbers
driver.find_element("xpath","(//input[@type='number'])[2]").send_keys("1")
time.sleep(2)

#location
location_name = driver.find_element("xpath","(//input[@class='css-eyudwk e1h5k8h92'])[6]")
obj_ename = ActionChains(driver)
obj_ename.double_click(location_name).perform()
obj_ename.send_keys_to_element(location_name,' Hyderabad').perform()
time.sleep(2)

#Hyderabad
suggestion = driver.find_element("xpath","(//ul[@class='suggestions down'])[3]")
obj_sugg = ActionChains(driver)
obj_sugg.move_to_element(suggestion).perform()
obj_sugg.click(suggestion).perform()

#select
driver.find_element("xpath","//div[@class='css-47sx24 egu3u860']").click()
time.sleep(2)

#full time
driver.find_element("xpath","//span[text()='Full Time']").click()
time.sleep(2)


