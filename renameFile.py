# -*- coding:utf-8 -*-
#批量增加文件名前缀
import sys
import os

if len(sys.argv) < 2:
	print("Usage:"+sys.argv[0] + " 文件夹路径 前缀")
	exit(1)

path = sys.argv[1]
pre = sys.argv[2]
for file_name in os.listdir(path):
	print(file_name)
	new_name = pre + '_' + file_name
	os.rename(path + '/' + file_name, path + '/' + new_name)

print("修改结束")
