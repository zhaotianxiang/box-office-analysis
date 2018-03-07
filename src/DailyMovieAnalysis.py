#create by zhaotianxiang
#codeing utf-8
#此文件用于从数据库中获取各个档期内票房的平均值
#并使用画图工具画出示意图
import pymysql 
import sys
import datetime
import matplotlib.pyplot as plt
#plt显示中文字体添加以下
from pylab import *  
mpl.rcParams['font.sans-serif'] = ['SimHei'] 
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
    dayCount = 0
    totalBoxOfficeSum = 0
    for date in dates:
        dayCount = dayCount + 1
        sql = "SELECT boxOffice FROM DailyBoxOffices WHERE itemDate ='%s' " %(date)
        try:
            cursor.execute(sql)
        except:
            print("Error to execute "+sql)

        rows = cursor.fetchall()
        dailyBoxOfficeSum = 0
        for row in rows:
            dailyBoxOfficeSum = dailyBoxOfficeSum + int(float(row[0]))
            #print(date+" "+str(dailyBoxOfficeSum))
        totalBoxOfficeSum = totalBoxOfficeSum + dailyBoxOfficeSum
        print(date+" "+str(dailyBoxOfficeSum)+" "+str(totalBoxOfficeSum))
    cursor.close()
    db.close()
    dailyBoxOfficeAVG = totalBoxOfficeSum/dayCount
    return int(dailyBoxOfficeAVG)

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
    #以下总共11个档期
    data = []
    #圣档平安夜档 准确
    NewYearDay = \
    dateRange("2011-01-01","2011-01-03")+\
    dateRange("2011-12-31","2012-01-03")+\
    dateRange("2012-12-31","2013-01-03")+\
    dateRange("2013-12-31","2014-01-03")+\
    dateRange("2014-12-31","2015-01-03")+\
    dateRange("2015-12-31","2016-01-03")+\
    dateRange("2016-12-31","2017-01-03")+\
    dateRange("2017-12-31","2018-01-03")
    newYearDayAvg = getInfoFromMySQL(NewYearDay)
    data.append(newYearDayAvg)
    #春节档 准确
    SpringFestival = \
    dateRange("2011-02-03","2011-02-06")+\
    dateRange("2012-01-23","2012-01-26")+\
    dateRange("2013-02-10","2013-02-13")+\
    dateRange("2014-01-31","2014-02-03")+\
    dateRange("2015-02-19","2015-02-22")+\
    dateRange("2016-02-08","2016-02-11")+\
    dateRange("2017-01-28","2017-01-31")+\
    dateRange("2018-02-16","2018-02-19")
    springFestivalAvg = getInfoFromMySQL(SpringFestival)
    data.append(springFestivalAvg)
    #元宵档 准确
    LanternFestival = \
    dateRange("2011-02-16","2011-02-19")+\
    dateRange("2012-02-05","2012-02-08")+\
    dateRange("2013-02-23","2013-02-26")+\
    dateRange("2014-02-13","2014-02-16")+\
    dateRange("2015-03-04","2015-03-07")+\
    dateRange("2016-02-21","2016-02-24")+\
    dateRange("2017-02-10","2017-02-13")+\
    dateRange("2018-03-01","2018-03-04")
    lanternFestivalAvg = getInfoFromMySQL(LanternFestival)
    data.append(lanternFestivalAvg)
    #清明档 准确
    ChingMingFestival = \
    dateRange("2011-04-04","2011-04-07")+\
    dateRange("2012-04-03","2012-04-06")+\
    dateRange("2013-04-03","2013-04-06")+\
    dateRange("2014-04-04","2014-04-07")+\
    dateRange("2015-04-04","2015-04-07")+\
    dateRange("2016-04-03","2016-04-06")+\
    dateRange("2017-04-03","2017-04-06")
    chingMingFestivalAvg = getInfoFromMySQL(ChingMingFestival)
    data.append(chingMingFestivalAvg)


    #五一档 准确
    Goichi = \
    dateRange("2011-04-30","2011-05-03")+\
    dateRange("2012-04-30","2012-05-03")+\
    dateRange("2013-04-30","2013-05-03")+\
    dateRange("2014-04-30","2014-05-03")+\
    dateRange("2015-04-30","2015-05-03")+\
    dateRange("2016-04-30","2016-05-03")+\
    dateRange("2017-04-30","2017-05-03")
    goichiAvg = getInfoFromMySQL(Goichi)
    data.append(goichiAvg)
    #端午档 准确
    DragonBoatFestival = \
    dateRange("2011-06-05","2011-06-07")+\
    dateRange("2012-06-22","2012-06-24")+\
    dateRange("2013-06-11","2013-06-13")+\
    dateRange("2014-06-01","2014-06-03")+\
    dateRange("2015-06-19","2015-06-21")+\
    dateRange("2016-06-08","2016-06-10")+\
    dateRange("2017-05-29","2017-05-31")
    dragonBoatFestivalAvg = getInfoFromMySQL(DragonBoatFestival)
    data.append(dragonBoatFestivalAvg)
    #中秋档
    MidAutumnFestival  = \
    dateRange("2011-09-11","2011-09-13")+\
    dateRange("2012-09-29","2012-10-01")+\
    dateRange("2013-09-18","2013-09-20")+\
    dateRange("2014-09-07","2014-09-09")+\
    dateRange("2015-09-26","2015-09-28")+\
    dateRange("2016-09-14","2016-09-16")+\
    dateRange("2017-10-03","2017-10-05")
    midAutumnFestivalAvg  = getInfoFromMySQL(MidAutumnFestival)
    data.append(midAutumnFestivalAvg)
    #十一档 准确
    ArmyDay = \
    dateRange("2011-10-01","2011-10-07")+\
    dateRange("2012-10-01","2012-10-07")+\
    dateRange("2013-10-01","2013-10-07")+\
    dateRange("2014-10-01","2014-10-07")+\
    dateRange("2015-10-01","2015-10-07")+\
    dateRange("2016-10-01","2016-10-07")+\
    dateRange("2017-10-01","2017-10-07")
    armyDayAvg = getInfoFromMySQL(ArmyDay)
    data.append(armyDayAvg)
    #情人档
    ValentineDay = \
    dateRange("2011-02-13","2011-02-14")+\
    dateRange("2012-02-13","2012-02-14")+\
    dateRange("2013-02-13","2013-02-14")+\
    dateRange("2014-02-13","2014-02-14")+\
    dateRange("2015-02-13","2015-02-14")+\
    dateRange("2016-02-13","2016-02-14")+\
    dateRange("2017-02-13","2017-02-14")+\
    dateRange("2018-02-13","2018-02-14")
    valentineDayAvg = getInfoFromMySQL(ValentineDay)
    data.append(valentineDayAvg)
    #暑期档 准确
    SummerVacation = \
    dateRange("2011-07-12","2011-08-31")+\
    dateRange("2012-07-12","2012-08-31")+\
    dateRange("2013-07-12","2013-08-31")+\
    dateRange("2014-07-12","2014-08-31")+\
    dateRange("2015-07-12","2015-08-31")+\
    dateRange("2016-07-12","2016-08-31")+\
    dateRange("2017-07-12","2017-08-31")
    summerVacationAvg = getInfoFromMySQL(SummerVacation)
    data.append(summerVacationAvg)
    #寒假档 准确
    WinterVacation = \
    dateRange("2011-01-15","2011-02-20")+\
    dateRange("2012-01-15","2012-02-20")+\
    dateRange("2013-01-15","2013-02-20")+\
    dateRange("2014-01-15","2014-02-20")+\
    dateRange("2015-01-15","2015-02-20")+\
    dateRange("2016-01-15","2016-02-20")+\
    dateRange("2017-01-15","2017-02-20")
    winterVacationAvg = getInfoFromMySQL(WinterVacation)
    data.append(winterVacationAvg)

    print(data)

    return (data)

