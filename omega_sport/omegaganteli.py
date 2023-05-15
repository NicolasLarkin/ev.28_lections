from bs4 import BeautifulSoup
import requests
import lxml 

def get_html(url):
    response = requests.get(url)
    return response.text

def get_soup(html):
    soup = BeautifulSoup(html, 'lxml')
    return soup

def get_links(soup):
    links = []
    container = soup.find('div', class_ ='row')
    items = container.find_all('div', class_='product-layout product-grid col-xs-12 col-sm-4 col-md-3')
    for item in items:
        a = item.find('a'.get('href'))
        link = 'https://omegasport.kg/' + a 
        links.append(link)
    return links

def get_all_links():
    res = []
    url = 'https://omegasport.kg/index.php?route=product/category&path=69_71'
    html = get_html(url)
    soup = get_soup(html)
    page_links = get_links(soup)
    res.extend(page_links)
    return res

def get_deps_data(link):
    html = get_html(link)
    soup = get_soup(html)
    name = soup.find('div', class_= 'deput-name').text
    info = ' '.join(soup.find('div', class_ = 'deput-info').text.strip().split())
    bio = soup.find('div', class_ = 'tab-content').text.strip()
    img = 'http://kenesh.kg' + soup.find('div', class_ = 'deput-image').find('img').get('src').replace(' ', '%20')
    data = {'name': name, 'info': info, 'bio': bio, 'img': img, 'link': link}
    return data

    