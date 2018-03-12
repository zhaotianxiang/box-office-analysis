'''
modify by zhaotianxiang
2017-10-21
coding:utf-8
'''

import requests
from bs4 import BeautifulSoup
import re

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0"}

'''
函数:infor()
功能：根据电影详细页面的网址（从一个已有的urls.txt文件中读入每一个详细页面的网址），收集电影的详细信息，并且以列表形式返回详细信息
参数：url 电影详细页面的网址
返回值：text 详细数据的列表
'''
def getDetials(url):
    html=requests.get(url,headers=headers,timeout=30).text
    soup=BeautifulSoup(html,'lxml')
    baseinfor=soup.find('div',attrs={'class':'ziliaofr'})
    #print(baseinfor)
    contentString = str(baseinfor).replace('\r','').replace('\n','').replace(' ','')
    try:
        moviesName = re.findall('<h2>(.*?)<span>',str(contentString))[0]
        #电影名称
    except:
        moviesName = '--'

    try:
        movieTickes = re.findall('累计票房<br/>(.*?)<',str(contentString))[0]
        #电影票房
    except:
        movieTickes = '--'
    try:
        movieLiveTickes = re.findall('今日实时票房<br/>(.*?)<',str(contentString))[0]
        #电影实时票房
    except:
        movieLiveTickes = '--'
    try:
        movieStaring = re.findall('<imgalt="(.*?)"',str(contentString))[0]
        #电影主演
        #还能另外的主演信息，存在一个变量中吗？
    except:
        movieStaring = '--'
    try:
        movieTime = re.findall('片长：(.*?)<',str(contentString))[0]
        #片长
    except:
        movieTime = '--'

    try:
        movieArea = re.findall('国家及地区：(.*?)</p>',str(contentString))[0]
        #国家及地区：
    except:
        movieArea = '--' 
    try:
        movieType = re.findall('类型：(.*?)</p>',str(contentString))[0]
        #电影类型
    except:
        movieType = '--'
    try:
        movieDate = re.findall('上映时间：(.*?)</p>',str(contentString))[0]
        #电影上映日期
    except:
        movieDate = '--'
    try:
        movieTechnology = re.findall('制式：(.*?)</p>',str(contentString))[0]
        #电影制作技术
    except:
        movieTechnology = '--'
    try:
        movieIssueingCompany = re.findall('target="_blank"title="(.*?)">',str(contentString))[0]
        #电影发行公司
        #发行公司不只一家，是否都要抓取？到底抓取几个？
    except:
        movieIssueingCompany = '--'

    text= moviesName+','+movieArea+','+movieTime+','+movieLiveTickes+','+movieTickes+','+movieStaring+','+movieType+','+movieTechnology+','+movieDate+','+movieIssueingCompany
    
    dd=soup.find('div',id='content').find('div',id='tabcont1').find('dl',attrs={'class':'dltext'}).find_all('dd')

    #获取导演名
    for item in dd[0:1]:
        infor_director = ''
        for d in item.find_all('p'):
            infor_director+=d.find('a').get_text().replace('\r','').replace('\n','').replace(' ','').replace('，','').replace(',','')+'，'
        text = text+','+infor_director

    #获取演员列表
    for item in dd[1:2]:
        infor_staring = ''
        for d in item.find_all('p'):
            infor_staring+=d.find('a').get_text().replace('\r','').replace('\n','').replace(' ','').replace('，','').replace(',','')+'/'
        text = text+','+infor_staring
    #获取制作公司名 以 / 分隔
    for item in dd[2:3]:
        infor_production_company = ''
        for d in item.find_all('p'):
            infor_production_company+=d.find('a').get_text().replace('\r','').replace('\n','').replace(' ','').replace('，','').replace(',','')+'/'
        text = text+','+infor_production_company
    #获取发行公司名 以 / 分隔
    for item in dd[3:4]:
        infor_issue_conmpany = ''
        for d in item.find_all('p'):
            infor_issue_conmpany+=d.find('a').get_text().replace('\r','').replace('\n','').replace(' ','').replace('，','').replace(',','')+'/'
        text = text+','+infor_issue_conmpany
    return (text)
#测试使用，吐槽python无严格数据类型
def getDetials_test(url):
    print(url)
    return True
'''
函数名：storeInfor()
功能：将收集到每一个电影页面的详细信息保存到 movie_details.txt 文件中
'''
def storeInfor():
    file_to_write = open('../data/movie_details.txt','a',encoding='utf-8')
    statue=True
    for line in open('../data/urls.txt','r').readlines():
        url=str(line).replace('\n','')
        try:
            data = getDetials(url)
            if file_to_write.write(data+'\n'):
                print('网址为：'+url+' 页的数据已抓取')
            else:
                print('网址为：'+url+' 页的数据抓取失败')
                continue
        except:
            print('网址为：'+url+' 页的数据抓取失败')
            continue
        if line == '':
            break
    file_to_write.close()
def main():
    storeInfor()
if __name__=='__main__':
    main()