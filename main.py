from crop_img import crop_img
from ocr import get_questions, get_text
from Actual_answers import get_answers

from PIL import Image
import io
import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from google import genai

client = genai.Client(api_key="AIzaSyDFYg6I3zuYjzrE1QQcMDG1yvoOQInUvXM")
try:
    driver = webdriver.Chrome()
    driver.get('https://pokedoku.com/')
    driver.fullscreen_window()
    time.sleep(2)
    driver.switch_to.active_element.send_keys(Keys.RETURN)
    time.sleep(3)
    
    # Take screenshot and crop
    screenshot = driver.get_screenshot_as_png()

    screenshot = Image.open(io.BytesIO(screenshot))

    cropped_image = crop_img(screenshot)
    cropped_image.save('ss.jpg')
    
    # Get text from image
    text_from_image = get_text(cropped_image,client)
    print("Text extracted from image:", text_from_image)
    
    # Process questions and get answers
    questions = get_questions(text_from_image,client)
    print("Questions:", questions)
    
    if not q:
        print("No questions extracted, check the image or OCR result")
        driver.quit()
        exit(1)
        
    a = get_answers(q)
    print("Answers:", a)
    
    # Input answers
    parent_div = driver.find_element(By.XPATH, "//div[@class='css-1yr34m6']")
    child_divs = parent_div.find_elements(By.XPATH, "./div")
    
    nums = [0,3,6,1,4,7,2,5,8]
    
    for i, j in zip(nums, range(9)):
        if j < len(a):  # Ensure we don't go out of bounds
            ActionChains(driver).move_to_element(child_divs[i]).click().send_keys(a[j]).perform()
            driver.switch_to.active_element.send_keys(Keys.TAB)
            driver.switch_to.active_element.send_keys(Keys.RETURN)
            driver.switch_to.active_element.send_keys(Keys.RETURN)
            time.sleep(2)
    
    time.sleep(100)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
