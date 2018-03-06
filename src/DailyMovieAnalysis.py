#create by zhaotianxiang
#codeing utf-8
import pymysql 
import sys
import datetime
#print(sys.getdefaultencoding())

#连接Mysql数据库连接
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

def getInfoFromMySQL(dates):
    db = connectMySQL()
    cursor = db.cursor()
    for date in dates:
        sql = "SELECT itemDate,boxOffice FROM DailyBoxOffices WHERE itemDate ='%s' " %(date)
        try:
            cursor.execute(sql)
        except:
            print("Error to execute "+sql)

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    cursor.close()
    db.close()
    return rows

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
def classifyDate():
    springFestival = \
    dateRange("2012-02-01","2013-02-02")+\
    dateRange("2012-02-01","2013-02-02")+\
    dateRange("2012-02-01","2013-02-02")+\
    dateRange("2012-02-01","2013-02-02")+\
    dateRange("2012-02-01","2013-02-02")
    print(springFestival)


if __name__ == '__main__':
    #dates = dateRange(springFestival)
    #getInfoFromMySQL(dates)
    classifyDate()



