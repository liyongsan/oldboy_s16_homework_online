#_*_ coding: utf-8 _*_

#�������
num=0

while num < 3:	#�ж��������Ƿ񳬹������������
	username=input('username: ')
	lock_check=open('lock.txt','r')
	for line in lock_check.readlines():		#�����ļ�����
		line=line.split()
		if username == line[0]:			#�ж��û����Ƿ���ȷ����
			exit(1)
	lock_check.close()
	password=input('password: ')	#�ж������Ƿ���ȷ
	lock_check.close()
	f=open('name.txt','r')	#��ȡname list
	match_flag = False
	for line in f.readlines():
		user,passwd = line.strip('\n').split()
		if username == user and password == passwd:		#�ж�����û���������ȷ��Ϊ��
			print('''OK,user %s information is matched!'''% (username))
			match_flag = True
	f.close()
	if match_flag == False:		#���û�������������ʱ����ƥ�䲻��ȷ������������
		print('User unmatched!')
		num +=1
	else:
		print('''Welcome %s login here!'''%(username))	#����ƥ�䣬��ӡ��ӭ����
		break
else:
	print('Your account is locked!')
	f=open('lock_file.txt','a')
	f.write(username + '\n')	#����3�δ��������˺�
	f.close()

