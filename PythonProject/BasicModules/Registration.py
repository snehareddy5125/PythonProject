from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://kwikhire-dev.s3-website.ap-south-1.amazonaws.com")
time.sleep(2)
elem = driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/a[3]")
elem.click()
time.sleep(3)

#empty inputs
elem = driver.find_element_by_id("signupEmail")
elem.send_keys("")
print("sending email")
elem = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[4]/input")
elem.send_keys("")
print("sending password")
elem = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[5]/input")
elem.send_keys("")
print("sending c password")
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/form/button").click()
print("click on login")

emailerror=driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[3]/p")
print(emailerror.text)
passerror = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[4]/p")
print(passerror.text)
cpasserror = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[5]/p")
print(cpasserror.text)
print("\n")   
time.sleep(3) 
#email format and password less then 8
elem = driver.find_element_by_id("signupEmail")
elem.send_keys("sneha")
print("sending email")
time.sleep(3)
elem = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[4]/input")
elem.send_keys("123456")
print("sending password")
time.sleep(3)
elem = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[5]/input")
elem.send_keys("123456")
print("sending c password")
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/form/button").click()
print("click on login")
time.sleep(5)
emailele = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[3]/p")
print(emailele.text)
passerror = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[4]/p").text
print(passerror)
time.sleep(3)
print("\n")         
#password policy              
elem = driver.find_element_by_id("signupEmail")
elem.clear()
elem.send_keys("sneha@gmail.com")
print("sending email")
time.sleep(3)
elem = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[4]/input")
elem.clear()
elem.send_keys("123456789")
print("sending password")
time.sleep(3)
elem = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[5]/input")
elem.clear()
elem.send_keys("123456870")
print("sending c password")
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/form/button").click()
time.sleep(3)
print("click on login")      
if driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]"):
    psserror = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]").text
    print(passerror)
    print("\n")   
    time.sleep(3)   
#re enter password mismatch
elem = driver.find_element_by_id("signupEmail")
elem.clear()
elem.send_keys("sneha@gmail.com")
print("sending email")
time.sleep(3)
elem = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[5]/input")
elem.clear()
elem.send_keys("123456789")
print("sending password")
time.sleep(3)
elem = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[6]/input")
elem.clear()
elem.send_keys("123456780")
print("sending c password")
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/form/button").click()
print("click on login")      
if driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]"):
    cpasserror = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]").text
    print(cpasserror)