from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
USERNAME = "whydoyouneedme_123"
PASSWORD = "Mummy@123"
options = Options()
options.add_argument("--start-maximized")  # Open browser in full screen

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)  # Wait for the login page to load

username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")

username_input.send_keys(USERNAME)
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.RETURN)

time.sleep(7)  # Wait for login to complete

# --- Visit CBITOSC Profile ---
search_url = "https://www.instagram.com/cbitosc/"
driver.get(search_url)
time.sleep(5)

# --- Click Follow Button (if not already following) ---
try:
    buttons = driver.find_elements(By.TAG_NAME, "button")
    for button in buttons:
        if button.text.lower() == "follow":
            button.click()
            print("✅ Followed cbitosc")
            time.sleep(2)
            break
    else:
        print("⚠️ Already following or Follow button not found")
except Exception as e:
    print(f"❌ Error clicking Follow button: {e}")


# --- Extract Profile Info (name and bio) ---
# --- Extract Name ---
try:
    profile_name = driver.find_element(By.TAG_NAME, "h2").text
except:
    profile_name = "Name not found"




# --- Write to output.txt ---
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(f"Profile: cbitosc\n")
    f.write(f"Name: {profile_name}\n")
   

# --- Done ---
driver.quit()
