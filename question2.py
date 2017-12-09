#coding:utf-8

#第二道题
def store(lists):
	try:
		text=""
		for item in lists:
			text+=";".join(["{0}={1}".format(key,value) for key,value in item.items()])
			if lists.index(item)!=len(lists)-1:
				text+="\n"
		return text
	except Exception,e:
		print 'store data wrong:\n{0}'.format(str(e))

def load(text):
	if not isinstance(lists,str):
		raise TypeError

	try:
		results=[]
		for item in text.split('\n'):
			line_dict={}
			for i in [dict_item for dict_item in item.split(';') if item !=""]:
				index=i.index('=')
				line_dict[i[0:index]]=i[index+1:len(i)-1]
			results.append(line_dict)
		return results
	except Exception,e:
		print 'load data wrong:\n{0}'.format(str(e))
