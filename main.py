
from modules.bestBuy import BestBuySearch
from modules.newEgg import NewEggSearch


def run_newegg():
    rtx_3000 = [
        {
            "name": "RTX 3090",
            "url": "https://www.newegg.com/p/pl?N=100007709%20601357248",
            "target_price": 1800.00
        },
        {
            "name": "RTX 3080",
            "url": "https://www.newegg.com/p/pl?N=100007709%20601357247",
            "target_price": 900.00
        },
        {
            "name": "RTX 3070",
            "url": "https://www.newegg.com/p/pl?N=100007709%20601357250",
            "target_price": 700.00
        },
        {
            "name": "RTX 3060 Ti",
            "url": "https://www.newegg.com/p/pl?N=100007709%20601359415",
            "target_price": 500.00
        }
    ]

    # ===================================
    radeon_rx = [
        {
            "name": "Radeon RX 6900 XT",
            "url": 'https://www.newegg.com/p/pl?N=100007709%20601359957',
            "target_price": 1200.00
        },
        {
            "name": "Radeon RX 6800 XT",
            "url": 'https://www.newegg.com/p/pl?N=100007709%20601359422',
            "target_price": 700.00
        },
        {
            "name": "Radeon RX 6800",
            "url": 'https://www.newegg.com/p/pl?N=100007709%20601359427',
            "target_price": 600.00
        },
        {
            "name": "Radeon RX 5700 XT",
            "url": 'https://www.newegg.com/p/pl?N=100007709%20601341484',
            "target_price": 500.00
        }
    ]

    # ===================================
    gtx_1600 = [
        {
            "name": "GTX 1660 Supper",
            "url": 'https://www.newegg.com/p/pl?N=100007709%20601329884',
            "target_price": 350.00
        }
    ]

    items = []
    items.extend(rtx_3000)
    items.extend(radeon_rx)
    items.extend(gtx_1600)

    for item in items:
        print("------------------------------------------------------------")
        print(f'Searching for {item["name"]}')
        new_egg_search = NewEggSearch(
            search_url=item['url'],
            target_price=item['target_price'],
            number_of_tries=1
        )
        new_egg_search.search()
        new_egg_search.close()


def run_best_buy():
    rtx_3000 = [
        {
            "name": "RTX 3090",
            "url": "https://www.bestbuy.com/site/computer-cards-components/video-graphics-cards/abcat0507002.c?id=abcat0507002&qp=gpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203090",
            "target_price": 1800.00
        },
        {
            "name": "RTX 3080",
            "url": 'https://www.bestbuy.com/site/computer-cards-components/video-graphics-cards/abcat0507002.c?id=abcat0507002&qp=gpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203080',
            "target_price": 900.00
        },
        {
            "name": "RTX 3070",
            "url": 'https://www.bestbuy.com/site/computer-cards-components/video-graphics-cards/abcat0507002.c?id=abcat0507002&qp=gpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203070',
            "target_price": 700.00
        },
        {
            "name": "RTX 3060 Ti",
            "url": 'https://www.bestbuy.com/site/computer-cards-components/video-graphics-cards/abcat0507002.c?id=abcat0507002&qp=gpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203060%20Ti',
            "target_price": 500.00
        }
    ]

    # ===================================
    radeon_rx = [
        {
            "name": "Radeon RX 6900 XT",
            "url": 'https://www.bestbuy.com/site/computer-cards-components/video-graphics-cards/abcat0507002.c?id=abcat0507002&qp=gpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~AMD%20Radeon%20RX%206900%20XT',
            "target_price": 1200.00
        },
        {
            "name": "Radeon RX 6800 XT",
            "url": 'https://www.bestbuy.com/site/computer-cards-components/video-graphics-cards/abcat0507002.c?id=abcat0507002&qp=gpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~AMD%20Radeon%20RX%206800%20XT',
            "target_price": 700.00
        },
        {
            "name": "Radeon RX 6800",
            "url": 'https://www.bestbuy.com/site/computer-cards-components/video-graphics-cards/abcat0507002.c?id=abcat0507002&qp=gpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~AMD%20Radeon%20RX%206800',
            "target_price": 600.00
        },
        {
            "name": "Radeon RX 5700 XT",
            "url": 'https://www.bestbuy.com/site/computer-cards-components/video-graphics-cards/abcat0507002.c?id=abcat0507002&qp=gpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~AMD%20Radeon%20RX%205700%20XT',
            "target_price": 500.00
        }
    ]

    # ===================================
    gtx_1600 = [
        {
            "name": "GTX 1660 Supper",
            "url": 'https://www.bestbuy.com/site/computer-cards-components/video-graphics-cards/abcat0507002.c?id=abcat0507002&qp=gpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20GTX%201660%20SUPER',
            "target_price": 350.00
        }
    ]

    items = []
    items.extend(rtx_3000)
    items.extend(radeon_rx)
    items.extend(gtx_1600)

    for item in items:
        print("------------------------------------------------------------")
        print(f'Searching for {item["name"]}')
        searcher = BestBuySearch(
            search_url=item['url'],
            target_price=item['target_price'],
            number_of_tries=1
        )
        searcher.search()
        searcher.close()


def run_console():
    ps5_list = [
        {
            "name": "PS5 at Newegg",
            "url": "https://www.newegg.com/PS5-Systems/SubCategory/ID-3762",
            "target_price": 700.00
        },
        {
            "name": "PS5 at Best Buy",
            "url": 'https://www.bestbuy.com/site/playstation-5/ps5-consoles/pcmcat1587395025973.c?id=pcmcat1587395025973',
            "target_price": 700.00
        }
    ]

    # ===================================
    xbox_list = [
        {
            "name": "Xbox Series X/S at Newegg",
            "url": 'https://www.newegg.com/Xbox-Series-X-S-System/SubCategory/ID-3759',
            "target_price": 600.00
        },
        {
            "name": "Xbox Series X/s at Best Buy",
            "url": 'https://www.bestbuy.com/site/xbox-series-x-and-s/xbox-series-x-and-s-consoles/pcmcat1586900952752.c?id=pcmcat1586900952752',
            "target_price": 400.00
        }
    ]

    items = []
    items.extend(ps5_list)
    items.extend(xbox_list)

    for item in items:
        print("------------------------------------------------------------")
        print(f'Searching for {item["name"]}')
        if "bestbuy.com" in item['url']:
            searcher = BestBuySearch(
                search_url=item['url'],
                target_price=item['target_price'],
                number_of_tries=1
            )
            searcher.search()
            searcher.close()

        elif "newegg.com" in item['url']:
            new_egg_search = NewEggSearch(
                search_url=item['url'],
                target_price=item['target_price'],
                number_of_tries=1
            )
            new_egg_search.search()
            new_egg_search.close()


if __name__ == "__main__":
    run_best_buy()
    run_newegg()
    run_console()

