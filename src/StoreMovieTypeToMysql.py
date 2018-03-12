import re
import datetime
import requests
from bs4 import BeautifulSoup
import pymysql
import json
#这是自定义模块
from ConnectToMySQL import connectMySQL
import time
##################################################
## 此程序用于创建并且保存电影类型信息表 MovieType
##################################################

def createTable():
    db = connectMySQL()
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS MovieType")

    sql = """
    CREATE TABLE MovieType(
    itemID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    movieName VARCHAR(45) NOT NULL,
    boxOffice VARCHAR(45) NOT NULL,
    firstType CHAR(10) NOT NULL,
    secondType CHAR(10),
    thirdType CHAR(10))
    """
    try:
        cursor.execute(sql)
        print("successed to create table!\n")
    except:
    	print("error to create table!\n")
    cursor.close()
    db.close()
###########################################################
##以上永不执行
def storeInfor():
	file_reader = open('../data/movie_details.txt','r',encoding='utf-8')
	db = connectMySQL()
	for line in file_reader.readlines():
		item = line.split(",")
		movieName = item[0]
		boxOffice = item[4].replace("万","")
		movieType = item[6].split("/")
		#数据的简单处理，将票房缺失值剔除
		if(boxOffice == "--"):
			continue
		firstType = movieType[0]
		try:
			secondType = movieType[1]
		except:
			secondType = "--"
		try:
			thirdType = movieType[2]
		except:
			thirdType = "--"
		data = (str(movieName),str(boxOffice),str(firstType),str(secondType),str(thirdType))
		print(data)

		# 插入数据库中
		
		
		cursor = db.cursor()
		sql = "INSERT INTO MovieType (movieName,boxOffice,firstType,secondType,thirdType) \
		VALUES ('%s','%s','%s','%s','%s')" % tuple(data)
		try:
			cursor.execute(sql)
			print("successed to insert data",data)
		except:
			print("fail to insert data",da)

		cursor.close()
	db.close()

if __name__ == '__main__':
	createTable()
	storeInfor()