
import json
import paramiko
import threading
import pymysql

class Remotehost(object):
    #远程操作主机
    def __init__(self,host,port,username,password,cmd):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.cmd = cmd

    def command(self):
        #获取命令
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())   # 允许连接不在know_hosts文件中的主机
        ssh.connect(hostname=self.host, port=self.port, username=self.username, password=self.password)   # 连接服务器
        stdin, stdout, stderr = ssh.exec_command(self.cmd)              # 获取命令结果
        res ,err = stdout.read(),stderr.read()              # 三元运算
        result = res if res else err
        print("[%s]".center(50,"-")%self.host)
        print(result.decode())                                      # 打印输出
        ssh.close()

    def put(self):
        #上传
        try:
            transport = paramiko.Transport((self.host, self.port))
            transport.connect(username=self.username, password=self.password)
            sftp = paramiko.SFTPClient.from_transport(transport)
            sftp.put(self.cmd.split()[1], self.cmd.split()[2])              # 上传文件
            transport.close()
            print("\033[32;0m【%s】 上传 文件【%s】 成功....\033[0m"%(self.host,self.cmd.split()[2]))
        except Exception as error:                                # 抓住异常
            print("\033[31;0m错误:【%s】【%s】\033[0m"%(self.host,error))

    def run(self):
        #反射
        cmd_str = self.cmd.split()[0]
        if hasattr(self,cmd_str):
            getattr(self,cmd_str)()
        else:
            setattr(self,cmd_str,self.command)
            getattr(self,cmd_str)()

def pymysql_connect(cmd):
    conn = pymysql.connect(host="10.143.117.28",port=3306,user="root",passwd="123qwe",db="jira")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # cursor = conn.cursor()
    # cmd = input("sql:")
    effect_row = cursor.execute(cmd)
    conn.commit()
    ret = cursor.fetchall()
    global ret
    cursor.close()
    conn.close()

if __name__ == "__main__":
    #主程序
    name = input("username:").strip()
    pwd = int(input("passord:").strip())
    cmd="select * from jirauser;"
    pymysql_connect(cmd)
    flag = False
    while not flag:
        for line in ret:
            if name == line["username"] and pwd == line["password"]:
                print("\033[32;0mauth success,welcome to login here!\033[0m")
                flag = True
                break
            else:
                flag = False
        if flag == False:
            print("user and passwd is not current,try again!")
            exit(1)

    data = ("(1): 主机管理","(2): 连接数据库")
    for i in data:
        print(i)
    data_choice = input("请输入您的选择:")
    if int(data_choice) == 1:
            with open("database","r") as file:
                data_dict = json.loads(file.read())     #获取数据库信息
            for k in data_dict:                        #打印地址组
                print(k)

            group_choice = input("输入要操作的组名：").strip()
            if data_dict.get(group_choice):
                host_dict = data_dict[group_choice]     #定义主机字典
                for k in host_dict:                    #打印所选地址组所有的主机名
                    print(k)
                while True:
                    cmd = input("选择进行的操作的命令：").strip()
                    thread_list=[]
                    if cmd:                                 #命令不为空
                        for k in host_dict:
                            host, port, username, password=k,host_dict[k]["port"],host_dict[k]["username"],host_dict[k]["password"]
                            func = Remotehost(host,port,username,password,cmd)      #实例化类
                            t = threading.Thread(target=func.run)                   #创建线程
                            t.start()
                            thread_list.append(t)
                        for t in thread_list:
                            t.join()                                                #等待线程执行结果
            else:
                print("\033[31;0m操作组不存在\033[0m")
    elif int(data_choice) == 2:
        while True:
            cmd = input("请输入您的SQL语句或q退出:").strip()
            if cmd == "q":
                break
            pymysql_connect(cmd)
            for line in ret:
                print(line)
    else: print("请选择正确的序号：1或2")