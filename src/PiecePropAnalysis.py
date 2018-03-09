import pymysql 
import sys
import datetime
import matplotlib.pyplot as plt
import pandas as pd  
from pandas import DataFrame  
#plt显示中文字体添加以下
from pylab import *  
mpl.rcParams['font.sans-serif'] = ['SimHei'] 
#这是个日期生成函数，参数是日期的范围，返回日期参数
def connectMySQL():
    db = pymysql.connect("47.100.51.19","root","aini1314@xiaoqing","movie",charset='utf8')
	#后面的编码格式极其重要，耽误了两个小时，下次一定操作数据的时候一定要注意设置编码的一致
    cursor = db.cursor()
    sql = "SELECT VERSION()"
    try:
        cursor.execute(sql)
        print("Success to connect MYSQL")
    except:
    	print("Error to connect MYSQL")
    data = cursor.fetchone()
    print("MYSQL VERSION is "+data[0])
    cursor.close()
    return db
def dateRange(beginDate, endDate):
    dates = []
    dt = datetime.datetime.strptime(beginDate, "%Y-%m-%d")
    date = beginDate[:]
    while date <= endDate:
        dates.append(date)
        dt = dt + datetime.timedelta(1)
        date = dt.strftime("%Y-%m-%d")
    return dates
def getInfoFromMySQL():
    db = connectMySQL()
    cursor = db.cursor()
    sql = "SELECT itemDate,boxOffice,proportion FROM DailyBoxOffices WHERE proportion !='--' "
    try:
        cursor.execute(sql)
    except:
        print("Error to execute "+sql)

    rows = cursor.fetchall()
    data = list(rows)
    data = [list(i) for i in data]

    df = DataFrame(data,columns=["日期","单日票房","排片占比"])
    df[2] = df.apply(lambda x: x.replace("%",""))

    df.to_csv('../data/boxOfficeProptation.csv')
    print(df)

    cursor.close()
    db.close()

if __name__ == '__main__':
	getInfoFromMySQL()

