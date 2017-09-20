#_*_ coding:utf-8 _*_

import os
def select(data):
    #查询语法一：select name,age from staff_table where age > 22
    #查询语法二：select * from staff_table where dept = IT
    #查询语法三: select * from staff_table where dept like IT
    data1 = data.split(" ")
    directory = ["staff_id", "name", "age", "phone", "dept", "enroll_date"]
    if data == ("select name,age from staff_table where age > %s" %(data1[7])):
                with open("nnd.txt", encoding="utf-8") as f:
                    list = []
                    list1 = []
                    list2 = []
                    for line in f:
                        i = line.strip().split(",")
                        a = [i[1], i[2]]
                        if i[2] > data1[7]:
                            list2.append(a)
                    for i in list2:
                        print(i)
                    print("查询到 %s 条符合的信息" %len(list2))
    else:
         with open("nnd.txt", encoding="utf-8") as f:
             ys = []
             for line in f:
                 i = line.strip().split(",")
                 if data == ("select * from staff_table where %s = %s" % (data1[5], i[directory.index(data1[5])])):
                     ys.append(line.strip())
                 elif data == ("select * from staff_table where %s like %s" % (data1[5], i[directory.index(data1[5])])):
                     ys.append(line.strip())
                 else:
                     continue
             for j in ys:
                  print(''.join(j))
             print("查询到 %s 条符合的信息" %len(ys))
             return 0
def add(data):
    #添加语法: "insert into staff_table(name,age,phone,dept,enroll-date) values(ys,22,11111111111,IT,2016-12-12)"
    data1 = data.split(",")
    data2 = []
    data3  = []
    for i in data1:
       j = i.replace('(',',')
       data2.append(j)
       #print(data2)
    data3 = data2[4:]
    data3[0] = data3[0].split(',')[1]
    data3[-1] = data3[-1].split(')')[0]
    print(data3)
    if data == ("insert into staff_table(name,age,phone,dept,enroll-date) values(%s,%s,%s,%s,%s)" %(data3[0],data3[1],data3[2],data3[3],data3[4])):
    	f=  open("nnd.txt",encoding="utf-8")
    	all_list = []
    	list = []
    	phone_list = []
    	for line in f:
        	i = line.strip().split(",")
        	q = i[3]
        	phone_list.append(q)

    	if data3[2] in phone_list:
        	        print("手机号已存在")
                	f.close()
    	else:
        	        f1 = open("nnd.txt", "r+", encoding="utf-8")
                	for line in f1:
                        	lines = line.strip().split(",")
                        	list.append(lines)
                        	i = line.strip().split(",")
                	w = str(int(list[-1][0]) + 1)
                	data3.insert(0, w)
                	print(data3)
                	data3 = ','.join(data3)
                	#f1.write("\n")
                	f1.write(data3)
                	f1.write("\n")
                	f1.close()
                	print("添加成功!!!")
    else:
    	print('语法不正确，请重新输入...')

def remove(data):
    #删除语法：delete from staff_table where staff_id = 12
   data1 = data.split(" ")
   if data == ("delete from staff_table where staff_id = %s" %data1[6]):
       with open("nnd.txt", encoding="utf-8") as f:
           list = []
           for line in f:
               i = line.strip().split(",")
               i1 = line.splitlines()
               q = i[0]
               if data1[6] == q:
                   i2 = ','.join(i1)
                   print(i2)
                   list.append(i)
       a = i2
       f = open("nnd.txt", encoding="utf-8")
       f1 = open("back", "a+", encoding="utf-8")
       for i in f:
           if a in i:
               i = i.replace(a, "").strip()
           f1.write(i)
           f1.flush()
       f.close()
       f1.close()
   os.remove("nnd.txt")
   os.rename("back","nnd.txt")
   print("删除成功！！！")
   return
def change(data):
    #修改请输：UPDATE staff_table SET dept = IT where dept = 运维
    data1 = data.split(" ")
    with open("nnd.txt", encoding="utf-8") as f,\
          open("back","w",encoding="utf-8")as f1:
        for line in f:
            lines = line.strip()
            print(lines)
            if  data1[9] in lines:
                lines = lines.replace(data1[9],data1[5])
            f1.write(lines)
            f1.write("\n")
            f1.flush()
    os.remove("nnd.txt")
    os.rename("back","nnd.txt")
    print("修改成功!!!")

def help1():
	print('''\t1):查询语法:\n\t\t1,select name,age from staff_table where age > 2;\n\t\t2,select * from staff_table where dept = IT;\n\t\t3,select * from staff_table where dept like IT;
    	2):添加语法:\n\t\t1,insert into staff_table(name,age,phone,dept,enroll-date) values(ys,22,11111111111,IT,2016-12-12)
    	3):删除语法:\n\t\t1,delete from staff_table where staff_id = 员工id
    	4):修改语法:\n\t\t1,UPDATE staff_table SET dept = IT where dept = 运维
    	5):退出''')


if __name__ == "__main__":
    msg = """
    1:查询
    2:添加
    3:删除
    4:修改
    5:帮助
    6:退出
    """
    msg_dict = {
        "1": select,
        "2": add,
        "3": remove,
        "4": change,
        "5": help1,
        "6": exit,
    }
    while True:
        print(msg)
        choice = input("输入序号>>:")
        if len(choice) == 0 or choice not in msg_dict: continue
        elif choice =='6':break
        elif choice =='5':help1()
        else:
            data = input("请输入数据>>:").strip()
            msg_dict[choice](data)
