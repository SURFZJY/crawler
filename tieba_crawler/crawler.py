# -*- coding:utf-8 -*-
import requests
import urllib.request
import os
from bs4 import BeautifulSoup

class Crawler:

    # 初始化帖子的地址
    def __init__(self):
        self.siteURL = 'http://tieba.baidu.com/p/4317998534'

    # 获得帖子的HTML文本
    def getText(self,pageIndex):
        url = self.siteURL + '?pn=' + str(pageIndex)
        source_code = requests.get(url)
        plain_text = source_code.text
        return plain_text

    # 获取楼主的昵称
    def getName(self):
        html_text = self.getText(1)
        soup = BeautifulSoup(html_text)
        for link in soup.find_all('a',{'alog-group':'p_author'}):
            landlord_name = link.string
            return landlord_name

    # 表情图片过滤
    def emojiFilter(self):
        pass

    # 获取帖子页数
    def getPagenumber(self):
        html_text = self.getText(1)
        soup = BeautifulSoup(html_text)
        page_list = list()
        for link in soup.find_all('span',{'class':'red'}):
            pagenumber = link.string
            page_list.append(pagenumber)
        return int(page_list[1])

    # 创建文件夹
    def mkdir(self,path):
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)
            return True
        else:
            return False

    # 根据URL保存图片
    def saveImg(self,imgURL,imgName):
        imgName = imgName + '.jpg'
        data = urllib.request.urlopen(imgURL).read()
        print('the '+ imgName + ' picture is downloading')
        with open(imgName, 'wb') as f:
            f.write(data)

    # 下载图片并按顺序依次编号
    def imageDownload(self):
        pageIndex = 1
        name = 1
        max_page = self.getPagenumber()
        landlord_name = self.getName()
        self.mkdir(landlord_name)
        cur_path = os.path.abspath('.')
        while pageIndex <= max_page:
            html_text = self.getText(pageIndex)
            soup = BeautifulSoup(html_text)
            for link in soup.find_all('img',{'class':'BDE_Image'}):
                object_url = link.get('src')
                down_dir = cur_path+ '\\' + landlord_name + '\\'
                self.saveImg(object_url, ( down_dir + str(name)))
                name += 1
            pageIndex += 1
        print('Downloading finished!')

crawler = Crawler()
crawler.imageDownload()

