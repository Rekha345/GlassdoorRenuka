import time
from Data import reading_objects
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# path=r"C:\Users\Eerumalla Renuka\Downloads\chromedriver_win32\chromedriver.exe"
# driver = webdriver.Chrome(path)
# driver.get("https://www.glassdoor.co.in/member/home/index.htm")
# driver.maximize_window()
# driver.implicitly_wait(30)
salary=reading_objects.read_locators()
class salaries:
    def __init__(self,driver):
        self.driver = driver
    def email_enter(self,data_):
        # time.sleep(3)
        self.driver.find_element(*salary['email_enter']).send_keys(data_[0])
        # time.sleep(5)
    def continue_button(self):
        self.driver.find_element(*salary['continue_button']).click()
        # time.sleep(2)
    def password_text(self,data_):
        self.driver.find_element(*salary['password_text']).send_keys(data_[1])
        # time.sleep(2)
    def submit_button(self):
        self.driver.find_element(*salary['submit_button']).click()
        time.sleep(2)
    def salary_click(self):
        self.driver.find_element(*salary['salary_click']).click()
        time.sleep(2)
    def job_title(self,data_):
        self.driver.find_element(*salary['job-title']).send_keys(data_[2])
        # time.sleep(2)
    def search_button(self):
        self.driver.find_element(*salary['search_button']).click()
        # time.sleep(2)
    def review_button(self):
        self.driver.find_element(*salary['review_button']).click()
        # time.sleep(2)
    def radio_button(self):
        self.driver.find_element(*salary['radio_button']).click()
        # time.sleep(2)

    def Rekha(self,data_):
        self.driver.find_element(*salary['Rekha']).send_keys(data_[3])
        # time.sleep(2)

    def suggession_s(self):
        self.driver.find_element(*salary['suggession_s']).click()
        # time.sleep(2)
    def next_button(self):
        self.driver.find_element(*salary['next_button']).click()
        # time.sleep(2)
    def year_s(self):
        self.driver.find_element(*salary['year_s']).click()
        # time.sleep(2)
    def monthl_y(self):
        self.driver.find_element(*salary['monthl_y']).click()
        # time.sleep(2)
    def salar_y(self,data_):
        self.driver.find_element(*salary['salary_y']).send_keys(data_[4])
        # time.sleep(2)
    def country_rupees(self):
        self.driver.find_element(*salary['country_rupees']).click()
        # time.sleep(2)
    def country(self):
        self.driver.find_element(*salary['country']).click()
        # time.sleep(2)
    def years(self):
        self.driver.find_element(*salary['years']).click()
        # time.sleep(2)
    def monthly(self):
        self.driver.find_element(*salary['monthly']).click()
        # time.sleep(2)
    def bonus(self,data_):
        self.driver.find_element(*salary['bonus']).send_keys(data_[5])
        # time.sleep(2)
    def stocks(self,data_):
        self.driver.find_element(*salary['stocks']).send_keys(data_[6])
        # time.sleep(2)
    def profits(self,data_):
        self.driver.find_element(*salary['profits']).send_keys(data_[7])
        # time.sleep(2)
    def sales(self,data_):
        self.driver.find_element(*salary['sales']).send_keys(data_[8])
        # time.sleep(2)
    def tips(self,data_):
        self.driver.find_element(*salary['tips']).send_keys(data_[9])
        # time.sleep(2)
    def employer(self):
        employers_name = self.driver.find_element(*salary['employer'])
        obj_ename = ActionChains(self.driver)
        obj_ename.double_click(employers_name).perform()
        obj_ename.send_keys_to_element(employers_name,' Capgemini').perform()
        # time.sleep(2)
    def capgemini(self):
        suggestion = self.driver.find_element(*salary['capgemini'])
        obj_sugg = ActionChains(self.driver)
        obj_sugg.move_to_element(suggestion).perform()
        obj_sugg.click(suggestion).perform()
    def  joblevel(self,data_):
        self.driver.find_element(*salary['joblevel']).send_keys(data_[10])
        # time.sleep(2)
    def number(self,data_):
        self.driver.find_element(*salary['number']).send_keys(data_[11])
        # time.sleep(2)
    def numbers(self,data_):
        self.driver.find_element(*salary['numbers']).send_keys(data_[12])
        # time.sleep(2)
    def  location(self):
        location_name = self.driver.find_element(*salary['location'])
        obj_ename = ActionChains(self.driver)
        obj_ename.double_click(location_name).perform()
        obj_ename.send_keys_to_element(location_name, ' Hyderabad').perform()
        # time.sleep(2)

    def Hyderabad(self):
        suggestion = self.driver.find_element(*salary['Hyderabad'])
        obj_sugg = ActionChains(self.driver)
        obj_sugg.move_to_element(suggestion).perform()
        obj_sugg.click(suggestion).perform()

    def select(self):
        self.driver.find_element(*salary['select']).click()
        # time.sleep(2)

    def fulltime(self):
        self.driver.find_element(*salary['fulltime']).click()
        # time.sleep(2)

# lp=salaries(driver)
# lp.email_enter()
# lp.continue_button()
# lp.password_text()
# lp.submit_button()
# lp.salary_click()
# lp.job_title()
# lp.search_button()
# lp.review_button()
# lp.radio_button()
# lp.Rekha()
# lp.suggession_s()
# lp.next_button()
# lp.year_s()
# lp.monthl_y()
# lp.salar_y()
# lp.country_rupees()
# lp.country()
# lp.years()
# lp.monthly()
# lp.bonus()
# lp.stocks()
# lp.profits()
# lp.sales()
# lp.tips()
# lp.employer()
# lp.capgemini()
# lp.joblevel()
# lp.number()
# lp.numbers()
# lp.location()
# lp.Hyderabad()
# lp.select()
# lp.fulltime()