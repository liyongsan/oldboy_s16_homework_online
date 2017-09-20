#_*_ coding: utf-8 _*_

#定义变量
num=0

while num < 3:	#判断输错次数是否超过允许的最大次数
	username=input('username: ')
	lock_check=open('lock.txt','r')
	for line in lock_check.readlines():		#遍历文件内容
		line=line.split()
		if username == line[0]:			#判断用户名是否正确存在
			exit(1)
	lock_check.close()
	password=input('password: ')	#判断密码是否正确
	lock_check.close()
	f=open('name.txt','r')	#读取name list
	match_flag = False
	for line in f.readlines():
		user,passwd = line.strip('\n').split()
		if username == user and password == passwd:		#判断如果用户名密码正确则为真
			print('''OK,user %s information is matched!'''% (username))
			match_flag = True
	f.close()
	if match_flag == False:		#当用户名或密码有误时，则匹配不正确，请重新输入
		print('User unmatched!')
		num +=1
	else:
		print('''Welcome %s login here!'''%(username))	#正常匹配，打印欢迎界面
		break
else:
	print('Your account is locked!')
	f=open('lock_file.txt','a')
	f.write(username + '\n')	#输入3次错误，锁定账号
	f.close()

