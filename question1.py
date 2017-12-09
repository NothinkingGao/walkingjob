# coding:utf-8
# 高明 2017.12.08

source={"a":1,"b":{"c":2,"d":[3,4],"e":{"f":1,"g":2}}}


#第一道题
def getResults(source,results=None,parent_key=None):
	if not isinstance(source,dict):
		raise TypeError

	if results is None:
		results={}
	for key,value in source.items():
		new_key= key if parent_key is None else "{0}.{1}".format(parent_key,key)
		if not isinstance(value,dict):	
			results[new_key]=value
			continue
		getResults(value,results,new_key)
	return results

print getResults(source)