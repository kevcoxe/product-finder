from core import crawler, scraper, utils
from html import unescape
import re
import pprint


def clean_price(price):
    price_contains_numbers = bool(re.search(r'[\d+,]+(\d+)', price))
    if price_contains_numbers:
        # split the price to remove the empty space and pick the first item
        price = unescape(price).split()[0]

    return price


def get_rtx_prices(tree):
    price_selector = "//li[contains(@class, 'price-current')]"
    price_text = scraper.get_text(tree, price_selector)
    return list(map(lambda price: clean_price(price), price_text))


def get_rtx_names(tree):
    name_selector = "//div[@class='item-info']/a"
    return scraper.get_text(tree, name_selector)


def get_rtx_links(tree):
    link_selector = "//div[@class='item-info']/a"
    return scraper.get_attributes(tree, link_selector, "href")


def get_rtx_stock_information(tree):
    item_selector = "//div[@class='item-container']"
    child_selector = "div[@class='item-info']/p[contains(., 'OUT OF STOCK')]"
    stock_details = scraper.get_children_text(
        tree, item_selector, child_selector)

    # set None to in stock, handles case when item has no "out of stock" label
    return list(map(lambda element: element or "IN STOCK", stock_details))


def get_rtx_ids(tree):
    item_id_selector = "//ul[@class='item-features']/li[contains(., 'Item #')]/text()"
    return scraper.get_nodes(tree, item_id_selector)


def get_rtx_items(tree):
    prices = get_rtx_prices(tree)
    names = get_rtx_names(tree)
    links = get_rtx_links(tree)
    ids = get_rtx_ids(tree)
    stock_details = get_rtx_stock_information(tree)
    items = []

    for index, price in enumerate(prices):
        try:
            name = names[index]
            link = links[index]
            stock = stock_details[index]
            id = ids[index]

            if stock == "IN STOCK":
                items.append({
                    'name': name,
                    'link': link,
                    'stock': stock,
                    'price': price,
                    'id': id
                })
        except:
            pass

    return items


crawler_urls = [
    {
        "name": "RTX 3000 cards",
        "url": "https://newegg.com/p/pl?PageSize=96&N=100007709%20601357282",
        "output_file": "rtx_3000_output"
    },
    {
        "name": "RX 6000 cards",
        "url": "https://www.newegg.com/p/pl?PageSize=96&N=100007709%20601359511",
        "output_file": "rx_6000_output"
    }
]

for item in crawler_urls:
    rtx_items = []
    html = crawler.crawl_html(item['url'])
    tree = scraper.get_tree(html)
    rtx_items = get_rtx_items(tree)

    # utils.write_to_csv(item['output_file'], rtx_items)

    pprint.pprint(rtx_items)
