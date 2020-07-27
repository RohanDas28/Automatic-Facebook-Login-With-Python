from selenium import webdriver

PATH = 'Your Driver PATH'
url = 'https://facebook.com'
driver = webdriver.Chrome(PATH)
driver.get(url)

email = driver.find_element_by_id('email')
email.send_keys('Your Email or Number')
password = driver.find_element_by_id('pass')
password.send_keys('Your Password')

submit = driver.find_element_by_xpath('//*[@id="loginbutton"]')
submit.click()
