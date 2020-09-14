from selenium import webdriver
from time import sleep
from robot.libraries.DateTime import get_current_date
from datetime import datetime, timedelta
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from readProperties import ReadConfig

driver= webdriver.Chrome()

driver.set_page_load_timeout(15)
driver.maximize_window()
baseURL=ReadConfig.getBaseURL()
userName=ReadConfig.getUserName()
userPass=ReadConfig.getUserPass()
#print("This line will be printed.")

now =   datetime.now()
print("now =", now)

Onehourplusfromnow = datetime.now() + timedelta(hours=1)
currentHour = Onehourplusfromnow.strftime("%H")
print("Current Hour =", currentHour)

Twominplusfromnow = datetime.now() + timedelta(minutes = 2)
currentMinute = Twominplusfromnow.strftime("%M")
print("Current Minute =", currentMinute)

driver.get(baseURL)
driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys(userName)
driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(userPass)
driver.find_element_by_id("action-login").click()
sleep(5)
driver.get(baseURL+"soc/create-trip")
driver.find_element_by_name("mobileNum").send_keys("01160606001")
sleep(1)
driver.find_element_by_xpath("//button[@class='btn btn-primary btn-lg']").click()
sleep(3)
driver.find_element_by_xpath("//div[@class='input-group-append']/button").click()
driver.find_element_by_xpath("//div[@tabindex='0']/div").click()
driver.find_element_by_xpath("//input[@placeholder='HH']").send_keys(currentHour)
driver.find_element_by_xpath("//input[@placeholder='MM']").send_keys(currentMinute)
if currentHour=="12":
    driver.find_element_by_xpath("//button[@class='btn btn-outline-primary']").click()
action = ActionChains(driver)
driver.find_element_by_id("createPickUpCtrl").send_keys("dhaka")
sleep(6)

action.drag_and_drop_by_offset(driver.find_element_by_xpath("//div[@class='map']/div/div/div/div"), 500, 200)
driver.find_element_by_id("createDropOffCtrl").send_keys("gazipur")
sleep(6)
action.drag_and_drop_by_offset(driver.find_element_by_id("createDropOffMap"), 50, 60)
driver.find_element_by_xpath("//input[@role='combobox']").send_keys("Palm Oil")
driver.find_element_by_xpath("//div[@role='option']").click()
#driver.find_element_by_xpath("//div[@class='customer-details']").send_keys(Keys.CONTROL + Keys.HOME)
driver.execute_script("scrollBy(0,-500);")
sleep(2)
driver.find_element_by_xpath("//div[@class='d-flex']/button[2]").click()
driver.find_element_by_xpath("//input[@formcontrolname='expectedTripPrice']").send_keys("2000")
driver.find_element_by_xpath("//textarea[@formcontrolname='creationReason']").send_keys("Trip approved by Admin")
driver.find_element_by_xpath("/html/body/ngb-modal-window/div/div/div[3]/button[1]").click()
print("Toast Message: ",driver.find_element_by_id("toast-container"))
sleep(3)
driver.quit()