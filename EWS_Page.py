from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://10.11.12.234/")
driver.maximize_window()

# Sign-IN
driver.find_element(By.ID,"details-button").click()
driver.find_element(By.ID,"proceed-link").click()
driver.find_element(By.ID,"EwsLogin").click()
print("EWS Page Launch Successfully")

if driver.find_elements(By.XPATH,"//*[@id='Information']" and '//*[@id="SecurityPages"]'):
    driver.find_element(By.XPATH,'//*[@id="SecurityPages"]').click()
    driver.find_element(By.XPATH,'//*[@id="newPassword"]').send_keys("rdl@12345")
    driver.find_element(By.XPATH, '//*[@id="verifyPassword"]').send_keys("rdl@12345")
    driver.find_element(By.XPATH,'//*[@id="FormButtonSubmit"]').click()
    time.sleep(5)
    print("EWs page password configured and sign-in successfully")
    time.sleep(2)
else:
    driver.find_element(By.ID, "PasswordTextBox").send_keys("rdl@12345")
    driver.find_element(By.ID, "signInOk").click()
    print("EWS Page Login Successfully")
    print("Ews signin successfully")
    time.sleep(2)

# Time and date Sync
driver.find_element(By.XPATH,"//a[@id='SettingsPages']").click()
driver.find_element(By.XPATH,"//a[@id='DateAndTime']").click()
driver.find_element(By.XPATH,"//input[@id='TimeZoneSettings']").click()
region=driver.find_element(By.XPATH,"//select[@id='CurrentTimeZone']")
drop=Select(region)
drop.select_by_visible_text('(GMT+05:30) Chennai, Kolkata, Mumbai, New Delhi')
driver.find_element(By.XPATH,"//input[@id='FormButtonSubmit']").click()
print("Region Set successfully")
driver.find_element(By.XPATH,"//input[@id='NTSSettings']").click()
driver.find_element(By.XPATH,"//input[@id='ServerAddress']").send_keys('10.11.12.67')
driver.find_element(By.XPATH,"//input[@id='SyncNow']").click()
driver.find_element(By.XPATH,"//input[@id='SyncNow']").click()
print("time and date Sync successfully")
time.sleep(2)

# Security TAB
driver.find_element(By.XPATH,"//a[@id='SecurityPages']").click()
driver.find_element(By.XPATH, "//input[@id='ServicePin']").clear()
driver.find_element(By.XPATH, "//input[@id='ServicePin']").send_keys("12345678")
driver.find_element(By.ID, "VerifyServicePin").send_keys("12345678")
print("ServicePin set successfully")
driver.find_element(By.XPATH,"//label[normalize-space()='Enable Remote User Auto Capture']").click()
print("Remote User Auto Capture set successfully")
driver.find_element(By.XPATH,"//label[normalize-space()='Enable PJL Device Access Commands']").click()#pjl 1
driver.find_element(By.XPATH,"//label[normalize-space()='Enable PS privileged operators']").click()#ps 1
driver.find_element(By.XPATH,"//label[normalize-space()='Enable PJL Drive Access']").click()#pjl 2
driver.find_element(By.XPATH,"//label[normalize-space()='Enable PS Drive Access']").click()#ps 2
print("PJL And PS set successfully")
driver.find_element(By.XPATH,"//input[@id='FormButtonSubmit']").click()
time.sleep(2)

#Networking TAB
driver.find_element(By.XPATH,"//a[normalize-space()='Networking']").click()
driver.find_element(By.XPATH,'//*[@id="localMenu"]/li[4]/a').click()
driver.find_element(By.XPATH,"//a[normalize-space()='Network Identification']").click()
driver.find_element(By.ID,"IPv4_DomainName").send_keys("winquc.dodca.com")
driver.find_element(By.ID,"IPv4_DnsServerId").clear()
driver.find_element(By.ID,"IPv4_DnsServerId").send_keys("10.11.12.67")
driver.find_element(By.XPATH,"//input[@id='Apply']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Network Settings']").click()
driver.find_element(By.XPATH,"//label[normalize-space()='Enable SNMPv1/v2 read-write access']").click()
driver.find_element(By.XPATH,"//input[@id='Apply']").click()
print("Domain join successfully")
time.sleep(2)