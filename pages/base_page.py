from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from .locators import BasePageLocators
from selenium.webdriver.common.keys import Keys


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_element_showing_during_time(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=1):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def go_to_images_page(self):
        images_link = self.browser.find_element(*BasePageLocators.IMAGES_LINK)
        images_link.click()

    def go_to_result_in_search_line(self):
        line = self.browser.find_element(*BasePageLocators.SEARCH_LINE)
        line.send_keys(Keys.ENTER)

    def should_be_images_page_link(self):
        assert self.is_element_present(*BasePageLocators.IMAGES_LINK), 'Link for Images page not found'

    def should_be_search_line(self):
        assert self.is_element_present(*BasePageLocators.SEARCH_LINE), 'Search line not found'

    def input_text_to_search_line(self, text):
        line = self.browser.find_element(*BasePageLocators.SEARCH_LINE)
        line.send_keys(text)
