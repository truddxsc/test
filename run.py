import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc  # Correct import

# Function to generate a random site name
def generate_random_site_name():
    letters = string.ascii_lowercase  # lowercase letters
    digits = string.digits  # digits
    site_name = (
        ''.join(random.choices(letters, k=3)) +  # 3 random letters
        ''.join(random.choices(digits, k=3)) +    # 3 random digits
        ''.join(random.choices(letters, k=3)) +  # 3 random letters
        ''.join(random.choices(digits, k=3))      # 3 random digits
    )
    return site_name

# Read email addresses from akun.txt
with open('akun.txt', 'r') as file:
    emails = [line.strip() for line in file.readlines()]

# Loop through each email address until the list is empty
while emails:
    email = emails.pop(0)  # Take the first email from the list and remove it
    
    # Setup driver using undetected_chromedriver
    driver = uc.Chrome()  # Use undetected ChromeDriver
    driver.implicitly_wait(10)  # Optional wait time to ensure elements load
    vars = {}
    
    def wait_for_window(timeout=2):
        time.sleep(timeout)
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
    driver.find_element(By.NAME, "email").clear()  # Clear previous email
    driver.find_element(By.NAME, "email").send_keys(email)  # Use the current email
    time.sleep(3)
    
    driver.find_element(By.NAME, "password").click()
    driver.find_element(By.NAME, "password").clear()  # Clear previous password if necessary
    driver.find_element(By.NAME, "password").send_keys("LeviYiyi123@")  # Replace with your password
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
    
    element = driver.find_element(By.XPATH, "//a[contains(@href, '/start/repos/betbeyw%2Ftitied') and contains(@aria-label, 'titied')]")
    actions.move_to_element(element).perform()
    time.sleep(2)
    element.click()
    time.sleep(5)
    
    driver.find_element(By.NAME, "siteName").click()
    site_name = generate_random_site_name()  # Generate random site name
    driver.find_element(By.NAME, "siteName").send_keys(site_name)  # Use the generated random site name
    driver.find_element(By.NAME, "siteName").send_keys(Keys.ENTER)
    time.sleep(5)
    
    driver.find_element(By.CSS_SELECTOR, "#deploys-secondary-nav-item .tw-transition").click()
    time.sleep(5)
    
    driver.find_element(By.CSS_SELECTOR, ".btn-secondary:nth-child(1) > .tw-flex").click()
    time.sleep(5)
    
    driver.find_element(By.CSS_SELECTOR, ".card:nth-child(8) .btn").click()
    time.sleep(5)
    
    driver.find_element(By.NAME, "title").send_keys("asc")  # Use the name attribute for the title input
    driver.find_element(By.NAME, "title").send_keys(Keys.ENTER)  # Submit the input
    time.sleep(5)
    
    # Save the API directly to a file
    api_element = driver.find_element(By.CSS_SELECTOR, ".tw-relative:nth-child(1) > .btn .scalable-icon")
    api_element.click()
    time.sleep(1)  # Short wait for the action to complete
    
    # Instead of using pyperclip, wait for the element containing the API key to appear
    time.sleep(2)  # Adjust based on how long it takes to display
    copied_text = driver.find_element(By.CSS_SELECTOR, "selector-for-api-key").text  # Update with the correct selector

    print(f"API: {copied_text}")  # Print the copied text to the console
    
    # Write the copied API to a file (append mode)
    with open('api.txt', 'a') as api_file:
        api_file.write(f"{copied_text}\n")
    
    # Wait before processing the next email
    time.sleep(5)
    
    # Close browser after one email is processed
    driver.quit()
    
    # Wait a moment before repeating the process if there are still emails
    time.sleep(2)

# After all emails are processed, program completes
print("Semua email selesai diproses.")
