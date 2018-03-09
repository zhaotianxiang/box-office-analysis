#coding=utf-8
#create by zhaotianxiang
import sys,locale
import re
import datetime
import requests
from bs4 import BeautifulSoup
import os

#import storeDaillyInformationToMySql
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0"}

#这是个日期生成函数，参数是日期的范围，返回日期参数
def dateRange(beginDate, endDate):
    dates = []
    dt = datetime.datetime.strptime(beginDate, "%Y-%m-%d")
    date = beginDate[:]
    while date <= endDate:
        dates.append(date)
        dt = dt + datetime.timedelta(1)
        date = dt.strftime("%Y-%m-%d")
    return dates

def getData(date):
	
	post_url="http://www.piaofang168.com/index.php/Jinzhun" 
	# url parameter
	data={"riqi":date}
	html=requests.post(post_url,data=data,headers=headers)
	html_soup=BeautifulSoup(html.text,"html.parser")
	table=html_soup.find('div',attrs={'class':'gross_total'}).find('table',attrs={'class':'gross_table'})
	tr = table.find_all('tr')
	# print(tr)
	# get the date
	date_data = table.find_all('h1')[0]
	date_str = str(date_data).replace('\r','').replace('\n','').replace(' ','')
	date=re.findall('<h1>(.*?)周',date_str)[0]

	dataFileName = '../data/movie_erverday_information.txt'
	file_to_write = open(dataFileName,'a',encoding='utf-8')

	index = 0
	for item_tr in tr[1:200]:
		item_td = item_tr.find_all('td')
		contentString = str(item_td).replace('\r','').replace('\n','').replace(' ','').replace('	','').replace(',','').replace('，','')
		#print(contentString)
		index = index + 1
		if(index%2 == 1):
			try:
				movie_name = re.findall('-bg">(.*?)<',str(contentString))[0]
			except:
				movie_name = '--'
	        #电影当日票房
			try:
				movie_daily_BoxOffice = re.findall('lor2">(.*?)<',str(contentString))[0]
			except:
				movie_daily_BoxOffice = '--'
	        #电影总票房
			try:
				movie_total_BoxOffice = re.findall('lor3">(.*?)<',str(contentString))[0]
			except:
				movie_total_BoxOffice = '--'
	        #排片占比
			try:
				percentage_screenings = re.findall('lor4">(.*?)<',str(contentString))[0]
			except:
				percentage_screenings = '--'
	        #上座率
			try:
				attendance = re.findall('lor5">(.*?)<',str(contentString))[0]
			except:
				attendance = '--'
	        #上映天数
			try:
				release_time = re.findall('lor6">(.*?)<',str(contentString))[0]
			except:
				release_time = '--'
		elif(index%2 == 0):
			try:
				movie_name = re.findall('ybg2">(.*?)<',str(contentString))[0]
			except:
				movie_name = '--'
	        #电影当日票房
			try:
				movie_daily_BoxOffice = re.findall('c2">(.*?)<',str(contentString))[0]
			except:
				movie_daily_BoxOffice = '--'
	        #电影总票房
			try:
				movie_total_BoxOffice = re.findall('c3">(.*?)<',str(contentString))[0]
			except:
				movie_total_BoxOffice = '--'
	        #排片占比
			try:
				percentage_screenings = re.findall('c4">(.*?)<',str(contentString))[0]
			except:
				percentage_screenings = '--'
	        #上座率
			try:
				attendance = re.findall('c5">(.*?)<',str(contentString))[0]
			except:
				attendance = '--'
	        #上映天数
			try:
				release_time = re.findall('c6">(.*?)<',str(contentString))[0]
			except:
				release_time = '--'
			#电影名称获取失败，直接跳过
		# to change the data as same formate
		if(movie_name == '--' or movie_daily_BoxOffice == '--' or movie_daily_BoxOffice == ''or movie_daily_BoxOffice == '--'):
			continue
		if(attendance == ''):
			attendance = '--'
		if(release_time == '' or release_time == '-'):
			release_time = '--'

		text =date+','+movie_name +','+movie_daily_BoxOffice+','+ movie_total_BoxOffice+','+percentage_screenings+','+attendance+','+release_time
		print (text)
		
		try:
			if file_to_write.write(text+'\n'):
				print('success get information:'+date)
			else:
				print('fail to get information:'+date)
				continue
		except:
			print('fail to get information:'+date)
			continue
	file_to_write.close()

if __name__ == '__main__':
	beginDate = str(input("请输入要查询数据的开始时间（年-月-日）:"))
	endDate = str(input("请输入要查询数据的结束时间（年-月-日）:"))
	dates = dateRange(beginDate, endDate)
	for date in dates:
		getData (date)
	print("\n\n"+beginDate+"至"+endDate+"的数据已全部抓取完毕！\n\n")