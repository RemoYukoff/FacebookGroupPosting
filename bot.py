from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

email="USER"
password="PASS"

options = Options()  
options.add_argument("--headless")
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=options)
driver.get("https://www.facebook.com/login")

# Login
elem=driver.find_element_by_id("email")
elem.send_keys(email)
elem=driver.find_element_by_id("pass")
elem.send_keys(password)
elem=driver.find_element_by_id("loginbutton")
elem.send_keys(Keys.ENTER)

# The ids appear in the url of the group https://www.facebook.com/groups/<HERE IS THE ID>
with open("groups.txt","r") as file:
    groups=file.read()
    groups = groups.split("\n")

# Post message
with open("message.txt","r") as file:
    message=file.read()

for id in groups:
    driver.get(f"https://www.facebook.com/groups/{id}/")
    elem = driver.find_elements_by_tag_name("textarea")[1]
    elem.click()
    # Something change on facebook and need to wait a moment
    time.sleep(2)
    # Write the post
    driver.switch_to.active_element.send_keys(message)
    time.sleep(1)
    driver.switch_to.active_element.send_keys(Keys.ENTER)
    time.sleep(5)
    while True:
        try:
            # Publish button, need to wait until appears
            elem = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[3]/div/div[2]/div/div[2]/button')
            break
        except Exception as e:
            print(e)
            print("Button not found")
            pass
    elem.click()
    # Wait for the post to be sended
    time.sleep(5)

driver.quit()