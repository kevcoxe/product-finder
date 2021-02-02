"""
This module can be used to find items on best buy
and return a list of links that are within your price bracket
"""
import os
import time
import pprint

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException


load_dotenv(verbose=True)

CHROME_DRIVER_PATH = os.getenv('CHROME_DRIVER_PATH', '/usr/local/bin/chromedriver')

class NewEggSearch:
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
        # clear popup
        try:
            popup_window = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "centerPopup-body"))
            )
            close_popup_button = popup_window.find_element_by_class_name("centerPopup-close")
            close_popup_button.click()
        except ElementNotInteractableException:
            pass
        except Exception:
            return

        # get list of cards from listing
        item_list = self.driver.find_elements_by_class_name("item-cell")
        for item in item_list:
            try:
                inventory_status = item.find_element_by_class_name("item-promo").text
                if "out of stock" in inventory_status.lower():
                    continue
            except Exception as e:
                try:
                    buy_button_text = item.find_element_by_class_name("item-button-area").text.strip()
                    if "add to cart" not in buy_button_text.lower():
                       continue 
                except:
                    continue

            # check the price of the card
            try:
                price_div = item.find_element_by_class_name("price-current")
                price_dollars = price_div.find_element_by_tag_name('strong').text.strip().replace(',', '')
                price_cents = price_div.find_element_by_tag_name('sup').text.strip()
                str_price = f"{price_dollars}{price_cents}"
                computed_price = float(str_price)
                if computed_price > (self.target_price * (1 + self.wiggle_room)):
                    print(f"too expensive: {computed_price}")
                    continue
            except Exception as e:
                print(f'EXCEPTION: {e}')
                continue

            # get link
            try:
                anchor_tag = item.find_element_by_class_name('item-title')
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
