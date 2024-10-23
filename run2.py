import time
import random
import string
import pyperclip  # Make sure to install this package using pip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException  # Import exception

# Function to generate a random site name
def generate_random_site_name():
    letters = string.ascii_lowercase  # lowercase letters
    digits = string.digits  # digits
    site_name = (
        ''.join(random.choices(letters, k=3)) +  # 3 random letters
        ''.join(random.choices(digits, k=3)) +   # 3 random digits
        ''.join(random.choices(letters, k=3)) +  # 3 random letters
        ''.join(random.choices(digits, k=3))     # 3 random digits
    )
    return site_name

# Read email addresses from test.txt
with open('test.txt', 'r') as file:
    emails = [line.strip() for line in file.readlines()]

# Loop through each email address until the list is empty
while emails:
    email = emails.pop(0)  # Take the first email from the list and remove it
    
    # Setup driver (assuming ChromeDriver is in the system's PATH)
    driver = webdriver.Chrome()  # If specific path is needed: webdriver.Chrome(executable_path='/path/to/chromedriver')
    driver.implicitly_wait(10)  # Optional wait time to ensure elements load
    vars = {}
    
    def wait_for_window(timeout=2):
        time.sleep(round(timeout / 1000))
        wh_now = driver.window_handles
        wh_then = vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()
    
    try:
        # Start the automation
        driver.get("https://app.netlify.com/login")
        time.sleep(5)
        
        driver.maximize_window()  # Open browser in full screen
        time.sleep(3)
        
        driver.find_element(By.CSS_SELECTOR, ".tw-text-left").click()
        time.sleep(5)
        
        element = driver.find_element(By.CSS_SELECTOR, ".tw-text-left")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(5)
        
        element = driver.find_element(By.CSS_SELECTOR, "body")
        actions.move_to_element(element).perform()
        time.sleep(3)
        
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

        # Check if the "Import from Git" element exists
        try:
            element = driver.find_element(By.LINK_TEXT, "Import from Git")
            actions.move_to_element(element).perform()
            time.sleep(5)
            driver.find_element(By.LINK_TEXT, "Import from Git").click()
        except NoSuchElementException:
            print(f"Element 'Import from Git' not found for {email}, skipping...")
            driver.quit()  # Close the browser
            continue  # Move to the next email
        
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
        
        # Mencari elemen dengan href link yang sesuai dan melakukan klik
        element = driver.find_element(By.XPATH, "//a[contains(@href, '/start/repos/betbeyw%2Ftitied') and contains(@aria-label, 'titied')]")
        actions.move_to_element(element).perform()
        time.sleep(2)

        # Klik elemen tersebut
        element.click()
        time.sleep(7)
        
        # Click "Disable visual editing"
        driver.find_element(By.XPATH, "//button[contains(@class, 'btn-secondary--danger') and text()='Disable visual editing']").click()
        time.sleep(7)
        
        # Scroll to SiteName and fill with random name
        site_name_element = driver.find_element(By.NAME, "siteName")
        driver.execute_script("arguments[0].scrollIntoView(true);", site_name_element)  # Ensure it's visible
        site_name_element.click()
        site_name = generate_random_site_name()
        site_name_element.send_keys(site_name)
        site_name_element.send_keys(Keys.ENTER)
        time.sleep(10)
              
        driver.find_element(By.CSS_SELECTOR, "#deploys-secondary-nav-item .tw-transition").click()
        time.sleep(5)
        
        driver.find_element(By.CSS_SELECTOR, ".btn-secondary:nth-child(1) > .tw-flex").click()
        time.sleep(5)
        
        driver.find_element(By.CSS_SELECTOR, ".card:nth-child(8) .btn").click()
        time.sleep(5)
        
        driver.find_element(By.NAME, "title").send_keys("asc")  # Use the name attribute for the title input
        driver.find_element(By.NAME, "title").send_keys(Keys.ENTER)  # Submit the input
        time.sleep(5)
        
        # Click the copy button
        driver.find_element(By.CSS_SELECTOR, ".tw-relative:nth-child(1) > .btn .scalable-icon").click()
        time.sleep(1)  # Short wait for clipboard to update
        
        # Get the copied text and write it to the console and the file
        copied_text = pyperclip.paste()  # Get the copied text from clipboard
        print(f"{copied_text}")  # Print the copied text to the console
        
        # Write the copied API to a file (append mode)
        with open('api.txt', 'a') as api_file:
            api_file.write(f"{copied_text}\n")
        
        time.sleep(5)
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Tutup browser setelah satu email diproses
        driver.quit()
        
        # Tunggu sebentar sebelum mengulangi proses jika masih ada email
        time.sleep(2)

# Setelah semua email diproses, program selesai
print("Semua email selesai diproses.")
