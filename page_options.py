from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageOptions:
    def __init__(self, driver: WebDriver):
        """
        Set options for airbnb website.
        :param driver: selenium.webdriver
        """
        self.driver = driver

    def select_language_and_currency(self, your_country: str = 'United States', currency_code: str = 'USD') -> None:
        """
        Change language and currency for website. Language will be matched to your country.
        Parameter 'your_country' must be your country name in your native language.
        :param your_country: str
        :param currency_code: str
        :return: None
        """
        popup_window = self.driver.find_element(by=By.CSS_SELECTOR,
                                                value='button[class="c1jdlqzl c177491c dir dir-ltr"]')
        popup_window.click()

        available_languages = sorted([language.text[language.text.index('\n') + 1:] for language in
                                      self.driver.find_elements(by=By.CLASS_NAME, value='_obr3yz') if
                                      len(language.text) > 0] + ['United States', 'United Kingdom',
                                                                 'Indonesia',
                                                                 'Polska',
                                                                 'Azərbaycan'])

        if your_country in available_languages:
            for WebElement in self.driver.find_elements(by=By.CLASS_NAME, value='_lwi6c1u'):
                if your_country in WebElement.text:
                    WebElement.click()
                    break

        else:
            raise Exception(f"Language for {your_country} country is not available.")

        sleep(1)

        WebDriverWait(driver=self.driver, timeout=100).until(
            method=EC.presence_of_element_located(locator=(By.CSS_SELECTOR, 'span[class="_pgfqnw"]'))).click()

        currencies = self.driver.find_elements(by=By.CSS_SELECTOR, value='li[class="_obr3yz"]')

        for code in currencies:
            for element in code.find_elements(by=By.CSS_SELECTOR, value='div[class="_a7a5sx"]'):
                if currency_code in element.text:
                    code.click()

        sleep(1)
