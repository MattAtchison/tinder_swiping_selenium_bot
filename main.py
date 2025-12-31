from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep

chrome_options = webdriver.ChromeOptions()

URL = 'https://tinder.com/app/recs'
NUMBER = '2486391680'

chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

wait = WebDriverWait(driver, 5)

#--------------------------------------------------------
# clicking the login button


login = wait.until(
    ec.element_to_be_clickable(
        (By.XPATH, "//a[.//div[text()='Log in']]")
    )
)
login.click()

#-------------------------------------------------------
# clicking the login by phone through the XPATH

login_with_phone = wait.until(
    ec.element_to_be_clickable(
        (By.XPATH, "//button[contains(., 'phone')]")
    )
)
login_with_phone.click()

#--------------------------------------------------------
# entering in my phone number

number_input = wait.until(
    ec.element_to_be_clickable(
        (By.ID, "phone_number")
    )
)

number_input.send_keys(f'{NUMBER}')

#--------------------------------------------------------
# hitting next after entering in the phone number

next_button = wait.until(
    ec.element_to_be_clickable(
        (By.XPATH, "//button[contains(., 'Next')]")
    )
)
next_button.click()

#--------------------------------------------------------
# the meat and potatoes of the project

for n in range(100):


    try:
        like_button = wait.until(
            ec.element_to_be_clickable(
                (By.XPATH, "//button[contains(.,'Like')]")
            )
        )
        like_button.click()

    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

driver.quit()







