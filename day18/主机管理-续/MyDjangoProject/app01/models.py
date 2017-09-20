from django.db import models

# Create your models here.

#主机管理的三个表
class Depart(models.Model):
    title = models.CharField(max_length=64)

class HostList(models.Model):
    hostname = models.CharField(max_length=64)
    system_version = models.CharField(max_length=64)
    dp = models.ForeignKey("Depart",default=1)
    UI = models.ForeignKey("UserInfo",default=1)

class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)





#抽屉页面设计
# import datetime
#
# #用户表
# class UserInfo_chouti(models.Model):
#     username = models.CharField(max_length=32)
#     password = models.CharField(max_length=32)
#     email = models.CharField(max_length=32)
#
# #点赞
# class Thumbs_Up(models.Model):
#     #点在用户
#     user_info_id = models.ForeignKey("UserInfo_chouti")
#
#
# #信息表
# class News_data(models.Model):
#     user_info_id = models.ForeignKey("UserInfo_chouti")
#     add_date = models.DateTimeField('保存日期',default = datetime.datetime.now)
#     mod_date = models.DateTimeField('最后修改日期', auto_now = True)
#     title = models.CharField(max_length=128)
#     content =  models.CharField()
#
#
# #评论表
# class Comment(models.Model):
#     #评论时间
#     # ctime = models.DateTimeField('最后修改日期', auto_now = True)
#
#     #评论人
#     user_info_id = models.ForeignKey("UserInfo_chouti")

#     #评论信息
#     news_id = models.ForeignKey("News_data")
#
#     #评论设备
#     # device = ?
#     #评论内容
#     content = models.CharField()

