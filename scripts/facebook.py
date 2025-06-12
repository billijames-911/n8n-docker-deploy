from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def login_to_facebook():
    print("Starting Facebook automation process...")
    
    # Set up Chrome options
    print("Configuring Chrome options...")
    chrome_options = Options()
    
    # --- CRITICAL: Point to the browser binary in Alpine Linux ---
    chrome_options.binary_location = "/usr/bin/chromium-browser"
    
    # Add all necessary arguments for running in a headless environment
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    print("Initializing Chrome driver...")

    # --- THIS IS THE KEY CHANGE ---
    # The Service object will automatically find the chromedriver 
    # that we installed in the Dockerfile (/usr/bin/chromedriver).
    # We NO LONGER use ChromeDriverManager.
    service = Service()
    
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        print("Navigating to Facebook...")
        driver.get('https://www.facebook.com')
        
        print("Waiting for email field to load...")
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        
        print("Entering email address...")
        email_field.send_keys("your-email@example.com") # Use environment variables for credentials!
        print("Email entered successfully!")
        
        print("Entering password...")
        password_field = driver.find_element(By.ID, "pass")
        password_field.send_keys("YourStrongPassword") # Use environment variables for credentials!
        print("Password entered successfully!")
        
        print("Clicking login button...")
        login_button = driver.find_element(By.NAME, "login")
        login_button.click()
        
        print("Waiting for login process to complete...")
        # Instead of a fixed sleep, it's better to wait for a specific element on the next page
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[aria-label='Home']")))
        
        print("Login process completed successfully!")
        
    except Exception as e:
        # Save a screenshot for debugging if something goes wrong
        driver.save_screenshot("debug_screenshot.png")
        print(f"An error occurred: {str(e)}")
        
    finally:
        print("Closing browser...")
        driver.quit()
        print("Browser closed successfully!")

if __name__ == "__main__":
    login_to_facebook()