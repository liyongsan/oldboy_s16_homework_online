
 主机管理：

1.http://127.0.0.1:8000/login/
登录页面使用ajax方式提交，通过session方式验证,账号密码从数据库中读取,验证成功后即跳转到主机管理页面(/users2/)
用户名：alex1
密码:1231

2.主机内容正文部分采用Form表单+Ajax提交+分页展示，具有查看、增加和编辑功能
	编辑页面采用直接提交Form表单形式提交请求(/edit_users-(\d+)/)
	新增主机页面采用Ajax提交Form表单(/add_aj/)

3.抽屉数据库表机构设计
共四张表,分别为用户表，信息表，点赞表和评论表，具体结构如下:

	用户表:
	userinfo:
		#用户名
		username
		#密码
		password
		#邮箱
		email
		
	信息表:
	newsType
		userinfo
		newsType
		title
		url
		content
		
	点赞表:
		#点赞者
		userinfo_id
		#点在信息
		news_id
		#点赞时间
		ctime
		
	评论表:
	Comment:
		#创建时间
		ctime
		#发表设备
		device
		#发表内容
		content
		#评论人
		userinfo_id