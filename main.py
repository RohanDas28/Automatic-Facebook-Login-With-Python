import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# Initiliaze Webdriver
driver = webdriver.Chrome(ChromeDriverManager().install())

def FacebookLogin():
    #Enter Your Email ID And Password
	user=input('Enter Email Id:')  
	password=input('Enter Password:')

	#Opening Facebook.
	driver.get('https://www.facebook.com/') 
	print ("Facebook Opened") 
	time.sleep(1) 
	  
    #Entering Email and Password
	username_box = driver.find_element_by_id('email') 
	username_box.send_keys(user) 
	print ("Email Id entered") 
	time.sleep(1) 
	  
	password_box = driver.find_element_by_id('pass') 
	password_box.send_keys(password) 
	print ("Password entered") 

	#Pressing The Login Button  
	login_box = driver.find_element_by_id('loginbutton') 
	login_box.click() 

	  
	print ("Done") 
	input('Press anything to quit') 
	driver.quit() 
	print("Finished")

FacebookLogin()


