from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class FilterBar:
    def __init__(self, driver: WebDriver):
        """
        Select filters for apartments what you search.
        :param driver: selenium.webdriver
        """
        self.driver = driver

    def select_filters(self) -> None:
        """
        Select filters button.
        :return: None
        """
        sleep(1)
        wait = WebDriverWait(driver=self.driver, timeout=10).until(
            method=EC.element_to_be_clickable(mark=(By.CSS_SELECTOR, 'button[class="c1tureqs dir dir-ltr"]')))
        self.driver.find_element(by=By.CSS_SELECTOR, value='button[class="c1tureqs dir dir-ltr"]').click()

    def clear_filters(self):
        self.driver.find_element(by=By.CSS_SELECTOR, value='button[class="_za4ekfm"]').click()

    def select_price_range(self, min_price: int = 300, max_price: int = 5000) -> None:
        """
        Filter offers between minimum price and maximum price of apartment.
        :param min_price: int
        :param max_price: int
        :return: None
        """
        low_price = self.driver.find_element(by=By.ID, value='price_filter_min')
        low_price.click()

        for _ in range(len(low_price.get_attribute(name='value'))):
            low_price.send_keys(Keys.BACKSPACE)

        low_price.send_keys(min_price)

        high_price = self.driver.find_element(by=By.ID, value='price_filter_max')
        high_price.click()

        for _ in range(len(high_price.get_attribute(name='value'))):
            high_price.send_keys(Keys.BACKSPACE)

        high_price.send_keys(max_price)

    def select_kind_of_places(self, *kind_of_places: str) -> None:
        """
        Choose kind of place. Available kind of places are 'Entire place', 'Private room', 'Shared room'.
        :param kind_of_places: str
        :return: None
        """
        available_places = [element.text[:element.text.find('\n')] for element in
                            self.driver.find_elements(by=By.CLASS_NAME, value='_gfomxi')][0:3]

        for place in kind_of_places:
            if place in available_places:
                for WebElement in self.driver.find_elements(by=By.CLASS_NAME, value='_gfomxi'):
                    if place in WebElement.text:
                        WebElement.click()
            else:
                raise Exception(f"{place} is not available. Available places are "
                                f"'Entire place', 'Private room', 'Shared room'.")

    def select_rooms(self, number_of_rooms: int = 1) -> None:
        """
        Choose number of rooms in apartment.
        :param number_of_rooms: int
        :return: None
        """
        self.driver.find_elements(by=By.ID, value=f'menuItemButton-{number_of_rooms}')[0].click()

    def select_beds(self, number_of_beds: int = 1) -> None:
        """
        Choose number of beds in apartment.
        :param number_of_beds: int
        :return: None
        """
        self.driver.find_elements(by=By.ID, value=f'menuItemButton-{number_of_beds}')[1].click()

    def select_bathrooms(self, number_of_bathrooms: int = 1) -> None:
        """
        Choose number of bathrooms in apartment.
        :param number_of_bathrooms: int
        :return: None
        """
        self.driver.find_elements(by=By.ID, value=f'menuItemButton-{number_of_bathrooms}')[2].click()

    def select_property_types(self, *property_types) -> None:
        """
        Choose type of property like 'House', 'Apartment', 'Guesthouse', 'Hotel'.
        :param type: str
        :return: None
        """
        available_property_types = [kind.text for kind in self.driver.find_elements(by=By.CLASS_NAME, value='_w7zj3g')
                                    if len(kind.text) > 0]

        for kind in property_types:
            if kind in available_property_types:
                for WebElement in self.driver.find_elements(by=By.CLASS_NAME, value='_w7zj3g'):
                    if kind in WebElement.text:
                        WebElement.click()
            else:
                raise Exception(f"{kind} is not available. Available property types are "
                                f"'House', 'Apartment', 'Guesthouse', 'Hotel'.")

    def select_show_more_for_amelities(self):
        """
        Expand down show more button for see all available amelities.
        :return:
        """
        self.driver.find_element(by=By.CSS_SELECTOR, value='button[class="_edqkt1v"]').click()

    def select_amenities(self, *amenities: str) -> None:
        """
        Choose amenity for apartment. Amenities you can choose are 'Wifi', 'Kitchen', 'Washes', 'Dryer',
        'Air conditioning', 'Heating', 'Dedicated workspace', 'TV', 'Hair dryer', 'Iron'.
        :param amenity: str
        :return: None
        """
        available_amenities = [amenity.text for amenity in
                               self.driver.find_elements(by=By.CLASS_NAME, value='_gw4xx4')][3:13]

        for amenity in amenities:
            if amenity in available_amenities:
                for WebElement in self.driver.find_elements(by=By.CLASS_NAME, value='_gw4xx4'):
                    if amenity in WebElement.text:
                        WebElement.click()
            else:
                raise Exception(
                    f"{amenity} is not available. Available amenities are 'Wifi', 'Kitchen', 'Washes', 'Dryer', "
                    f"'Air conditioning', 'Heating', 'Dedicated workspace', 'TV', 'Hair dryer', 'Iron'")

    def select_additional_amenities(self, *additional_amenities: str) -> None:
        """
        Choose apartment functions like 'Pool', 'Hot tub', 'Free parking on premises', 'EV charger', 'Crib', 'Gym',
        'BBQ grill', 'Breakfast', 'Indoor fireplace', 'Smoking allowed'.
        :param functions: str
        :return: None
        """
        available_additional_amenities = [additional_amenity.text for additional_amenity in
                                          self.driver.find_elements(by=By.CLASS_NAME, value='_gfomxi')][13:23]

        for additional_amenity in additional_amenities:
            if additional_amenity in available_additional_amenities:
                for WebElement in self.driver.find_elements(by=By.CLASS_NAME, value='_gfomxi'):
                    if additional_amenity in WebElement.text:
                        WebElement.click()
            else:
                raise Exception(
                    f"{additional_amenity} is not available. Available additional amenities are "
                    f"'Pool', 'Hot tub', 'Free parking on premises', 'EV charger', 'Crib', 'Gym', "
                    f"'BBQ grill', 'Breakfast', 'Indoor fireplace', 'Smoking allowed'")

    def select_locations(self, *locations: str) -> None:
        """
        Choose apartment location like 'Beachfront', 'Waterfront', 'Ski-in/ski-out'.
        :param locations: str
        :return: None
        """
        available_locations = [location.text for location in
                               self.driver.find_elements(by=By.CLASS_NAME, value='_gw4xx4')][23:26]

        for location in locations:
            if location in available_locations:
                for WebElement in self.driver.find_elements(by=By.CLASS_NAME, value='_gw4xx4'):
                    if location in WebElement.text:
                        WebElement.click()
            else:
                raise Exception(f"{location} is not available. Available locations are "
                                f"'Beachfront', 'Waterfront', 'Ski-in/ski-out'.")

    def select_safeties(self, *safeties: str) -> None:
        """
        Choose security for apartment like 'Smoke alarm', 'Carbon monoxide alarm'.
        :param safeties: str
        :return: None
        """
        available_security = [sec.text for sec in self.driver.find_elements(by=By.CLASS_NAME, value='_gfomxi')][26:28]

        for s in safeties:
            if s in available_security:
                for WebElement in self.driver.find_elements(by=By.CLASS_NAME, value='_gfomxi'):
                    if s in WebElement.text:
                        WebElement.click()
            else:
                raise Exception(f"{s} is not available. Available security are 'Smoke alarm', 'Carbon monoxide alarm'.")

    def select_booking_options(self, *options: str) -> None:
        """
        Choose reservation options like 'Instant Book', 'Self check-in'.
        :param options: str
        :return: None
        """
        available_options = [option.text for option in self.driver.find_elements(by=By.CLASS_NAME, value='_jro6t0')][
                            29:31]

        for option in options:
            if option in available_options:
                if option == 'Instant Book':
                    self.driver.find_element(by=By.CLASS_NAME, value='_1vmcy00').click()
                elif option == 'Self check-in':
                    self.driver.find_elements(by=By.CLASS_NAME, value='_1vmcy00')[1].click()
            else:
                raise Exception(f"{option} is not available. Available options are 'Instant Book', 'Self check-in'")

    def select_high_quality_places(self, superhost: bool = False, airbnb_plus=False) -> None:
        """
        If superhost is True, Airbnb will display only trusted hosts otherwise Airbnb will display you all hosts.
        If airbnb_plus is True, Airbnb will display verified and high quality places.
        :param superhost: bool
        :param airbnb_plus: bool
        :return: None
        """
        if superhost:
            self.driver.find_elements(by=By.CLASS_NAME, value='_1vmcy00')[2].click()

        if airbnb_plus:
            self.driver.find_elements(by=By.CLASS_NAME, value='_1vmcy00')[3].click()

    def select_show_more_for_languages(self):
        """
        Expand down show more button to see all available languages.
        :return: None
        """
        self.driver.find_elements(by=By.CLASS_NAME, value='_edqkt1v')[2].click()

    def select_host_language(self, *languages: str) -> None:
        """
        Choose language/languages which you want to talk with host. Available languages are 'English', 'French',
        'German', 'Japanese', 'Italian', 'Russian', 'Spanish', 'Chinese', 'Arabic', 'Portuguese', 'Turkish',
        'Indonesian', 'Dutch', 'Thai', 'Greek', 'Sign', 'Hebrew', 'Polish', 'Tagalog', 'Danish', 'Swedish',
        'Norwegian', 'Finnish', 'Czech', 'Hungarian', 'Ukrainian'.
        :param languages: str
        :return: None
        """
        available_languages = list(map(lambda x: x[:x.find('(')].strip() if '(' in x else x, [lang.text for lang in
                                                                                              self.driver.find_elements(
                                                                                                  by=By.CLASS_NAME,
                                                                                                  value='_gfomxi')]))[
                              32:59]

        for language in languages:
            if language in available_languages:
                for WebElement in self.driver.find_elements(by=By.CLASS_NAME, value='_gfomxi'):
                    if language in WebElement.text:
                        WebElement.click()
            else:
                raise Exception(
                    f"{language} not available. Available languages are 'English', 'French', 'German', 'Japanese', "
                    f"'Italian', 'Russian', 'Spanish', 'Chinese', 'Arabic', 'Portuguese', 'Turkish', 'Indonesian', "
                    f"'Dutch', 'Thai', 'Greek', 'Sign', 'Hebrew', 'Polish', 'Tagalog', 'Danish', 'Swedish', "
                    f"'Norwegian', 'Finnish', 'Czech', 'Hungarian', 'Ukrainian'")

    def get_offers(self) -> None:
        """
        Display all offers with chosen filters.
        :return: None
        """
        self.driver.get(
            url=self.driver.find_element(by=By.CSS_SELECTOR, value='a[class="_1ku51f04"]').get_attribute(name='href'))
