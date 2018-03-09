import re
import datetime
import requests
from bs4 import BeautifulSoup
import pymysql
#这是自定义模块
from ConnectToMySQL import connectMySQL

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0"}

def storeToDatabase(db,line):
	item = line.split(',')
	item[6] = item[6].replace('\n','')
	item[0] = item[0].replace('\ufeff','')
	#print(line)
	data = (item[0],item[1],item[2],item[4],item[5],item[6])
	print(data)
	sql = "INSERT INTO DailyBoxOffices (itemDate,movieName,boxOffice,proportion,attendence,releaseDays) VALUES ('%s','%s','%s','%s','%s','%s')" % tuple(data)
	try:
		cursor = db.cursor()
		cursor.execute(sql)
		db.commit()
		print("commit sucess!")
	except:
		db.rollback()
		print("commit error!")
	cursor.close()

def updateData():
	post_url="http://www.piaofang168.com/index.php/Jinzhun" 
	html=requests.post(post_url,headers=headers)
	html_soup=BeautifulSoup(html.text,"html.parser")
	table=html_soup.find('div',attrs={'class':'gross_total'}).find('table',attrs={'class':'gross_table'})
	tr = table.find_all('tr')
	#print(tr)
	date_data = table.find_all('h1')[0]
	date_str = str(date_data).replace('\r','').replace('\n','').replace(' ','').replace('	','').replace(',','').replace('，','')
	#print(date_str)
	date=re.findall('<h1>(.*?)周',date_str)[0]
	print(date)
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
		# to change the data as same formate
		text =date+','+movie_name +','+movie_daily_BoxOffice+','+ movie_total_BoxOffice+','+percentage_screenings+','+attendance+','+release_time
		db = connectMySQL()
		storeToDatabase(db,text)
		db.close()
if __name__ == '__main__':
	updateData()