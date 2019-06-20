from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1366,768")
        self.driver = webdriver.Chrome(executable_path='C:/Python/features/steps/webdrivers/chromedriver.exe',
                                       chrome_options=chrome_options)

    def get_element(self, xpath: str):
        """Метод получения вэб элемента по xpath

        Args:
            xpath: xpath

        Returns:
            element: вэб-элемент
        """
        try:
            element = WebDriverWait(driver=self.driver, timeout=20).until(
                expected_conditions.presence_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            element = self.driver.find_element(By.XPATH, xpath)
        return element

    def click(self, xpath):
        element = self.get_element(xpath=xpath)
        element.click()

    def fill_input(self, xpath, value):
        """Метод заполняет поле

        Args:
            xpath: xpath
            value: значение которым заполняется

        Returns:

        """

        element = self.get_element(xpath=xpath)
        element.send_keys(value)

    def clear_input(self, xpath):
        """Метод очистки поля ввода

        :param xpath: xpath
        """
        cleaner = self.get_element(xpath=xpath)
        cleaner.clear()

    def check_element(self, xpath: str):
        """Метод проверки вэб элемента по xpath

        Args:
            xpath: xpath

        Returns:
            element: вэб-элемент
        """

        self.driver = WebDriverWait(driver=self.driver, timeout=20).until(
            expected_conditions.presence_of_element_located((By.XPATH, xpath)))

        assert self.driver.find_element_by_xpath((By.XPATH, xpath))
        self.driver.quit()


    def quit_browser(self):
        self.driver.quit()
