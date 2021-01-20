import pytest
from .pages.main_page import MainPage


link = 'https://yandex.ru/'


class TestSearchFromMainPage:

    @pytest.mark.smoke
    def test_find_with_search_line(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_search_line()
        page.input_text_to_search_line('4px Кострома')  # Запрос, вводимый, в поисковой строке
        page.should_be_suggest_list()
        page.go_to_result_in_search_line()
        page.should_be_search_result_ul()
        page.should_first_count_result_is_text('4px.ru', 1)
        # Текст искомой ссылки, сколько результатов от начала выдачи проверяем на соответствие
