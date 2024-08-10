from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://10.11.13.231")
driver.maximize_window()
# Sign-IN
driver.find_element(By.ID,"details-button").click()
driver.find_element(By.ID,"proceed-link").click()
driver.find_element(By.ID,"EwsLogin").click()
print("EWS Page Launch Successfully")
driver.find_element(By.ID,"PasswordTextBox").send_keys("rdl@12345")
driver.find_element(By.ID,"signInOk").click()
print("EWS Page Login Successfully")
time.sleep(2)

# Scan and digital
driver.find_element(By.XPATH,"//a[@id='SendPages']").click()
driver.find_element(By.ID,"AddressBook").click()
for i in range(3):
    #driver.get_screenshot_as_file("C:\Users\HEMANTHM\Desktop\F_W\Curie.png")
    if i<=3:
        driver.find_element(By.ID,"DeviceContactAddContactButton").click()
        driver.find_element(By.ID,"DisplayName").send_keys("MPHASIS")
        driver.find_element(By.ID,"LastName").send_keys("HP")
        driver.find_element(By.ID,"Email").send_keys("user2@dodca.com")
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div[2]/form/div[2]/span[1]/input").click()
        driver.find_element(By.XPATH,"//input[@id='FormButtonSubmit']").click()
# time.sleep(4)
driver=webdriver.Edge()
saving in git