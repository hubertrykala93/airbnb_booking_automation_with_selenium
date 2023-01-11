from load_driver import Driver
from page_options import PageOptions
from search_bar import SearchBar
from filter_bar import FilterBar


def main():
    driver = Driver(teardown=True)
    page_options = PageOptions(driver=driver)
    search_bar = SearchBar(driver=driver)
    filter_bar = FilterBar(driver=driver)

    driver.load_page()
    driver.accept_cookies()

    page_options.select_language_and_currency(your_country='United States', currency_code='USD')

    filter_bar.select_filters()
    filter_bar.select_price_range(min_price=100, max_price=500)
    filter_bar.select_kind_of_places('Entire place')
    filter_bar.select_rooms(number_of_rooms=2)
    filter_bar.select_beds(number_of_beds=1)
    filter_bar.select_bathrooms(number_of_bathrooms=1)
    filter_bar.select_property_types('Apartment')
    filter_bar.select_show_more_for_amelities()
    filter_bar.select_amenities('Kitchen', 'Wifi')
    filter_bar.select_additional_amenities()
    filter_bar.select_locations()
    filter_bar.select_safeties()
    filter_bar.select_booking_options('Instant Book')
    filter_bar.select_high_quality_places(superhost=False, airbnb_plus=False)
    filter_bar.select_show_more_for_languages()
    filter_bar.select_host_language('Polish')
    filter_bar.get_offers()

    search_bar.select_location(location='Kanada')
    # search_bar.select_dates(start='01.11.2022', end='04.11.2022')
    # search_bar.select_adults(number_of_adults=1)
    # search_bar.select_search()


if __name__ == '__main__':
    main()
