from django.db import models

# Create your models here.
#ORM 对象关系映射
# Python的类----------->数据表
# Python的类实例------> 表的记录
# Python的类属性------> 表的字段

class Books(models.Model):
    # nid=models.ImageField(primary_key=True)
    title=models.CharField(max_length=32)
    author=models.CharField(max_length=32)
    price=models.FloatField()
    pub_date=models.DateField()
