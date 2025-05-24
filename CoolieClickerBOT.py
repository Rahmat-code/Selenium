import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver():
    options = Options()
    options.add_argument("--disable-infobars")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    return webdriver.Chrome(options=options)

def main():
    driver = setup_driver()
    try:
        driver.get("https://orteil.dashnet.org/experiments/cookie/")
        wait = WebDriverWait(driver, 10)

        start_time = time.time()
        duration = 5 * 60  # 5 minutes

        while time.time() - start_time < duration:
            # Click cookie for 5 seconds
            click_start = time.time()
            while time.time() - click_start < 10:
                cookie = wait.until(EC.element_to_be_clickable((By.ID, "cookie")))
                cookie.click()

            # Get current money
            money_text = driver.find_element(By.ID, "money").text.replace(",", "")
            try:
                current_money = int(money_text)
            except ValueError:
                current_money = 0

            # Find all available items
            store_items = driver.find_elements(By.CSS_SELECTOR, "#store div")
            affordable = {}

            for item in store_items:
                if "grayed" not in item.get_attribute("class"):
                    try:
                        name = item.get_attribute("id")
                        cost_text = item.find_element(By.TAG_NAME, "b").text
                        match = re.search(r"(\d[\d,]*)$", cost_text)
                        if match:
                            cost = int(match.group(1).replace(",", ""))
                            affordable[name] = cost
                    except:
                        continue

            if affordable:
                best_choice = max(
                    (item for item in affordable.items() if item[1] <= current_money),
                    key=lambda x: x[1],
                    default=None
                )
                if best_choice:
                    driver.find_element(By.ID, best_choice[0]).click()
                    print(f"Bought {best_choice[0]} for {best_choice[1]}")

        print("Finished 5-minute run.")

    except Exception as e:
        print("An error occurred:", e)
    else:
        cps = driver.find_element(By.ID, "cps").text
        print(cps)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
