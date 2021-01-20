from .base_page import BasePage
from .locators import ImagesPageLocator


class ImagesPage(BasePage):
    def should_be_images_page(self, link):
        handle = self.browser.window_handles[-1]
        self.browser.switch_to.window(handle)
        url = self.browser.current_url
        assert link in url, 'Link should be for images page'

    def open_first_link_of_popular_category(self):
        category = self.browser.find_element(*ImagesPageLocator.POPULAR_CATEGORY)
        category.click()

    def should_be_image_for_click(self):
        assert self.is_element_showing_during_time(*ImagesPageLocator.IMAGE_IN_GALLERY)

    def open_first_image(self):
        image = self.browser.find_element(*ImagesPageLocator.IMAGE_IN_GALLERY)
        image.click()

    def should_open_image_in_slider(self):
        assert self.is_element_present(*ImagesPageLocator.SLIDER), 'Image was not open'

    def open_next_image(self):
        button = self.browser.find_element(*ImagesPageLocator.NEXT_SLIDER_BUTTON)
        button.click()
        image = self.browser.find_element(*ImagesPageLocator.IMAGE_HREF).get_attribute('src')
        return image

    def open_prev_image(self):
        button = self.browser.find_element(*ImagesPageLocator.PREV_SLIDER_BUTTON)
        button.click()
        image = self.browser.find_element(*ImagesPageLocator.IMAGE_HREF).get_attribute('src')
        return image

    def should_change_image_after_click(self):
        prev_image = self.browser.find_element(*ImagesPageLocator.IMAGE_HREF).get_attribute('src')
        next_image = self.open_next_image()
        assert prev_image != next_image, 'Images must be difference'
        next_image = self.open_prev_image()
        assert prev_image == next_image, 'After click back Image must be equal itself'
