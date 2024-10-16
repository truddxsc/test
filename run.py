import time
import random
import string
import pyperclip  # Ensure this package is installed
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    
    # Setup Chrome options
    options = Options()
    options.add_argument("--headless")  # Run in headless mode (without GUI)
    options.add_argument("--no-sandbox")  # Bypass OS security model
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    # Setup driver (assuming ChromeDriver is pre-installed in GitHub Action environment)
    service = Service('/usr/bin/chromedriver')  # Path to chromedriver in GitHub Actions
    driver = webdriver.Chrome(service=service, options=options)

    # Start the automation
    driver.get("https://app.netlify.com/login")
    
    # Wait for elements to be present
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".tw-text-left")))
    time.sleep(5)
    
    driver.set_window_size(1200, 1000)
    time.sleep(3)
    
    driver.find_element(By.CSS_SELECTOR, ".tw-text-left").click()
    
    # Wait for the input fields to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
    
    # Input the email and password
    driver.find_element(By.NAME, "email").clear()  # Clear previous email
    driver.find_element(By.NAME, "email").send_keys(email)  # Use the current email
    time.sleep(3)
    
    driver.find_element(By.NAME, "password").clear()  # Clear previous password if necessary
    driver.find_element(By.NAME, "password").send_keys("LeviYiyi123@")  # Replace with your password
    time.sleep(3)
    
    driver.find_element(By.CSS_SELECTOR, ".tw-flex > .btn").click()
    
    # Wait for the import link to be clickable
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Import from Git")))
    driver.find_element(By.LINK_TEXT, "Import from Git").click()
    
    # Wait for the Bitbucket button to be clickable
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Bitbucket']")))
    driver.find_element(By.XPATH, "//button[text()='Bitbucket']").click()
    
    # Handle window switching
    vars = {}
    vars["window_handles"] = driver.window_handles
    vars["win3727"] = wait_for_window(2000)  # Custom function not provided in your original code
    vars["root"] = driver.current_window_handle
    driver.switch_to.window(vars["win3727"])

    # Log in to Bitbucket
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    driver.find_element(By.ID, "username").send_keys("geivux1+fatiscent@outlook.com")
    driver.find_element(By.ID, "username").send_keys(Keys.ENTER)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
    driver.find_element(By.ID, "password").send_keys("AyLevy123@")
    driver.find_element(By.ID, "password").send_keys(Keys.ENTER)

    # Switch back to the root window
    driver.switch_to.window(vars["root"])
    
    # Wait for the element containing the href link to be clickable
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/start/repos/betbeyw%2Ftitied') and contains(@aria-label, 'titied')]")))
    element = driver.find_element(By.XPATH, "//a[contains(@href, '/start/repos/betbeyw%2Ftitied') and contains(@aria-label, 'titied')]")
    element.click()

    driver.find_element(By.NAME, "siteName").click()
    site_name = generate_random_site_name()  # Generate random site name
    driver.find_element(By.NAME, "siteName").send_keys(site_name)  # Use the generated random site name
    driver.find_element(By.NAME, "siteName").send_keys(Keys.ENTER)
    
    driver.find_element(By.CSS_SELECTOR, "#deploys-secondary-nav-item .tw-transition").click()
    
    # Wait for and click the button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-secondary:nth-child(1) > .tw-flex")))
    driver.find_element(By.CSS_SELECTOR, ".btn-secondary:nth-child(1) > .tw-flex").click()
    
    # Wait for and click the card button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".card:nth-child(8) .btn")))
    driver.find_element(By.CSS_SELECTOR, ".card:nth-child(8) .btn").click()
    
    driver.find_element(By.NAME, "title").send_keys("asc")  # Use the name attribute for the title input
    driver.find_element(By.NAME, "title").send_keys(Keys.ENTER)  # Submit the input
    
    # Click the copy button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".tw-relative:nth-child(1) > .btn .scalable-icon")))
    driver.find_element(By.CSS_SELECTOR, ".tw-relative:nth-child(1) > .btn .scalable-icon").click()
    
    time.sleep(1)  # Short wait for clipboard to update
    
    # Get the copied text and write it to the console and the file
    copied_text = pyperclip.paste()  # Get the copied text from clipboard
    print(f"API: {copied_text}")  # Print the copied text to the console
    
    # Write the copied API to a file (append mode)
    with open('api.txt', 'a') as api_file:
        api_file.write(f"{copied_text}\n")
    
    # Jeda 5 detik
    time.sleep(5)
    
    # Tutup browser setelah satu email diproses
    driver.quit()
    
    # Tunggu sebentar sebelum mengulangi proses jika masih ada email
    time.sleep(2)

# Setelah semua email diproses, program selesai
print("Semua email selesai diproses.")
