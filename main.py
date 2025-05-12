# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

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
  driver.get("http://automated.pythonanywhere.com/login/")
  return driver

def clean_text(text):
  """Extract only the temperature from text"""
  output = float(text.split(": ")[1])
  return output

def write(text):
  cur_date = dt.now()
  timestamp = cur_date.strftime("%Y-%m-%d_%H-%M-%S")
  filename = f"{timestamp}.txt"
  with open(filename, "w") as f:
    f.write(f"Temperature: {text}")


def main():
  driver = get_drvier()
  driver.find_element(by="id", value="id_username").send_keys("automated")
  time.sleep(2)
  driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
  time.sleep(10)
  driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
  #print(driver.current_url)

  while(1):
    time.sleep(2)
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    temp = clean_text(element.text)
    write(temp)


main()