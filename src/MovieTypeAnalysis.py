#coding:utf-8
#create by zhaotianxiang
#2018-03-02
#这是自定义模块
import time
##################################################
## 此程序用于量化电影类型        movieType
##################################################

def getTypes():
	file_reader = open('../data/movie_details.txt','r',encoding='utf-8')
	types = set()
	for line in file_reader.readlines():
		item = line.split(",")
		movieName = item[0]
		boxOffice = item[4].replace("万","")
		movieType = item[6].split("/")
		#数据的简单处理，将票房缺失值剔除
		if(boxOffice == "--" and firstType == ''):
			continue

		try:
			firstType = movieType[0]
		except:
			firstType = "--"
		try:
			secondType = movieType[1]
		except:
			secondType = "--"
		try:
			thirdType = movieType[2]
		except:
			thirdType = "--"

		if(secondType == ''):
			secondType = "--"

		if(thirdType == ''):
			thirdType = "--"
		types.add(firstType)
		types.add(secondType)
		types.add(thirdType)
	dictionary ={}
	for type in types:
		dictionary[type] = {"总票房":0,"计数":0}
	#print(dictionary)

	file_reader.close()
	return dictionary
# 
# 不同类型量化方式
def quanType():
	file_reader = open('../data/movie_details.txt','r',encoding='utf-8')
	typeDic = getTypes()
	for line in file_reader.readlines():
		item = line.split(",")
		movieName = item[0]
		boxOffice = item[4].replace("万","")
		movieType = item[6].split("/")
		#数据的简单处理，将票房缺失值剔除
		if(boxOffice == "--" and firstType == ''):
			continue

		try:
			firstType = movieType[0]
		except:
			firstType = "--"
		try:
			secondType = movieType[1]
		except:
			secondType = "--"
		try:
			thirdType = movieType[2]
		except:
			thirdType = "--"

		if(secondType == ''):
			secondType = "--"

		if(thirdType == ''):
			thirdType = "--"

		###########################################
		#
		# 量化方案：给同一部电影类型位置设置不同权重
		#
		# 情况1：缺少第三类型 权重 7:3:0
		# 情况2：缺少后两类型 权重 1:0:0
		# 情况3：具有三种类型 权重 7:2:1
		#
		###########################################
		
		if(boxOffice != '--' and firstType!='--' and secondType !='--' and thirdType == '--'):
			#情况1
			typeDic[firstType]['总票房'] += float(boxOffice)*0.7
			typeDic[firstType]['计数'] = typeDic[firstType]['计数']+1

			typeDic[secondType]['总票房'] += float(boxOffice)*0.3
			typeDic[secondType]['计数'] = typeDic[secondType]['计数']+1

		elif(boxOffice != '--' and firstType!='--' and secondType =='--' and thirdType == '--'):
			#情况2
			typeDic[firstType]['总票房'] += float(boxOffice)
			typeDic[firstType]['计数'] = typeDic[firstType]['计数']+1

		elif(boxOffice != '--' and firstType!='--' and secondType !='--' and thirdType != '--'):
			#情况3
			typeDic[firstType]['总票房'] += float(boxOffice)*0.7
			typeDic[firstType]['计数'] = typeDic[firstType]['计数']+1

			typeDic[secondType]['总票房'] += float(boxOffice)*0.2
			typeDic[secondType]['计数'] = typeDic[secondType]['计数']+1

			typeDic[thirdType]['总票房'] += float(boxOffice)*0.1
			typeDic[thirdType]['计数'] = typeDic[thirdType]['计数']+1

	#print(typeDic)

	avgDic = {}
	for movieType in typeDic.keys():
		#除零错误
		if(typeDic[movieType]['计数'] == 0):
			continue
		avgDic[movieType] = typeDic[movieType]['总票房']/typeDic[movieType]['计数']

	#排序输出

	avgDic = sorted(avgDic.items(),key = lambda x:x[1],reverse = True)

	print(avgDic)
	return avgDic	
	file_reader.close()
def saveToTxt(List):
	file_writer = open('../data/MovieTypeResult.txt','w+',encoding='utf-8')
	for item in List:
		data = str(item[0])+","+ str(item[1])
		file_writer.write(str(data)+"\n")
	file_writer.close()




if __name__ == '__main__':
	saveToTxt(quanType()) 