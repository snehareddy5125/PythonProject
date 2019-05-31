from selenium import webdriver
import time

driver= webdriver.Firefox()
driver.get("http://kwikhire-dev.s3-website.ap-south-1.amazonaws.com/login")
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/form/div[1]/div[3]/a").click()
time.sleep(3)
print("click on forgot password")
url1 = driver.current_url
if url1 =="http://kwikhire-dev.s3-website.ap-south-1.amazonaws.com/forgot-password":
    
    mail=["","sneha","sneha@gmail.com","snehareddy5125@gmail.com"]
    for i in mail:
        email = driver.find_element_by_id("forgotPasswordEmail")
        email.clear()
        email.send_keys(i)
        time.sleep(3)
        print("sending email ")
        driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/form/div[3]").click()
        time.sleep(5)
        print("send")
        url2 = driver.current_url
       
        try:
            if driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/form/div[2]/div/p"):
                emailerror = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/form/div[2]/div/p").text
                if emailerror == "E-mail cannot be blank":
                    print("E-mail cannot be blank")
                elif emailerror == "E-mail format is wrong":
                    print("E-mail format is wrong")
        except :                                           
            try:
                if driver.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[1]/p"):
                    error = driver.find_element_by_xpath("//html/body/div/div/div/div[2]/form/div[1]/p").text
                    if error == "E-Mail ID is not found in our database":   
                        print("E-Mail ID is not found in our database") 
            except:        
                error =  driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/p").text
                
                #when email is like snehareddy5125@gmail  
                if error == "Error occured while sending password reset link":
                    print("Error occured while sending password reset link")  
                #when email is like snehareddy5125@gmail.com    
                else:
                    print(error)  
                    print("Success")                                  