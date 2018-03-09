import re
import datetime
import requests
from bs4 import BeautifulSoup
import pymysql
import json
#这是自定义模块
from ConnectToMySQL import connectMySQL

headers = {
    "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0"}

#警告，建立数据表只执行一次，建好后千万不再执行
def createTable():
    db = connectMySQL()
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS RealtimeDatasFromEN")

    sql = """CREATE TABLE RealtimeDatasFromEN(
    itemID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    itemDate DATE NOT NULL,
    rank CHAR(10),
    movieName VARCHAR(45) NOT NULL,
    boxOffice CHAR(10),
    sumBoxOffice CHAR(10),
    boxProportion CHAR(10),
    movieDay CHAR(10),
    mId CHAR(10))"""
    try:
        cursor.execute(sql)
        print("successed to create table!\n")
    except:
    	print("error to create table!\n")
def getInfor():
	get_url = 'http://www.cbooo.cn//BoxOffice/GetHourBoxOffice'
	html=requests.get(get_url,headers=headers).text
	jsonData = json.loads(html)
	#print(html)
	#print(jsonData["data1"])
	#print(jsonData["data2"])
	sumInformation = jsonData["data1"]
	itemDatas = jsonData["data2"]
	for i in range(0,11):
		item = itemDatas[i]
		print(item)
		#以下是获取了七项数据
		rank = item['Irank']
		mId = item['mId']
		movieName = item['MovieName']
		boxOffice = item['BoxOffice']
		sumBoxOffice = item['sumBoxOffice']
		movieDay = item['movieDay']
		#票房占比
		boxProportion =item['boxPer']
		print(movieName)




if __name__ == '__main__':
	#getInfor()
	createTable()