
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime as dt

def get_drvier():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("https://titan22.com/account/login?return_url=%2Faccount")
  return driver

def main():
  driver = get_drvier()
  username = "rahmathussain08jan@gmail.com"
  pwd = "Hamza@12052025"
  driver.find_element(by="id", value="CustomerEmail").send_keys(username)
  time.sleep(2)
  driver.find_element(by="id", value="CustomerPassword").send_keys(pwd + Keys.RETURN)
  time.sleep(10)
  # Pause for manual CAPTCHA resolution
  input("Please complete the CAPTCHA manually, then press Enter to continue...")
  driver.find_element(by="xpath", value='//*[@id="shopify-section-footer"]/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a').click()
  print(driver.current_url)

main()