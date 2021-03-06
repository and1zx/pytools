#!/usr/bin/env python
#coding:utf-8

'''
本脚本功能为从文件中随机抽取指定行数的样本
算法原理：
如随机抽取n条，
1. 前n条放入list
2. 第n+k条以n/(n+k)的概率替换list中的随机某一条

论证过程略
此算法对于在海量数据中随机抽取小量数据效率较高
'''

import sys
from random import *

if __name__ == '__main__':
	try:
		select = int(sys.argv[1])
	except:
		print >>sys.stderr, "usage:\n\t%s interger" % sys.argv[0]
		exit(1)

	select_list=[]
	line_no = 0
	for line in sys.stdin:
		line = line.strip()
		line_no += 1
		if line_no <= select:
			select_list.append(line)
		else:
			if uniform(0,1) <= select*1.0/line_no:
				select_list[randint(0,select - 1)] = line

	for line in select_list:
		print line
