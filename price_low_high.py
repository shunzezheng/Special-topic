from __init__ import *

price_low_high_api = 'https://online.carrefour.com.tw/on/demandware.store/Sites-Carrefour-Site/default/Search' \
                     '-UpdateGrid?q={}&srule=price-low-high'


def low_to_high(keywords):
    user_agent = UserAgent()
    url = price_low_high_api.format(urllib.parse.quote(keywords.encode('utf8')))
    response = requests.get(url, headers={'user-agent': user_agent.random})
    soup = BeautifulSoup(response.text, "lxml")  # Parser選用lxml，較為快速

    extract = soup.find_all('a', class_='gtm-product-alink', limit=3)
    ele1 = [s.get('data-name') for s in extract]
    ele2 = [s.get('data-baseprice') for s in extract]

    print('價格由低到高排序後結果:')
    for (s, items) in zip(ele1, ele2):
        print(s, items, '元')


if __name__=="__main__":
    word = input('')
    low_to_high(keywords=word)
