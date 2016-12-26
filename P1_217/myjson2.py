#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
json.loads() 将字符串转换成python的基本数据类型
json.dumps() 将python的基本数据类型转换成字符串

'''
import json
user_list = ["lily","jimmy","kiki"]

s = json.dumps(user_list)

print(s,type(s))
