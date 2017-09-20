主机批量管理工具

    需求:
    主机分组
	用户验证
        登录后显示主机分组，选择分组后查看主机列表
        可批量执行命令、发送文件，结果实时返回
        主机用户名密码可以不同

    远程操作数据库

### 目录结构：
    Host-Manage
    │
    ├── ftpclient #客户端程序
            ├── README.txt
            ├── management.py #服务端入口程序
            ├── database #数据库

数据库jirauser信息如下：

│id│username│password
----------------------
│1 │alex    │123
----------------------
│2 │simon   │123
----------------------
│3 │jack    │456



### 注释
    可批量执行命令、发送文件
    上传命令格式： put database /tmp/db
    执行SQL格式： 正常SQL语句

   

示例：
username:alex
passord:123
auth success,welcome to login here!
(1): 主机管理
(2): 连接数据库
请输入您的选择:1
group2
group1
输入要操作的组名：group1
10.143.117.27
10.143.117.28
选择进行的操作的命令：ifconfig
-----------------------[10.143.117.28]-----------------------
eth1      Link encap:Ethernet  HWaddr 00:50:56:94:1C:AD  
          inet addr:10.143.117.28  Bcast:10.143.117.255  Mask:255.255.255.0
          inet6 addr: fe80::250:56ff:fe94:1cad/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:49558877 errors:0 dropped:0 overruns:0 frame:0
          TX packets:30349023 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:77601597702 (72.2 GiB)  TX bytes:4729936259 (4.4 GiB)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:16436  Metric:1
          RX packets:1969354 errors:0 dropped:0 overruns:0 frame:0
          TX packets:1969354 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:334650689 (319.1 MiB)  TX bytes:334650689 (319.1 MiB)


-----------------------[10.143.117.27]-----------------------
eth2      Link encap:Ethernet  HWaddr 00:50:56:94:35:9F  
          inet addr:10.143.117.27  Bcast:10.143.117.255  Mask:255.255.255.0
          inet6 addr: fe80::250:56ff:fe94:359f/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:38929910 errors:0 dropped:0 overruns:0 frame:0
          TX packets:28942690 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:28153625498 (26.2 GiB)  TX bytes:27480263229 (25.5 GiB)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:16436  Metric:1
          RX packets:83567 errors:0 dropped:0 overruns:0 frame:0
          TX packets:83567 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:13067456 (12.4 MiB)  TX bytes:13067456 (12.4 MiB)

