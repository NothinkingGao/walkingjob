#coding:utf-8

graph={
	'A':{'weight':5,'edge':['B','C','D']},
	'B':{'weight':2,'edge':['C','D']},
	'C':{'weight':3,'edge':['D']},
	'D':{'weight':1,'edge':['E']},
	'E':{'weight':5,'edge':[]}
}


#获取所有路由
def getRouters(graph,node,results=None,line=None):
	if results is None:
		results=[]

	line=node if line is None else "{0}.{1}".format(line,node)
	results.append(line)

	for item in graph[node]['edge']:
		getRouters(graph,item,results,line)
	return results

#计算每条路径的权重
def caculate(router):
	result=0
	for item in router.split('.'):
		result+=graph[item]['weight']
	return result
	
#获取最大权重的路径
def getMaxRouter(graph,startNode):
	routers=getRouters(graph,startNode)
	max_router,max_weight=None,0
	for router in routers:
		weight=caculate(router)
		if weight>max_weight:
			max_router,max_weight=router,weight
	return max_router,max_weight

print getMaxRouter(graph,'A')
