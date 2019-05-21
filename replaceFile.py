# -*- coding:utf-8 -*-
#批量替换文件名
import sys
import os

def replaceFileName(rootDir, oldStr, newStr):
	for dir in os.listdir(rootDir):
		filepath = rootDir + '/' + dir
		if os.path.isdir(filepath):
			print('####递归子目录:'+filepath)
			replaceFileName(filepath, oldStr, newStr)
		else:
			isIn = oldStr in dir
			if isIn:
				dir = dir.replace(oldStr,newStr)
				os.rename(filepath, rootDir + '/' + dir)
				print(filepath + '---->替换成功:'+dir)

if len(sys.argv) < 4:
	print("Usage:"+sys.argv[0] + " 文件夹路径 旧字符 新字符")
	exit(1)

rootDir = sys.argv[1]
oldStr = sys.argv[2]
newStr = sys.argv[3]

replaceFileName(rootDir,oldStr,newStr)

print("替换结束")
