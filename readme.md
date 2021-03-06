# 最近面试时被要求做的工程问题和我的答案

## 【第一题】JSON格式转换
在某个特定应用场景中,我们有一个从JSON获取的内容,比如:
m = { "a": 1, "b": { "c": 2, "d": [3,4] } }
现在需要把这个层级的结构做展开,只保留一层key/value结构。对于上述
输入,需要得到的结构是:
o = {"a": 1, "b.c": 2, "b.d": [3,4] }
也就是说,原来需要通过 m["b"]["c"] 访问的值,在展开后可以通过 o["b.c"]
访问。
请实现这个“层级结构展开”的代码。
输入:任意JSON(或者map/dict)
输出:展开后的JSON(或者map/dict)
```
answer1.py
```
##  【第二题】数据存取
我们的程序运行过程中用到了一个数组a,数组元素是一个map/dict。
数组元素的“键”和“值”都是字符串类型。在不同的语言中,对应的类型是:
PHP的array, Java的HashMap, C++的std::map, Objective-C的
NSDictionary, Swift的Dictionary, Python的dict, JavaScript的object, 等
等
示例:
a[0]["key1"]="value1"
a[0]["key2"]="value2"
a[1]["keyA"]="valueA"
...
为了方便保存和加载,我们使用了一个基于文本的存储结构,数组元素每行
一个:
text="key1=value1;key2=value2\nkeyA=valueA\n..."
要求:请实现一个“保存”函数、一个“加载”函数。
text=store(a); //把数组保存到一个文本字符串中a=load(text); //把文本字符串中的内容读取为数组
必须严格按照上述的“每行一个、key=value”的格式保存。

```
answer2.py
```
## 【第三题】路径规划
假设现在有一个有向无环图,每个节点上都带有正数权重。我们希望找到一
条最优路径,使得这个路径上经过的节点的权重之和最大。
输入:n个节点,m个路径,起点
输出:最优路径的权重值之和
举例:
3个节点:
A 1
B 2
C 2
3条路径:
A->B
B->C
A->C
起点:
A
输出:5 (最优路径是 A->B->C , 权重之和是 1+2+2=5)
• 附加问题:我们要求的输入是有向无环图,但是没人知道实际使用的时
候会有什么数据输入进来,如何避免输入了带环路的图导致的死循环
呢? 	
```
answer3.py
```