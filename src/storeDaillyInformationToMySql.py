#coding:utf-8 
#create by zhaotianxiang
import pymysql 
import sys
print(sys.getdefaultencoding())
db = pymysql.connect("47.100.51.19","root","aini1314@xiaoqing","movie",charset='utf8')
#后面的编码格式极其重要，耽误了两个小时，下次一定操作数据的时候一定要注意设置编码的一致
cursor = db.cursor()

def createTable():
    cursor.execute("DROP TABLE IF EXISTS DailyBoxOffices")
    sql = """CREATE TABLE DailyBoxOffices(
    itemID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    itemDate DATE NOT NULL,
    movieName VARCHAR(45) NOT NULL,
    boxOffice CHAR(10),
    proportion CHAR(10),
    attendence CHAR(10),
    releaseDays CHAR(10))"""
    try:
        cursor.execute(sql)
    except:
    	print("error to create table!\n")
def storeToDatabase():

	file_read=open('../data/movie_erverday_information.txt','r',encoding='utf8')
	for line in file_read.readlines():

		try:
			item = line.split(',')
			item[6] = item[6].replace('\n','')
			item[0] = item[0].replace('\ufeff','')
			data = (item[0],item[1],item[2],item[4],item[5],item[6])
			print(data)
			sql = "INSERT INTO DailyBoxOffices (itemDate,movieName,boxOffice,proportion,attendence,releaseDays) VALUES ('%s','%s','%s','%s','%s','%s')" % tuple(data)
			#print(sql)
		except:
			print("error format")
			#break
			continue
		try:
			cursor.execute(sql)
			db.commit()
			print("success to insert data into table")
		except:
			db.rollback()
			print("error to insert data into table")
			#break
			continue
	file_read.close()

if __name__ == '__main__':
	#createTable()
	storeToDatabase()
	cursor.close()
	db.close()


