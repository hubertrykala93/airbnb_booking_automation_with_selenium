from time import sleep
import datetime as dt
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SearchBar:
    def __init__(self, driver: WebDriver):
        """
        Select localization, date and number of people for apartment what you want to find.
        :param driver: selenium.webdriver
        """
        self.driver = driver

    def select_location(self, location: str = 'Nowy Jork'):
        """
        Choose travel destination.
        :param location: str
        :return: None
        """
        self.driver.find_element(by=By.CSS_SELECTOR, value='button[class="f19g2zq0 dir dir-ltr"]').click()
        sleep(1)
        self.driver.find_element(by=By.ID, value='bigsearch-query-location-input').clear()
        sleep(1)
        place_to = self.driver.find_element(by=By.ID, value='bigsearch-query-location-input')
        place_to.send_keys(location)
        sleep(1)

        self.driver.find_element(by=By.CSS_SELECTOR, value='div[data-testid="option-0"]').click()
        sleep(1)

    def select_dates(self, start: str = dt.date.today().strftime('%d.%m.%Y'), end=None) -> None:
        """
        Choose start and end your trip. Date must have format like '25.10.2022' with separator '.'.
        :param start: str
        :param end: str
        :return: None
        """
        if not end:
            raise Exception('You have choose end date.')
        else:
            self.driver.find_element(by=By.CSS_SELECTOR, value=f'div[data-testid="calendar-day-{start}"]').click()
            self.driver.find_element(by=By.CSS_SELECTOR, value=f'div[data-testid="calendar-day-{end}"]').click()

    def select_adults(self, number_of_adults: int = 1) -> None:
        """
        Choose number of adults.
        :param number_of_adults: int
        :return: None
        """
        element = self.driver.find_element(by=By.CSS_SELECTOR,
                                           value='div[data-testid="structured-search-input-field-guests-button"]')
        element.click()
        sleep(1)

        for _ in range(number_of_adults):
            self.driver.find_element(by=By.CSS_SELECTOR,
                                     value='button[data-testid="stepper-adults-increase-button"]').click()
        sleep(1)

        element.send_keys(Keys.ESCAPE)
        sleep(1)

    def select_children(self, number_of_children: int = 0) -> None:
        """
        Choose number of children.
        :param number_of_children: int
        :return: None
        """
        self.driver.find_element(by=By.CSS_SELECTOR,
                                 value='div[data-testid="structured-search-input-field-guests-button"]').click()
        sleep(1)

        for _ in range(number_of_children):
            self.driver.find_element(by=By.CSS_SELECTOR,
                                     value='button[data-testid="stepper-children-increase-button"]').click()
        sleep(1)

    def select_newborns(self, number_of_newborns: int = 0) -> None:
        """
        Choose number of newborns.
        :param number_of_newborns: int
        :return: None
        """
        self.driver.find_element(by=By.CSS_SELECTOR,
                                 value='div[data-testid="structured-search-input-field-guests-button"]').click()
        sleep(1)

        for _ in range(number_of_newborns):
            self.driver.find_element(by=By.CSS_SELECTOR,
                                     value='button[data-testid="stepper-infants-increase-button"]').click()
        sleep(1)

    def select_pets(self, number_of_pets: int = 0) -> None:
        """
        Choose number of pets.
        :param number_of_pets: int
        :return: None
        """
        self.driver.find_element(by=By.CSS_SELECTOR,
                                 value='div[data-testid="structured-search-input-field-guests-button"]').click()
        sleep(1)

        for _ in range(number_of_pets):
            self.driver.find_element(by=By.CSS_SELECTOR,
                                     value='button[data-testid="stepper-pets-increase-button"]').click()
        sleep(1)

    def select_search(self) -> None:
        """
        Click search bar and find results of selected parameters.
        :return: None
        """
        self.driver.find_element(by=By.CSS_SELECTOR,
                                 value='button[data-testid="structured-search-input-search-button"]').click()
        sleep(1)
