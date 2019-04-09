# -*- coding:utf-8 -*-

import os
import sys
import shutil

if len(sys.argv) < 3:
	print("Usage:python "+sys.argv[0]+" 配置文件 文件后缀  文件夹路径")
	exit(1)

conf = sys.argv[1]
suffix = sys.argv[2]
dir = sys.argv[3]

if not os.path.isdir(dir):
	print("输入路径"+ dir +"有误")
	exit(2)


fopen = open(conf,"r")
lines = fopen.readlines()
for line in lines:
	str = line.strip()
	s = str.split(",",1)
	if s[1] == "":
		print("警告:文件"+s[0]+suffix+"不处理")
		continue
	source = os.path.join(dir,s[0]+suffix)
	if os.path.exists(source):
		output = dir + "/output"
		if not os.path.isdir(output):
			os.makedirs(output)
		src = os.path.join(output,s[0]+suffix)
		dest = os.path.join(output,s[1]+suffix)
		if os.path.exists(dest):
			print("警告:目标文件"+s[1]+suffix+"已经存在!"+s[0]+suffix+"重命名失败，跳过！")
			continue
		shutil.copyfile(source,src)
		os.rename(src,dest)
		print(s[0]+suffix+"->"+s[1]+suffix+"文件替换成功")
	else:
		print("警告:"+s[0]+suffix+"文件不存在!")
