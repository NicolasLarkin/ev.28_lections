from bs4 import BeautifulSoup as bs
import requests 
import json
import lxml

def get_html(url):
    response = requests.get(url)
    return response.text

def get_soup(html):
    soup = bs(html, 'lxml')
    return soup
    # return bs(html, 'lxml') нет никакой разницы :)

def get_catalog(soup):
    catalog = soup.find('div', class_ ='Tag--articles')
    return catalog

def get_articles(catalog):
    articles = catalog.find_all('div', class_ ='Tag--article') [0:20]
    return articles

def get_detail(link):
    from functools import reduce
    html = get_html('https://kaktus.media/doc/479619_v_kyrgyzstane_proydet_massovyy_detskiy_zabeg._kak_priniat_ychastie.html')
    soup = get_soup(html)
    desc = soup.find('div', class_ = 'BbCode')
    text = desc.find_all('p')
    res = reduce(lambda a, b: a + ' ' + b, [x.text.strip() for x in text])
    return res

get_detail('123') # Пример

def get_data(articles):
    i = 1
    res = {}
    for item in articles:
        title = item.find('a', class_ = 'ArticleItem--name').text.strip()
        image = item.find('img', class_ ='ArticleItem--image-img').get('src')
        image = image.replace('small', 'big')
        link = item.find('a', class_ = 'ArticleItem--name').get('href')
        description = get_detail(link)
        data = {'title': title, 'img':image, 'desc': description}
        res[i] = data
        i += 1
    return res 

def write_to_json(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
              

def parse_news():
    base_url = 'https://kaktus.media/?lable=8&date=2023-04-25&order=time'
    html = get_html(base_url)
    soup = get_soup(html)
    catalog = get_catalog(soup)
    articles = get_articles(catalog)
    data = get_data(articles)
    write_to_json(data)

# parse_news()

