from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys


# setting the browser/driver
browser = webdriver.Firefox()
browser.get("https://trello.com/")
time.sleep(5)

# clicking on login
login_elem = browser.find_element(By.LINK_TEXT, "Log in")
login_elem.click()

# clicking for email
email_elem = WebDriverWait(browser, 10).until(
    expected_conditions.visibility_of_element_located((By.ID, "username"
                                                       )))
email_elem.click()

# entering email
email_elem.send_keys("automationtasks12@gmail.com")
email_elem.submit()

# entering password
time.sleep(5)
pass_elem = browser.find_element(By.ID, "password")
pass_elem.send_keys("qwerty_12345_automation")
pass_elem.submit()

"""
_2fa_elem = browser.find_element(By.CSS_SELECTOR, "#mfa-promote-dismiss > span:nth-child(1)")
_2fa_elem.click()

browser.implicitly_wait(5)
"""

# scrolling down to find page
time.sleep(10)
pg_down = browser.find_element(By.TAG_NAME, "html")
pg_down.send_keys(Keys.PAGE_DOWN)

# selecting te board
board_elem = WebDriverWait(browser, 10).until(
    expected_conditions.element_to_be_clickable((
        By.XPATH, '//div[@class="DIkCJzvVP3VODq"]'
    )))
board_elem.click()

# clicking to add board
browser.implicitly_wait(5)
add_card = browser.find_element(By.XPATH, "//button[@data-testid='list-add-card-button']")
add_card.click()

# entering card name
click_card = browser.find_element(By.XPATH, "//textarea[@placeholder='Enter a title or paste a link']")
click_card.send_keys("Newly created card")
click_card.submit()

# selecting element for screenshot
browser.implicitly_wait(3)
snap_elem = browser.find_element(By.XPATH, "//ol[@id='board']")

# saving screenshot of full pages
browser.save_screenshot("whole_window_ss.png")
browser.save_full_page_screenshot("Full_page_Screenshot.png")

# saving screenshot of element
snap_elem.screenshot("element_screenshot.png")

# clicking created element for description
select_card = browser.find_element(By.LINK_TEXT, "Newly created card")
select_card.click()

# clicking on description element
time.sleep(3)
des_elem = browser.find_element(By.CSS_SELECTOR, ".css-1y6z04t")
des_elem.click()

# writing description
write_des = browser.find_element(By.ID, "ak-editor-textarea")
write_des.send_keys("Here is the complete detail of the card which is entered just now hahaha.")

# saving description
save_elem = browser.find_element(By.XPATH, "//button[@data-testid='description-save-button']")
save_elem.click()

# saving the final screenshot
page_up_elem = browser.find_element(By.TAG_NAME, "html")
page_up_elem.send_keys(Keys.PAGE_UP)
final_snap = browser.find_element(By.CSS_SELECTOR, ".NauH5zhD2hZvpP")
final_snap.screenshot("Final_screenshot.png")
