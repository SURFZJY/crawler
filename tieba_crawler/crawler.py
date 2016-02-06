import requests
from bs4 import BeautifulSoup
import urllib.request

def basic_spider(max_pages):
    page = 1
    name = 1
    while page <= max_pages:
        url = 'http://tieba.baidu.com/p/4336363424' + '?pn=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('img',{'class':'BDE_Image'}):
            object_url = link.get('src')
            # title = link.string
            # get_single_item_data(href)
            # save_image(object_url,str(name))
            # print(object_url)
            # print(name)
            save_image(object_url,str(name))
            name += 1
        page += 1

def save_image(image_url,name):
    filename = name+'.jpg'
    urllib.request.urlretrieve(image_url,filename)

max_page = 6
basic_spider(max_page)