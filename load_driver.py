import os
from time import sleep
from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.common.by import By


class Driver(Firefox):
    def __init__(self, path: str = '/Users/admin/PycharmProjects/pythonProject/Airbnb Booking Automation Project',
                 teardown: bool = False):
        self.path = path
        self.teardown = teardown
        os.environ['PATH'] = self.path
        super(Driver, self).__init__()
        self.set_window_size(width=2880, height=1800)
        self.implicitly_wait(time_to_wait=100)
        self.maximize_window()

    def load_page(self) -> None:
        """
        Load home page.
        :return: None
        """
        self.get(url='https://www.airbnb.com')
        sleep(1)

    def accept_cookies(self) -> None:
        """
        Accept all cookies.
        :return: None
        """
        sleep(2)
        self.find_element(by=By.CSS_SELECTOR, value='button[class="_148dgdpk"]').click()
        sleep(1)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
