from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  # for demo pauses

def setup_driver():
    options = Options()
    options.add_argument("--disable-infobars")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    # Do not run headless — we want to see the browser
    # options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    return driver

def main():
    driver = setup_driver()

    try:
        driver.get("https://secure-retreat-92358.herokuapp.com/")
        
        wait = WebDriverWait(driver, 10)  # waits up to 10 seconds for elements

        # Wait for and fill first name
        fName_input = wait.until(EC.presence_of_element_located((By.NAME, "fName")))
        fName_input.send_keys("John")
        time.sleep(1)

        # Fill last name
        lName_input = driver.find_element(By.NAME, "lName")
        lName_input.send_keys("Doe")
        time.sleep(1)

        # Fill email
        email_input = driver.find_element(By.NAME, "email")
        email_input.send_keys("rahmathussain08jan@gmail.com")
        time.sleep(1)

        # Wait and click the submit button
        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-block")))
        submit_button.click()

        time.sleep(5)  # wait to see result page before browser closes

    except Exception as e:
        print("An error occurred:", e)
    
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
