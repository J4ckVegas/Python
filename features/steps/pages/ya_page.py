from features.steps.pages.base_page import BasePage


class MainYaPage(BasePage):

    INPUT_SEARCH = '//input[@class="input__control input__input"]'
    INPUT_SEARCH_WithText = '//input[@class="input__control"]'
    BUTTON_SEARCH = '//span[text()="Найти"]/ancestor::button'
    BUTTON_SEARCH_WithText = '//div[text()="Найти"]/ancestor::button'
    IMG_ON_IMAGE_PAGE = '//img[@class ="serp-item__thumb justifier__thumb"]'

'//span[text()="Картинки"]/ancestor::button'
