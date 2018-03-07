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
        dailyBoxOfficeSum = 0.0
        for row in rows:
            dailyBoxOfficeSum = dailyBoxOfficeSum + float(row[1])
            print(date+" "+str(dailyBoxOfficeSum))
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
    #元旦档
    NewYearDay = \
    dateRange("2011-01-01","2011-01-03")+\
    dateRange("2012-01-01","2012-01-03")+\
    dateRange("2013-01-01","2013-01-03")+\
    dateRange("2014-01-01","2014-01-03")+\
    dateRange("2015-01-01","2015-01-03")+\
    dateRange("2016-01-01","2016-01-03")+\
    dateRange("2016-12-31","2017-01-03")+\
    dateRange("2017-12-31","2018-01-03")
    print(NewYearDay)
    #春节档
    SpringFestival = \
    dateRange("2011-02-02","2011-02-08")+\
    dateRange("2012-01-22","2012-01-28")+\
    dateRange("2013-02-09","2013-02-15")+\
    dateRange("2014-01-31","2014-02-06")+\
    dateRange("2015-02-18","2015-02-24")+\
    dateRange("2016-02-07","2016-02-13")+\
    dateRange("2017-01-27","2017-02-02")+\
    dateRange("2018-02-16","2018-02-22")
    print(SpringFestival)
    #元宵档
    LanternFestival = \
    dateRange("2011-02-02","2011-02-08")+\
    dateRange("2012-01-22","2012-01-28")+\
    dateRange("2013-02-09","2013-02-15")+\
    dateRange("2014-01-31","2014-02-06")+\
    dateRange("2015-02-18","2015-02-24")+\
    dateRange("2016-02-07","2016-02-13")+\
    dateRange("2017-01-27","2017-02-02")+\
    dateRange("2018-02-16","2018-02-22")
    print(LanternFestival)
    #清明档
    ChingMingFestival = \
    dateRange("2011-02-02","2011-02-08")+\
    dateRange("2012-01-22","2012-01-28")+\
    dateRange("2013-02-09","2013-02-15")+\
    dateRange("2014-01-31","2014-02-06")+\
    dateRange("2015-02-18","2015-02-24")+\
    dateRange("2016-02-07","2016-02-13")+\
    dateRange("2017-01-27","2017-02-02")+\
    dateRange("2018-02-16","2018-02-22")
    print(ChingMingFestival)
    #五一档
    Goichi = \
    dateRange("2011-02-02","2011-02-08")+\
    dateRange("2012-01-22","2012-01-28")+\
    dateRange("2013-02-09","2013-02-15")+\
    dateRange("2014-01-31","2014-02-06")+\
    dateRange("2015-02-18","2015-02-24")+\
    dateRange("2016-02-07","2016-02-13")+\
    dateRange("2017-01-27","2017-02-02")+\
    dateRange("2018-02-16","2018-02-22")
    print(Goichi)
    #端午档
    DragonBoatFestival = \
    dateRange("2011-02-02","2011-02-08")+\
    dateRange("2012-01-22","2012-01-28")+\
    dateRange("2013-02-09","2013-02-15")+\
    dateRange("2014-01-31","2014-02-06")+\
    dateRange("2015-02-18","2015-02-24")+\
    dateRange("2016-02-07","2016-02-13")+\
    dateRange("2017-01-27","2017-02-02")+\
    dateRange("2018-02-16","2018-02-22")
    print(DragonBoatFestival)
    #中秋档
    MidAutumnFestival  = \
    dateRange("2011-02-02","2011-02-08")+\
    dateRange("2012-01-22","2012-01-28")+\
    dateRange("2013-02-09","2013-02-15")+\
    dateRange("2014-01-31","2014-02-06")+\
    dateRange("2015-02-18","2015-02-24")+\
    dateRange("2016-02-07","2016-02-13")+\
    dateRange("2017-01-27","2017-02-02")+\
    dateRange("2018-02-16","2018-02-22")
    print(MidAutumnFestival)
    #十一档
    ArmyDay = \
    dateRange("2011-02-02","2011-02-08")+\
    dateRange("2012-01-22","2012-01-28")+\
    dateRange("2013-02-09","2013-02-15")+\
    dateRange("2014-01-31","2014-02-06")+\
    dateRange("2015-02-18","2015-02-24")+\
    dateRange("2016-02-07","2016-02-13")+\
    dateRange("2017-01-27","2017-02-02")+\
    dateRange("2018-02-16","2018-02-22")
    print(ArmyDay)
    #平安夜档
    ChristmasEve = \
    dateRange("2011-02-02","2011-02-08")+\
    dateRange("2012-01-22","2012-01-28")+\
    dateRange("2013-02-09","2013-02-15")+\
    dateRange("2014-01-31","2014-02-06")+\
    dateRange("2015-02-18","2015-02-24")+\
    dateRange("2016-02-07","2016-02-13")+\
    dateRange("2017-01-27","2017-02-02")+\
    dateRange("2018-02-16","2018-02-22")
    print(ChristmasEve)
    #七夕档
    ChineseValentineDay = \
    dateRange("2011-02-02","2011-02-08")+\
    dateRange("2012-01-22","2012-01-28")+\
    dateRange("2013-02-09","2013-02-15")+\
    dateRange("2014-01-31","2014-02-06")+\
    dateRange("2015-02-18","2015-02-24")+\
    dateRange("2016-02-07","2016-02-13")+\
    dateRange("2017-01-27","2017-02-02")+\
    dateRange("2018-02-16","2018-02-22")
    print(ChineseValentineDay)
    #暑期档
    SummerVacation = \
    dateRange("2011-02-02","2011-02-08")+\
    dateRange("2012-01-22","2012-01-28")+\
    dateRange("2013-02-09","2013-02-15")+\
    dateRange("2014-01-31","2014-02-06")+\
    dateRange("2015-02-18","2015-02-24")+\
    dateRange("2016-02-07","2016-02-13")+\
    dateRange("2017-01-27","2017-02-02")+\
    dateRange("2018-02-16","2018-02-22")
    print(SummerVacation)
    #寒假档
    WinterVacation = \
    dateRange("2011-02-02","2011-02-08")+\
    dateRange("2012-01-22","2012-01-28")+\
    dateRange("2013-02-09","2013-02-15")+\
    dateRange("2014-01-31","2014-02-06")+\
    dateRange("2015-02-18","2015-02-24")+\
    dateRange("2016-02-07","2016-02-13")+\
    dateRange("2017-01-27","2017-02-02")+\
    dateRange("2018-02-16","2018-02-22")
    print(WinterVacation)

    return NewYearDay


if __name__ == '__main__':
    #dates = dateRange(springFestival)
    #getInfoFromMySQL(dates)
    getInfoFromMySQL(classifyDate())



