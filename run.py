import time
import random
import string
import pyperclip
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Function to generate a random site name
def generate_random_site_name():
    letters = string.ascii_lowercase
    digits = string.digits
    site_name = (
        ''.join(random.choices(letters, k=3)) +  
        ''.join(random.choices(digits, k=3)) +    
        ''.join(random.choices(letters, k=3)) +  
        ''.join(random.choices(digits, k=3))      
    )
    return site_name

# Read email addresses from akun.txt
with open('akun.txt', 'r') as file:
    emails = [line.strip() for line in file.readlines()]

while emails:
    email = emails.pop(0)
    
    # Setup ChromeDriver with undetected_chromedriver
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--headless")  # Set headless mode

    # Initialize ChromeDriver
    driver = uc.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    vars = {}
    
    def wait_for_window(timeout=2):
        time.sleep(round(timeout / 1000))
        wh_now = driver.window_handles
        wh_then = vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()
    
    # Start the automation
    driver.get("https://app.netlify.com/login")
    time.sleep(5)
    
    driver.set_window_size(1200, 1000)
    time.sleep(3)
    
    driver.find_element(By.CSS_SELECTOR, ".tw-text-left").click()
    time.sleep(5)
    
    element = driver.find_element(By.CSS_SELECTOR, ".tw-text-left")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(5)
    
    element = driver.find_element(By.CSS_SELECTOR, "body")
    actions.move_to_element(element).perform()
    time.sleep(5)
    
    # Input the email and password
    driver.find_element(By.NAME, "email").click()
    driver.find_element(By.NAME, "email").clear()
    driver.find_element(By.NAME, "email").send_keys(email)
    time.sleep(3)
    
    driver.find_element(By.NAME, "password").click()
    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "password").send_keys("LeviYiyi123@")
    time.sleep(3)
    
    driver.find_element(By.CSS_SELECTOR, ".tw-flex > .btn").click()
    time.sleep(5)
    
    element = driver.find_element(By.LINK_TEXT, "Import from Git")
    actions.move_to_element(element).perform()
    time.sleep(5)
    
    driver.find_element(By.LINK_TEXT, "Import from Git").click()
    time.sleep(5)
    
    vars["window_handles"] = driver.window_handles
    driver.find_element(By.XPATH, "//button[text()='Bitbucket']").click()
    time.sleep(5)
    
    vars["win3727"] = wait_for_window(2000)
    vars["root"] = driver.current_window_handle
    driver.switch_to.window(vars["win3727"])
    time.sleep(5)
    
    # Log in to Bitbucket
    driver.find_element(By.ID, "username").click()
    driver.find_element(By.ID, "username").send_keys("geivux1+fatiscent@outlook.com")
    driver.find_element(By.ID, "username").send_keys(Keys.ENTER)
    time.sleep(5)
    
    driver.find_element(By.ID, "password").click()
    driver.find_element(By.ID, "password").send_keys("AyLevy123@")
    driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
    time.sleep(5)
    
    # Switch back to the root window
    driver.switch_to.window(vars["root"])
    time.sleep(5)
    
    element = driver.find_element(By.XPATH, "//a[contains(@href, '/start/repos/betbeyw%2Fvipor') and contains(@aria-label, 'vipor')]")
    actions.move_to_element(element).perform()
    time.sleep(2)
    
    element.click()
    time.sleep(5)
    
    driver.find_element(By.NAME, "siteName").click()
    site_name = generate_random_site_name()
    driver.find_element(By.NAME, "siteName").send_keys(site_name)
    driver.find_element(By.NAME, "siteName").send_keys(Keys.ENTER)
    time.sleep(5)
    
    driver.find_element(By.CSS_SELECTOR, "#deploys-secondary-nav-item .tw-transition").click()
    time.sleep(5)
    
    driver.find_element(By.CSS_SELECTOR, ".btn-secondary:nth-child(1) > .tw-flex").click()
    time.sleep(5)
    
    driver.find_element(By.CSS_SELECTOR, ".card:nth-child(8) .btn").click()
    time.sleep(5)
    
    driver.find_element(By.NAME, "title").send_keys("asc")
    driver.find_element(By.NAME, "title").send_keys(Keys.ENTER)
    time.sleep(5)
    
    driver.find_element(By.CSS_SELECTOR, ".tw-relative:nth-child(1) > .btn .scalable-icon").click()
    time.sleep(1)
    
    copied_text = pyperclip.paste()
    print(f"{copied_text}")
    
    with open('api.txt', 'a') as api_file:
        api_file.write(f"{copied_text}\n")
    
    time.sleep(5)
    driver.quit()
    time.sleep(2)

print("Semua email selesai diproses.")
