from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://kwikhire-dev.s3-website.ap-south-1.amazonaws.com")
elem = driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/a[2]")
elem.click()
time.sleep(3)

#Empty email and password
elem = driver.find_element_by_id("loginEmail")
elem.send_keys("")
print("sending email")
time.sleep(3)
elem = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/form/div[1]/div[2]/input")
elem.send_keys("")
print("sending password")
time.sleep(3)
elem.send_keys(Keys.RETURN)
print("click on login")

if driver.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[1]/div[1]/p"):
    error1 = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[1]/div[1]/p")
    time.sleep(3)
    if driver.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[1]/div[2]/p"):
        error2 = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[1]/div[2]/p")
        assert error2.text == 'Password cannot be blank'
        print(error1.text)
        print(error2.text)
    else :    
        assert error1.text == 'E-mail cannot be blank'
        print(error1.text)
elif driver.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[1]/div[2]/p"):
    error = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[1]/div[2]/p")
    assert error.text == 'Password cannot be blank'
    print(error.text)  
    
#email format wrong
time.sleep(3)
elem = driver.find_element_by_id("loginEmail")
elem.send_keys("sneha")
print("sending email")
time.sleep(3)
elem = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/form/div[1]/div[2]/input")
elem.send_keys("1234")
print("sending password")
time.sleep(3)
elem.send_keys(Keys.RETURN)
print("click on login")
if driver.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[1]/div[1]/p"):
    error = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[1]/div[1]/p")
    assert 'E-mail format is wrong' == error.text 
    print(error.text)

#invalid credentials
time.sleep(3)
elem = driver.find_element_by_id("loginEmail")
elem.clear()
elem.send_keys("sneha@gmail.com")
print("sending email")
time.sleep(3)
elem = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/form/div[1]/div[2]/input")
elem.clear()
elem.send_keys("1234567")
print("sending password")
time.sleep(3)
elem.send_keys(Keys.RETURN)
time.sleep(5)
print("click on login")
if driver.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[1]/p[2]/span"):
    error = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[1]/p[2]/span")
    assert error.text == 'E-Mail ID or Password is invalid'
    print(error.text)

#valid 
time.sleep(3)
elem = driver.find_element_by_id("loginEmail")
elem.clear()
elem.send_keys("snehareddy5125@gmail.com")
print("sending email")
time.sleep(3)
elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[2]/div[2]/input")
elem.clear()
elem.send_keys("Password1")
print("sending password")
time.sleep(3)
elem.send_keys(Keys.RETURN)
print("click on login")   
time.sleep(3) 
url2 = driver.current_url 
print(url2)
dashboard = "http://kwikhire-dev.s3-website.ap-south-1.amazonaws.com/dashboard"
if url2 == dashboard :
    print("Login successfully")
    