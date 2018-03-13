#coding:utf-8

import requests
#import xlwt3
from bs4 import BeautifulSoup
import re

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0"}


# def get_code():
#     #单独执行，储存上映地区名称和选择编号code
#     f=open('../data/code.txt','w',encoding='utf-8')
#     html=requests.get('http://www.cbooo.cn/movies').text
#     table=BeautifulSoup(html,'lxml').find('div',attrs={'class':'select01'}).find('select',id='selArea').find_all('option')
#     for item in table:
#         text=item.get_text()+','+item.get('value')
#         print(text)
#         f.write(text+'\n')
#     f.close()

def get_url(code,page):
    results=[]
    html=requests.get('http://www.cbooo.cn/Mdata/getMdata_movie?area='+str(code)+'&type=0&year=0&initial=%E5%85%A8%E9%83%A8&pIndex='+str(page),headers=headers).text
    data=eval(html)['pData']
    for item in data:
        text='http://www.cbooo.cn/m/'+item['ID']
        results.append(text)
    return results


def main():
    f=open('../data/urls.txt','a',encoding='utf-8')

    for line in open('../data/code.txt','r',errors='ignore').readlines():
        code=line.split(',')[-1]
        page=1
        pre=[]
        while True:
            try:
                results=get_url(code, page)
            except:
                break
            if pre==results:
                break
            pre=results
            page+=1
            for item in results:
                f.write(item+'\n')
            print(code,'--',page)  
    f.close()
if __name__ =='__main__':
    main()