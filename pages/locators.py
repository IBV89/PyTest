from selenium.webdriver.common.by import By


class BasePageLocators():
    SEARCH_LINE = (By.CSS_SELECTOR, 'input[name="text"]')
    IMAGES_LINK = (By.CSS_SELECTOR, 'a[data-id="images"]')


class MainPageLocators():
    SUGGEST_LIST = (By.CSS_SELECTOR, 'ul[role="listbox"]')
    SEARCH_RESULT = (By.ID, 'search-result')
    RESULT_LINK = (By.CSS_SELECTOR, 'a.organic__url')


class ImagesPageLocator():
    POPULAR_CATEGORY = (By.CSS_SELECTOR, 'a.Link.PopularRequestList-Preview')
    IMAGE_IN_GALLERY = (By.CSS_SELECTOR, 'a.serp-item__link')
    IMAGE_HREF = (By.CSS_SELECTOR, 'img.MMImage-Preview')
    SLIDER = (By.CSS_SELECTOR, 'div.Modal_visible')
    NEXT_SLIDER_BUTTON = (By.CSS_SELECTOR, 'div.CircleButton_type_next')
    PREV_SLIDER_BUTTON = (By.CSS_SELECTOR, 'div.CircleButton_type_prev')
