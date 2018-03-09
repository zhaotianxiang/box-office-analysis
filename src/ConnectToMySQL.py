import pymysql 
#这是一个数据库连接模块，代码复用
def connectMySQL():
    db = pymysql.connect(
    host='47.100.51.19',
    user='root',
    passwd='aini1314@xiaoqing',
    db='movie',
    charset='utf8')
    cursor = db.cursor()
    sql = "SELECT VERSION()"
    try:
        cursor.execute(sql)
        print("Success to connect MYSQL")
    except:
    	print("Error to connect MYSQL")
    data = cursor.fetchone()
    #print("MYSQL VERSION is "+data[0])
    cursor.close()
    return db