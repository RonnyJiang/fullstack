#！/usr/bin/env python
# -*- coding:utf-8 -*-
'''json.loads用于将 字典，列表，元组形式的字符串，转换成相应的字典，列表，元组。
   发送request消息，返回的看着像字典，实际类型是字符串，我们为了方便操作，并获取相应的值，
   需要将字符串转换成字典或列表数据结构来操作'''

# https://my.oschina.net/yangyanxing/blog/280029
# http://docs.python-requests.org/en/master/
import json
s = '{"desc":"value1","status":"value2"}'   #里面一定要双引号
# s = "{'desc':'value1','status':'value2'}"   #这样就不行，会报错。loads是会报错，里面必须全是双引号，只能个字符串用单引号或三引号包着
l = "[11,22,33,44]"
# s1 = {"desc":"value1","status":"value2"}
#
# for i in s1.keys():
# 	print(i)
result1 = json.loads(s)
print(result1,type(result1))
for result1Key in result1.keys():
	print('key is %s' % result1Key,'value is %s' % result1[result1Key])




result2 = json.loads(l)
print(result2,type(result2))

for item in result2:
	print("element in list is %s" % item)