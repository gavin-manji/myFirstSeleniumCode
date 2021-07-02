# install selenium and import webdriver
from selenium import webdriver
# Gives access to enter key and other related keys
from selenium.webdriver.common.keys import Keys
# to set specific time delays between tasks
import time
# imported By, WebDriverWait, expected_conditions  are used for the try and except part
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setting the path for the chromedriver
PATH = "C:\Program Files (x86)\chromedriver.exe"

# set-up the driver to use
driver = webdriver.Chrome(PATH)

# to maximize the browser window
driver.maximize_window()

# enter the webpage as shown below
driver.get("https://www.google.com/")

# to clearly see the title in the python console as a print statement
print(driver.title)

# searching the specific name in inspect in google.com - in this case searching the search box
find = driver.find_element_by_name("q")

# search in the search box
find.send_keys("Youtube")

# to get and print in entire source code in the python console uncomment the below line and print
# print(driver.page_source)

# click search or enter to search
find.send_keys(Keys.RETURN)


try:
    # Wait for 10 seconds until finding the element
    find2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "rcnt"))
    )
    print(find2.text)

except:
    # driver will quit here if only an exception is thrown
    driver.quit()


# If needed to keep the window for 7 seconds before going to next step
time.sleep(7)

# driver will quit after executing all above
driver.quit()
