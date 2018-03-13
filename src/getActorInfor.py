import re
#coding:utf-8
#create by zhaotianxiang
#2018-03-13
##################################################
## 此程序用于抓取演员数据       movieActor
##################################################
def getActorName():
	actors = set()
	file_reader = open('../data/movie_china_details.txt','r',encoding='utf-8')
	actorNames = set()
	for line in file_reader.readlines():
		item = line.split(',')
		names = item[11].split('/')
		for name in names:
			#处理每个名字中的英文字母,字符，反正仅保留汉字
			new_name = re.sub("[A-Za-z0-9\[\`\~\!\@\#\$\^\&\*\(\)\=\|\{\}\'\-\:\;\'\,\[\]\.\<\>\/\?\~\！\@\#\\\&\*\%]", "", name)
			#处理不间断空白符 \xa0
			new_name = "".join(new_name.split())

			name_type = ""

			for s in new_name:
				if(s == '·'):
					name_type = '外国人名'
					break
				else:
					name_type = '算是中国人名吧'
			if(name_type == '外国人名'):
				continue
			actors.add(new_name)

	return (actors)



if __name__ == '__main__':
	actors = getActorName()
	print(actors)
	count = 0
	for actor in actors:
		count = count + 1
	print("演员名字数目：",count)
	#我的妈呀，抓出来1万个像是中国演员的名字，让我冷静一下
