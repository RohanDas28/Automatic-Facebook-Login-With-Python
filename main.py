import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from colored import fg, bg, attr  # pip install colored
# Initiliaze Webdriver
try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
except:
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())


def FacebookLogin():
    try:
        # Enter Your Email ID And Password
        user = input(f"{fg('green_1')}Enter Email Id:{attr('reset')}")
        password = input(f"{fg('green_1')}Enter Password:{attr('reset')}")

        # Opening Facebook.
        driver.get('https://www.facebook.com/')
        print(f"{fg('yellow_1')}Faceboook Opened!{attr('reset')}")
        time.sleep(1)

        # Entering Email and Password
        username_box = driver.find_element_by_id('email')
        username_box.send_keys(user)
        print(f"{fg('yellow_1')}Email entered{attr('reset')}")
        time.sleep(1)

        password_box = driver.find_element_by_id('pass')
        password_box.send_keys(password)
        print(f"{fg('yellow_1')}Password entered{attr('reset')}")

        # Pressing The Login Button
        login_box = driver.find_element_by_id('loginbutton')
        login_box.click()

        print(f"Done")
        input("{fg('green_1')}Press anything to quit{attr('reset')}")
        driver.quit()
        print(f"{fg('green_1')}Finished{attr('reset')}")
    except Exception:
        print(f"{fg('red_1')}Failed to execute script{attr('reset')}")


FacebookLogin()
