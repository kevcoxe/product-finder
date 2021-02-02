"""
This module can be used to find items on best buy
and return a list of links that are within your price bracket
"""
import os
import time
import pprint

from dotenv import load_dotenv
from selenium import webdriver


load_dotenv(verbose=True)

CHROME_DRIVER_PATH = os.getenv('CHROME_DRIVER_PATH', '/usr/local/bin/chromedriver')


class BestBuySearch:
    """ Best Buy """

    found_items = []

    def __init__(self, search_url, target_price, wiggle_room=0.05, number_of_tries=5, time_between_searches=10):
        """ """
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")

        self.search_url = search_url
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH, chrome_options=chrome_options)
        self.target_price = target_price
        self.wiggle_room = wiggle_room
        self.number_of_tries = number_of_tries
        self.time_between_searches = time_between_searches

    def get_items(self):
        """ Get a list of items with prices """
        self.driver.get(self.search_url)

        # get list of cards from listing
        item_list = self.driver.find_element_by_class_name("sku-item-list")
        for item in item_list.find_elements_by_tag_name("li")[1:]:
            try:
                inventory_status = item.find_element_by_class_name("sku-list-item-button").text
                if "sold out" in inventory_status.lower() or "coming soon" in inventory_status.lower():
                    continue
            except:
                continue

            # check the price of the card
            try:
                price_div = item.find_element_by_class_name("priceView-customer-price")
                price_element = price_div.find_element_by_tag_name("span")
                price = price_element.text.strip()[1:].replace(',', '')
                computed_price = float(price)
                if computed_price > (self.target_price * (1 + self.wiggle_room)):
                    print(f"too expensive: {computed_price}")
                    continue
            except:
                continue

            # get link
            try:
                anchor_tag = item.find_element_by_class_name('image-link')
                link = anchor_tag.get_attribute("href")
                self.found_items.append((link, computed_price))
            except:
                continue

    def search(self):
        """  """
        search_count = 0
        while len(self.found_items) <= 0 and search_count < self.number_of_tries:
            self.get_items()
            search_count = search_count + 1
            time.sleep(self.time_between_searches)

        # display results
        pprint.pprint(self.found_items)

    def buy_item(self, address_info, billing_info):
        """ buy item """
        pass

    def close(self):
        """ """ 
        self.driver.close()
        self.driver.quit()
