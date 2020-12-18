import time
import math
from selenium import webdriver

link = 'http://suninjuly.github.io/execute_script.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = int(browser.find_element_by_id('input_value').text)
    answer = str(math.log(abs(12*math.sin(x_element))))
    answer_input = browser.find_element_by_id('answer').send_keys(answer)
    button = browser.find_element_by_css_selector('button.btn.btn-primary')
    browser.execute_script("document.getElementsByClassName('form-check-label')[0].scrollIntoView(true);")
    checkbox = browser.find_element_by_id('robotCheckbox').click()
    radio_button = browser.find_element_by_css_selector('label[for="robotsRule"]').click()
    button.click()


finally:
    time.sleep(5)
    browser.quit()