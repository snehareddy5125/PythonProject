from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

user = "stest@gmail.com"
pwd = "Password123"

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("url")
#login
elem = driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/a[2]")
elem.click()
time.sleep(3)
elem = driver.find_element_by_id("loginEmail")
elem.send_keys(user)
print("sending email")
time.sleep(3)
elem = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/form/div[1]/div[2]/input")
elem.send_keys(pwd)
print("sending password")
time.sleep(3)
elem.send_keys(Keys.RETURN)
print("login")
time.sleep(3)
url = driver.current_url 
print(url)
currenturl="url/login"

if currenturl==url:
    #email   
   
    
    try:
        if  driver.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[1]/div[1]/p"):
            print("element found")
            
            error = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[1]/div[1]/p")
            print(error.text)
    except Exception as e:    
        print("element not found")
        
    #password  
    try:
           
        if driver.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[1]/div[2]/p"):
            error = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[1]/div[2]/p")
            print(error.text)
    except Exception as e:    
        print("element not found")        
    # invalid credentials 
                     
    try:
        if driver.find_element_by_css_selector(".auth__content1__message-box"):
            error = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[1]/p[2]/span")
            print(error.text)  
    except Exception as e:    
        print("element not found")     
else:
    url= driver.current_url 
    print("Login Success" )    
