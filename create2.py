import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import re
import os.path
import base64
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Scopes untuk mengakses Gmail API
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_gmail_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    service = build('gmail', 'v1', credentials=creds)
    return service

def get_verification_link_from_email(service, query):
    results = service.users().messages().list(userId='me', q=query).execute()
    messages = results.get('messages', [])
    
    if not messages:
        print('No messages found.')
        return None

    for message in messages:
        msg = service.users().messages().get(userId='me', id=message['id']).execute()
        payload = msg.get('payload', {})
        
        if 'parts' in payload:
            for part in payload['parts']:
                if part['mimeType'] == 'text/html':
                    data = part['body']['data']
                    decoded_data = base64.urlsafe_b64decode(data).decode('utf-8')
                    link = re.search(r'href="(https://app\.netlify\.com/signup[^"]+)', decoded_data)
                    if link:
                        return link.group(1)
        else:
            if 'body' in payload and 'data' in payload['body']:
                data = payload['body']['data']
                decoded_data = base64.urlsafe_b64decode(data).decode('utf-8')
                link = re.search(r'href="(https://app\.netlify\.com/signup[^"]+)', decoded_data)
                if link:
                    return link.group(1)

    return None

def generate_random_name(length=6):
    # Generate random lowercase letters of specified length
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def get_email_from_file(file_path):
    with open(file_path, 'r') as file:
        emails = file.readlines()
    
    return [email.strip() for email in emails if email.strip()]  # Return non-empty emails

def clean_email(email):
    return email.split('@')[0].replace('+', '-').replace('.', '-')

def sign_up_netlify(email):
    driver = webdriver.Chrome()  # Pastikan ChromeDriver ada di PATH sistem
    driver.get("https://app.netlify.com/signup")

    try:
        sign_up_with_email_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div/div/main/div/div/section/div/div[1]/div/p[1]/button"))
        )
        sign_up_with_email_button.click()

        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        email_input.send_keys(email)

        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_input.send_keys("LeviYiyi123@")
        password_input.send_keys(Keys.ENTER)
        sleep(5)

    except Exception as e:
        print(f"Error occurred during sign-up: {e}")
        driver.quit()

    return driver

def verify_netlify_account(driver):
    service = get_gmail_service()
    verification_link = None
    for _ in range(30):  
        verification_link = get_verification_link_from_email(service, 'from:team@netlify.com')
        if verification_link:
            print(f'Link verifikasi ditemukan: {verification_link}')
            break
        print("Menunggu link verifikasi...")
        sleep(1)

    if verification_link:
        driver.get(verification_link)
        print("Akun berhasil diverifikasi!")
    else:
        print('Link verifikasi tidak ditemukan.')

def fill_in_additional_details(driver, email):
    sleep(10)
    modified_email = clean_email(email)
    url = f"https://app.netlify.com/teams/{modified_email}/sites"
    driver.get(url)
    sleep(5)
    driver.quit()

if __name__ == '__main__':
    generated_emails = []
    
    # Buat 10 email acak
    for _ in range(10):
        random_name = generate_random_name()
        new_email = f"mr.platra10+{random_name}@butyusa.com"
        generated_emails.append(new_email)
        
        # Simpan email baru ke dalam file test.txt
        with open('test.txt', 'a') as file:
            file.write(f"{new_email}\n")
        
        print(f"Email generated: {new_email}")

    # Mulai proses pendaftaran dan verifikasi
    for email in generated_emails:
        print(f"Processing email: {email}")
        driver = sign_up_netlify(email)
        verify_netlify_account(driver)
        fill_in_additional_details(driver, email)
        sleep(10)
