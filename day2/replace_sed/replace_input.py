#!/usr/bin/env python
#_*_ conding:utf-8 _*_
#交互式实现sed替换和文件按时间备份

import os
import sys
import time

dir = "/root/day2/homework/replace/"
time_local = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())


if len(sys.argv) != 1:
	print("Usage: ./test.py sed or backup")
	#print(len(sys.argv))
	exit(1)
else:
	dst = input('请输入您的选择:\n (1):替换文件内容\n (2):备份文件(Linux下使用)\n :')
	

	#if sys.argv[1] == "file":
	if dst == "1":
		file = input('请输入您要更改的文件名: ')
		source = input("请输入您要被替换的内容: ")
		dest = input('请输入您需要替换的内容: ')
		dir1 = "%s%s"%(dir,file)
		with open(file,'r+') as f:
			t = f.read()
			t = t.replace(source,dest) #替换文件内容
			f.seek(0,0) #读写偏移位置移到最开始处
			f.write(t)
	else:
		dir2 = input("请输入您要备份的文件名: ")
		dire = "%s%s"%(dir,dir2)
		os.system('cp -ra %s %s_%s_bak' % (dire2,dire2,time_local)) #备份文件内容，制定备份日期(linux下执行)
		#os.rename(dir,'%s_bak' % dir)
		exit(0)
