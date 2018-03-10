import re
import datetime
import requests
from bs4 import BeautifulSoup
import pymysql
import json
#这是自定义模块
from ConnectToMySQL import connectMySQL
import time

headers = {
    "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0"}

# 警告，建立数据表只执行一次，建好后千万不再执行
# 建立各个电影每日的更新的上座率
def createTable():
    db = connectMySQL()
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS DailyAttendenceFromEN")

    sql = """CREATE TABLE DailyAttendenceFromEN(
    itemID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    itemDate DATE NOT NULL,
    movieName VARCHAR(45) NOT NULL,
    bookingRate CHAR(10),
    avgPeople CHAR(10),
    rateLine CHAR(10),
    peopleLine CHAR(10),
    mId CHAR(10))"""
    try:
        cursor.execute(sql)
        print("successed to create table!\n")
    except:
    	print("error to create table!\n")
    cursor.close()
    db.close()
###########################################################
##以上永不执行
def getInfor():
	get_url = 'http://www.cbooo.cn/BoxOffice/GetTopRate'
	html=requests.get(get_url,headers=headers).text
	jsonData = json.loads(html)
	#print(jsonData)
	for i in range(0,10):
		item = jsonData[i]
		date = time.strftime("%Y-%m-%d")
		data = (date,str(item["MovieName"]),str(item["BookingRate"]),str(item["AvgPeople"]),
			str(item["RateLine"]),str(item["PeopleLine"]),str(item["MovieID"]))
		sql = "INSERT INTO DailyAttendenceFromEN \
		(itemDate,movieName,bookingRate,avgPeople,rateLine,peopleLine,mId) \
		VALUES ('%s','%s','%s','%s','%s','%s','%s')" % tuple(data)
		# 插入数据库
		db = connectMySQL()
		cursor = db.cursor()
		print(data)
		try:
			cursor.execute(sql)
			db.commit()
			print("commit sucess!")
		except:
			db.rollback()
			print("commit error!")
			cursor.close()
		cursor.close()
		db.close()
if __name__ == '__main__':
	getInfor()