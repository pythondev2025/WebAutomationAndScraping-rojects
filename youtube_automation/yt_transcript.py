from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def main():
    data_list = extract_data()
    save_transcript(data_list)
    
    
def extract_data():
    browser = webdriver.Firefox()
    page = browser.get("https://www.youtube.com/watch?v=EOLPQdVj5Ac&t=3088s")
    
    time.sleep(5)
    more_button = browser.find_element(By.ID, "expand")
    more_button.click()
    
    time.sleep(2)


    # prev_height = browser.execute_script("return document.body.scrollHeight")
    
    # while True:
    #     browser.execute_script("window.scrollBy(0, window.innerHeight);")
        
    #     current_height = browser.execute_script("return document.body.scrollHeight")
    #     time.sleep(5)

    #     if show_transcript.is_displayed():    
    #         show_transcript.click()
    #         break
        
        # returns the current height of the page and used to check afterwards if we reached the bottom of the 
        # # page
        # elif current_height == prev_height:
        #     print("bottom of the page")
        #     break
    browser.execute_script("window.scrollBy(0, window.innerHeight);")
    browser.execute_script("window.scrollBy(0, window.innerHeight);")
    browser.execute_script("window.scrollBy(0, window.innerHeight);")
    browser.execute_script("window.scrollBy(0, window.innerHeight);")
    browser.execute_script("window.scrollBy(0, window.innerHeight);")

    time.sleep(5)
    show_transcript = browser.find_element(By.CSS_SELECTOR, 
                                           "ytd-video-description-transcript-section-renderer.style-scope:nth-child(4) > div:nth-child(3) > div:nth-child(1) > ytd-button-renderer:nth-child(1) > yt-button-shape:nth-child(1) > button:nth-child(1) > yt-touch-feedback-shape:nth-child(2) > div:nth-child(1) > div:nth-child(2)")
    time.sleep(1)
    show_transcript.click()
    
    time.sleep(5)
    
    transcript_list = browser.find_elements(By.XPATH, "//yt-formatted-string[@class='segment-text style-scope ytd-transcript-segment-renderer']")
    return transcript_list


def save_transcript(data):
    with open("transcript.txt", "w") as file:
        for para_elem in data:
            file.writelines(para_elem.text + "\n")


if __name__ == "__main__":
    main()
    