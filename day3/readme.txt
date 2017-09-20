针对员工信息文件，实现增删改查操作

要求：
1，可进行模糊查询，语法至少支持下面3种:
　　select name,age from staff_table where age > 22
　　select  * from staff_table where dept = "IT"
    select  * from staff_table where enroll_date like 2013,
2，查到的信息，打印后，最后面还要显示查到的条数 
3，可创建新员工纪录，以phone做唯一键，staff_id需自增,
4，可删除指定员工信息纪录，输入员工id，即可删除
5，可修改员工信息，语法如下:
　　UPDATE staff_table SET dept="Market" WHERE where dept = IT

使用方法：
选择5即可打印增删改查的使用方法，依次根据 提示输入即可