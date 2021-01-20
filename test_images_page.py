import pytest
from .pages.main_page import MainPage
from .pages.images_page import ImagesPage

link = 'https://yandex.ru/'


class TestSliderForImagesPage:
    def test_show_pictures_in_images_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_images_page_link()
        page.go_to_images_page()
        images_page = ImagesPage(browser, browser.current_url)
        images_page.should_be_images_page('https://yandex.ru/images/')
        images_page.open_first_link_of_popular_category()
        images_page.should_be_image_for_click()
        images_page.open_first_image()
        images_page.should_open_image_in_slider()
        images_page.should_change_image_after_click()


