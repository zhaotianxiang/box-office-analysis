#coding:utf-8
#create by zhaotianxiang
#2018-03-13
##################################################
## 此程序用于抓取演员数据       movieActor
##################################################
def getActorName():
	file_reader = open('../data/movie_details.txt','r',encoding='utf-8')
	actorNames = set()
	for line in file_reader.readlines():
		item = line.split(',')
		names = item[11].split('/')
		print(names)


if __name__ == '__main__':
	getActorName()