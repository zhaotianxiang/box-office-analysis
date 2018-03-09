#create by zhaotianxiang
#codeing utf-8
# 关于程序的说明
# 这是一个画图分析档期对票房影响的程序
# 输入：日期的范围
# 输出: 日期内单日票房的变化图示

import pymysql 
import sys
import datetime
import numpy as np  
import matplotlib.pyplot as plt 
#日期作为坐标轴引入函数
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY,YEARLY 

#连接Mysql数据库连接
#这是自定义模块
from ConnectToMySQL import connectMySQL

def dateRange(beginDate, endDate):
    dates = []
    dt = datetime.datetime.strptime(beginDate, "%Y-%m-%d")
    date = beginDate[:]
    while date <= endDate:
        dates.append(date)
        dt = dt + datetime.timedelta(1)
        date = dt.strftime("%Y-%m-%d")
    return dates
#根据日期范围画图
def drawByDates(beginDate,endDate):
	#从此开始获取数据
	db = connectMySQL()
	dates = dateRange(beginDate,endDate)
	boxOffices = []
	for date in dates:
		boxOffice = int(getInforByDate(date,db))
		#print(date+" "+str(boxOffice))
		boxOffices.append(boxOffice)
	db.close()
	#从此开始做图
	print(dates)
	print(boxOffices)
	plt.xlabel("Date(day)") #X轴标签
	plt.ylabel("BoxOffices(WanYuan)") #Y轴标签 
	plt.title(beginDate+" to "+endDate+" dialy Box-Office") #标题     
	plt.plot(dates,boxOffices,color="red",linewidth=2)
	plt.ylim(0,200000)  
	plt.grid(True)
	plt.show()

#根据日期获取当天票房的均值
def getInforByDate(date,db):
	
	cursor = db.cursor()
	sql = "SELECT boxOffice FROM DailyBoxOffices WHERE itemDate ='%s' " %(date)
	try:
		cursor.execute(sql)
	except:
		print("Error to execute "+sql)
	rows = cursor.fetchall()
	dailyBoxOfficeSum = 0.0
	for row in rows:
		dailyBoxOfficeSum = dailyBoxOfficeSum + float(row[0])
	cursor.close()
	return (dailyBoxOfficeSum)

if __name__ == '__main__':
	beginDate = input("请输入开始日期：")
	endDate = input("请输入结束日期：")
	drawByDates(beginDate,endDate)


