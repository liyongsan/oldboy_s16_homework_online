访问：
http://127.0.0.1/login 跳转登录界面
user=alex
pwd=123

跳转到 http://127.0.0.1:8000/show/

界面通过Django模板继承的方式来完成的
模板：modules


其中/show/ 可以通过对界面增删改查来操作MySQL数据库
新增用户名密码为新添加的账号密码
更改用户名密码选项是更改该用户的密码


数据库多表查询支持：
1.使用ForeignKey查询
2.ManyToManyField
3.OneToOneField
4.OneToManyField