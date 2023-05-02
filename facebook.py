import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from colored import fg, bg, attr  # pip install colored
from dotenv import load_dotenv

from fake import get_data

load_dotenv()


class Facebook:
    def __init__(self):
        try:
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        except:
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def sign_up(self, user_data):
        try:
            # Opening Facebook.
            self.driver.get(os.getenv('FB_URL'))
            print(f"{fg('yellow_1')}Faceboook Opened!{attr('reset')}")
            time.sleep(1)

            signup_btn = self.driver.find_element(By.XPATH, "//*[@data-testid='open-registration-form-button']")
            signup_btn.click()
            time.sleep(1)

            firstname = self.driver.find_element(By.NAME, 'firstname')
            firstname.send_keys(user_data['firstname'])
            time.sleep(1)

            lastname = self.driver.find_element(By.NAME, 'lastname')
            lastname.send_keys(user_data['lastname'])
            time.sleep(1)

            email = self.driver.find_element(By.NAME, 'reg_email__')
            email.send_keys(user_data['email'])
            time.sleep(1)


            email = self.driver.find_element(By.NAME, 'reg_email_confirmation__')
            email.send_keys(user_data['email'])
            time.sleep(1)

            passwd = self.driver.find_element(By.ID, 'password_step_input')
            passwd.send_keys(user_data['pass'])
            time.sleep(1)

            birth_day = Select(self.driver.find_element(By.NAME, "birthday_day"))
            birth_day.select_by_visible_text(user_data['birth_day'])
            time.sleep(1)

            # short month name in title case .i.e. Jan, Feb, Mar
            birth_month = Select(self.driver.find_element(By.NAME, "birthday_month"))
            birth_month.select_by_visible_text(user_data['birth_month'])
            time.sleep(1)

            birth_year = Select(self.driver.find_element(By.NAME, "birthday_year"))
            birth_year.select_by_visible_text(user_data['birth_year'])
            time.sleep(1)

            if user_data['gender'] == 'F':
                gender = self.driver.find_element(By.XPATH, "//input[@name='sex' and @value='1']")
            elif user_data['gender'] == 'M':
                gender = self.driver.find_element(By.XPATH, "//input[@name='sex' and @value='1']")
            else:
                print('Other genders are not supported yet!')

            gender.click()


            # # Entering Email and Password
            # username_box = self.driver.find_element(By.ID, "email")
            # username_box.send_keys(user)
            # print(f"{fg('yellow_1')}Email entered{attr('reset')}")
            # time.sleep(1)
            #
            # password_box = self.driver.find_element(By.ID, "pass")
            #
            # password_box.send_keys(password)
            # print(f"{fg('yellow_1')}Password entered{attr('reset')}")
            #
            # Pressing The Signup Button
            signup_box = self.driver.find_element(By.NAME, "websubmit")
            signup_box.click()

            print(f"Done")
            input(f"{fg('green_1')}Press anything to quit{attr('reset')}")
            print(f"{fg('green_1')}Finished{attr('reset')}")
            return user_data
        except Exception as e:
            print(f"{fg('red_1')}Failed to execute script{attr('reset')}")
            print(f"{fg('red_1')}Exception: {e}")
        finally:
            self.driver.quit()


    def sign_in(self):
        try:
            # Enter Your Email ID And Password
            user = os.getenv('EMAIL')#input(f"{fg('green_1')}Enter Email Id:{attr('reset')}")
            password = os.getenv('PASS')#input(f"{fg('green_1')}Enter Password:{attr('reset')}")

            # Opening Facebook.
            self.driver.get('https://www.facebook.com/')
            print(f"{fg('yellow_1')}Faceboook Opened!{attr('reset')}")
            time.sleep(1)

            # Entering Email and Password
            username_box = self.driver.find_element(By.ID, "email")
            username_box.send_keys(user)
            print(f"{fg('yellow_1')}Email entered{attr('reset')}")
            time.sleep(1)

            password_box = self.driver.find_element(By.ID, "pass")

            password_box.send_keys(password)
            print(f"{fg('yellow_1')}Password entered{attr('reset')}")

            # Pressing The Login Button
            login_box = self.driver.find_element(By.NAME, "login")

            login_box.click()
            self.driver.quit()

            print(f"{fg('green_1')}Finished{attr('reset')}")
        except Exception as e:
            print(f"{fg('red_1')}Failed to execute script{attr('reset')}")
            print(e)
        finally:
            self.driver.quit()

if __name__ == "__main__":
     # Initiliaze Webdriver

    user_data = get_data()
    fb = Facebook()
    fb.sign_up(user_data)
