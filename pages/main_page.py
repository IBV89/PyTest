from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def should_be_suggest_list(self):
        assert self.is_element_present(*MainPageLocators.SUGGEST_LIST)

    def should_be_search_result_ul(self):
        assert self.is_element_present(*MainPageLocators.SEARCH_RESULT)

    def should_first_count_result_is_text(self, text, count):
        links = self.browser.find_elements(*MainPageLocators.RESULT_LINK)
        for link in links[:count]:
            a_link = link.get_attribute('href')
            assert text in a_link, 'First results not is count'

