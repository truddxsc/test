from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def sign_up_netlify(email):
    # Menyiapkan opsi untuk menjalankan Chrome dalam mode headless
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Aktifkan mode headless
    chrome_options.add_argument("--no-sandbox")  # Untuk meningkatkan stabilitas pada sistem tertentu
    chrome_options.add_argument("--disable-dev-shm-usage")  # Memperbaiki masalah pada kontainer

    # Membuka browser dan navigasi ke halaman sign up Netlify
    driver = webdriver.Chrome(service=Service(), options=chrome_options)  # Pastikan ChromeDriver ada di PATH sistem
    driver.get("https://app.netlify.com/signup")

    try:
        # Klik tombol 'Sign up with email'
        sign_up_with_email_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div/div/main/div/div/section/div/div[1]/div/p[1]/button"))
        )
        sign_up_with_email_button.click()

        # Isi email dari akun.txt
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        email_input.send_keys(email)

        # Isi password
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_input.send_keys("LeviYiyi123@")
        password_input.send_keys(Keys.ENTER)
        sleep(5)  # Tunggu beberapa detik hingga pendaftaran diproses

    except Exception as e:
        print(f"Error occurred during sign-up: {e}")
        driver.quit()

    return driver
