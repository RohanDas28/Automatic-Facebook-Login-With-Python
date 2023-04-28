import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from colored import fg, bg, attr  # pip install colored
from dotenv import load_dotenv

from fake import get_data
# Initiliaze Webdriver
try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
except:
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

load_dotenv()
def FacebookSignUp():
    try:
        user_data = get_data()
        # Opening Facebook.
        driver.get('https://www.facebook.com/')
        print(f"{fg('yellow_1')}Faceboook Opened!{attr('reset')}")
        time.sleep(1)

        signup_btn = driver.find_element(By.XPATH, "//a[@data-testid='open-registration-form-button']")
        signup_btn.click()
        time.sleep(1)

        firstname = driver.find_element(By.NAME, 'firstname')
        firstname.send_keys(user_data['firstname'])
        time.sleep(1)

        lastname = driver.find_element(By.NAME, 'lastname')
        lastname.send_keys(user_data['lastname'])
        time.sleep(1)

        email = driver.find_element(By.NAME, 'reg_email__')
        email.send_keys(user_data['email'])
        time.sleep(1)


        email = driver.find_element(By.NAME, 'reg_email_confirmation__')
        email.send_keys(user_data['email'])
        time.sleep(1)

        passwd = driver.find_element(By.NAME, 'reg_passwd__')
        passwd.send_keys(user_data['pass'])
        time.sleep(1)

        birth_day = Select(driver.find_element(By.NAME, "birthday_day"))
        birth_day.select_by_visible_text(user_data['birth_day'])
        time.sleep(1)

        # short month name in title case .i.e. Jan, Feb, Mar
        birth_month = Select(driver.find_element(By.NAME, "birthday_month"))
        birth_month.select_by_visible_text(user_data['birth_month'])
        time.sleep(1)

        birth_year = Select(driver.find_element(By.NAME, "birthday_year"))
        birth_year.select_by_visible_text(user_data['birth_year'])
        time.sleep(1)

        if user_data['gender'] == 'F':
            gender = driver.find_element(By.XPATH, "//input[@name='sex' and @value='1']")
        elif user_data['gender'] == 'M':
            gender = driver.find_element(By.XPATH, "//input[@name='sex' and @value='1']")
        else:
            print('Other genders are not supported yet!')

        gender.click()


        # # Entering Email and Password
        # username_box = driver.find_element(By.ID, "email")
        # username_box.send_keys(user)
        # print(f"{fg('yellow_1')}Email entered{attr('reset')}")
        # time.sleep(1)
        #
        # password_box = driver.find_element(By.ID, "pass")
        #
        # password_box.send_keys(password)
        # print(f"{fg('yellow_1')}Password entered{attr('reset')}")
        #
        # Pressing The Signup Button
        signup_box = driver.find_element(By.NAME, "websubmit")
        signup_box.click()

        print(f"Done")
        input("{fg('green_1')}Press anything to quit{attr('reset')}")
        # driver.quit()
        print(f"{fg('green_1')}Finished{attr('reset')}")
    except Exception as e:
        print(f"{fg('red_1')}Failed to execute script{attr('reset')}")
        print(f"{fg('red_1')}Exception: {e}")

def FacebookLogin():
    try:
        # Enter Your Email ID And Password
        user = os.getenv('EMAIL')#input(f"{fg('green_1')}Enter Email Id:{attr('reset')}")
        password = os.getenv('PASS')#input(f"{fg('green_1')}Enter Password:{attr('reset')}")

        # Opening Facebook.
        driver.get('https://www.facebook.com/')
        print(f"{fg('yellow_1')}Faceboook Opened!{attr('reset')}")
        time.sleep(1)

        # Entering Email and Password
        username_box = driver.find_element(By.ID, "email")
        username_box.send_keys(user)
        print(f"{fg('yellow_1')}Email entered{attr('reset')}")
        time.sleep(1)

        password_box = driver.find_element(By.ID, "pass")

        password_box.send_keys(password)
        print(f"{fg('yellow_1')}Password entered{attr('reset')}")

        # Pressing The Login Button
        login_box = driver.find_element(By.NAME, "login")

        login_box.click()

        print(f"Done")
        input("{fg('green_1')}Press anything to quit{attr('reset')}")
        driver.quit()
        print(f"{fg('green_1')}Finished{attr('reset')}")
    except Exception as e:
        print(f"{fg('red_1')}Failed to execute script{attr('reset')}")
        print(e)

FacebookSignUp()