def drawHistogram():
    dataFileName = '../data/daliyBoxOfficeResult.txt'
    file_to_reader = open(dataFileName,'r',encoding='utf8')
    name_list = []
    numb_list = []
    for line in file_to_reader.readlines():
        item = line.split(' ')
        name = item[0]
        value = int(item[1])

        name_list.append(name)
        numb_list.append(value)
        print(value)
    file_to_reader.close()
    plt.bar(range(len(numb_list)), numb_list,color='rgb',tick_label=name_list)  
    plt.show()  

def saveResultToTxt(datas):
    dataFileName = '../data/daliyBoxOfficeResult.txt'
    data = ("元旦 "+str(datas[0])+"\n春节 "+str(datas[1])+"\n元宵 "+str(datas[2])+"\n清明 "+str(datas[3])
        +"\n五一 "+str(datas[4])+"\n端午 "+str(datas[5])+"\n中秋 "+str(datas[6])+"\n十一 "+str(datas[7])
        +"\n情人节 "+str(datas[8])+"\n暑假 "+str(datas[9])+"\n寒假 "+str(datas[10])+"\n7年平均值 "+str(datas[11]))

    file_to_write = open(dataFileName,'w+',encoding='utf-8')
    if file_to_write.write(data+'\n'):
        print('success save information:')
    else:
        print('fail to save information:')
    file_to_write.close()

def quantDate():
    # 0-100
    dataFileName = '../data/daliyBoxOfficeResult.txt'
    file_to_reader = open(dataFileName,'r',encoding='utf8')
    result = []
    dataSum = 0
    dataCount = 0
    data_max = 0
    for line in file_to_reader.readlines():
        item = line.split(' ')
        value = int(item[1])
        
        if( value >= data_max ):
            data_max = value
        continue
    #print(data_max)
    file_to_reader.close()
    file_to_reader = open(dataFileName,'r',encoding='utf8')
    for line in file_to_reader.readlines():
        item = line.split(' ')
        value = int(item[1])
        #print(value)
        quanti_value = 100 * value / data_max
        print(quanti_value)
        result.append(str(quanti_value))
    file_to_reader.close()
    return (result)



if __name__ == '__main__':
    #avgDailyBoxOffice = getInfoFromMySQL(dateRange('2011-01-01','2018-03-06'))
    #print(avgDailyBoxOffice)
    #上面的函数计算7年来每日平均票房为9553万元
    # datas = classifyDate()
    # avgDailyBoxOffice = 9553
    # datas.append(avgDailyBoxOffice)
    # saveResultToTxt(datas)
    # drawHistogram()
    quantDate()






