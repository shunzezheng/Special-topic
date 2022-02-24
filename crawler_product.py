#                                     _                                        _               _
#                                    | |                                      | |             | |
#          ___  _ __  __ _ __      __| |  ___  _ __     _ __   _ __  ___    __| | _   _   ___ | |_
#         / __|| '__|/ _` |\ \ /\ / /| | / _ \| '__|   | '_ \ | '__|/ _ \  / _` || | | | / __|| __|
#        | (__ | |  | (_| | \ V  V / | ||  __/| |      | |_) || |  | (_) || (_| || |_| || (__ | |_
#         \___||_|   \__,_|  \_/\_/  |_| \___||_|      | .__/ |_|   \___/  \__,_| \__,_| \___| \__|
#                                                      | |
#                                                      |_|
#
#
#                                                                                       目前版本 v1.7.0
#                                                                                       撰寫成員: 鄭舜澤


from __init__ import *


# crawler the product info (name、link、price、pop)
def goods_info(user_input):
    content = ""
    listx = []

    url = 'https://online.carrefour.com.tw/zh/search?q=' + str(user_input) if not None else print("error!")
    user_agent = UserAgent()
    response = requests.get(url, headers={'user-agent': user_agent.random})
    soup = BeautifulSoup(response.text, "lxml")  # Parser選用lxml，較為快速
    # extract the html tag <a> sections
    extract = soup.find_all('a', class_='gtm-product-alink', limit=3)
    ele = [s.get('href') for s in extract]

    if len(ele) > 0:

        for (s, items) in zip(extract, [0, 1, 2]):
            search = s.get('href')
            link = shorten("https://online.carrefour.com.tw" + search, '')
            name = s.get('data-name')
            price = s.get('data-baseprice') + '元'
            category = s.get('data-category')
            listx.append(link)
            content += f"\n{category}\n{name}{price}\n{link}\n"

        print("以下是商品熱門結果:\n" + content.strip())

    else:
        print("商品不存在!")


# 縮網址
def shorten(long_url, alias):
    URL = "http://tinyurl.com/create.php?source=indexpage&url=" + long_url + "&submit=Make+TinyURL%21&alias=" + alias
    response = urlopen(URL)
    soup = BeautifulSoup(response, 'lxml')
    return soup.find_all('div', {'class': 'indent'})[1].b.string


if __name__=='__main__':
    user_input = input('')
    goods_info(user_input)
