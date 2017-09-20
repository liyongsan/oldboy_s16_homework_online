功能实现:
    角色:学校、学员、课程、讲师
    要求:
	1. 创建北京、上海 2 所学校
	2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开
	3. 课程包含，周期，价格，通过学校创建课程 
	4. 通过学校创建班级， 班级关联课程、讲师
	5. 创建学员时，选择学校，关联班级
	5. 创建讲师角色时要关联学校， 
	6. 提供两个角色接口
	6.1 学员视图， 可以注册， 交学费， 选择班级，
	6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 查看班级学员列表 ， 修改所管理的学员的成绩 
	6.3 管理视图，创建讲师， 创建班级，创建课程
	7. 上面的操作产生的数据都通过pickle序列化保存到文件里


程序详解：
	三个视图：学员视图 讲师视图 管理视图 三个视图即为三个管理接口

	五个角色：学校、学员、课程、讲师、班级 五个角色即需要定义5个类

		① 创建北京、上海 2 所学校 
			分析：定义学校类，通过类去创建学校实例 
		② 创建linux , python , go 3个课程 ，linux\py 在北京开，go 在上海开 
			分析：定义课程类，通过课程类去创建课程实例
		③ 课程包含，周期，价格，通过学校创建课程 
			分析： 课程类里要包含周期、价格 课程实例通过学校类去创建

		④ 班级关联课程、班级关联讲师 
			分析：可以创建班级的时候需输入关联的课程，创建讲师的时候需输入关联的班级； 一个班级对应一个课程 一个班级对应一个讲师 
		⑤ 通过学校创建班级， 班级关联课程、讲师 分析：跟 ④一样

		⑥ 创建学员时，选择学校，关联班级 
			分析：定义学员类，创建时选择学校，选择班级， 通过学校类创建学员实例，班级类里面要有包含学员的信息的字典

		⑦ 创建讲师角色时要关联学校 
			分析： 之前一样，依然通过学校类去创建讲师实例

		⑧ 学员视图可以注册， 交学费， 选择班级 
			分析： 看 ⑥ 学员选择班级后，通过班级关联的课程，打印课程的学费

		⑨ 讲师视图， 讲师可以xxxxx 
			分析： 讲师视图登录需要讲师名，通过讲师名可以找到对应的班级实例，班级实例里包含班级名，课程名，学员信息等


	管理视图：
		管理视图具有的功能创建讲师， 创建班级，创建课程，这些都是通过学校创建（即通过学校类的方法调用），除了创建以外我们还需要增加查询讲师、班级、课程的功能（查看相应的信息）， 管理视图要有6个功能

	讲师视图：
		讲师视图可查看所授课的班级，班级学生信息 讲师视图具有2个功能

	学生视图：

		学生视图，要选择学校，选择班级（ 显示班级的名称，课程，价钱 ）， 添加到对应的班级内

class Student(object): '''学生类，包含姓名，年龄''' def __init__(self,student_name,student_age): self.student_name = student_name self.student_age = student_age
都跟它有关系，但是他是被关系的课程类： 只包含周期，价格，名称，可扩展其他信息，被关联，啥关联信息都不用存

class Course(): '''定义课程类，包含名称，价格，周期''' def __init__(self,course_name,course_price,course_time): self.course_name = course_name self.course_price = course_price self.course_time = course_time
跟三个都有关系，还一一对应（课程、讲师）的班级类： 看 ④⑥ 包含班级名，课程对应课程类（对应关系在本类里保存），班级学生成员字典，存放学生类，与讲师关联信息不再本类存

class Class(object): '''班级类，包含名称，课程，学生''' def __init__(self,class_name,course_obj): self.class_name = class_name self.class_courese = course_obj self.class_student = {} #学生字典 {学生名：学生实例}
关联性单一，只跟班级相好的讲师类： 看 ⑨ 包含讲师名、薪资；讲师关联班级（对应关系在本类保存）班级成员列表，存放班级名（做判断，不会重复）；通过班级名查看班级类里面的班级信息（包含学生），避免存双份数据

class Teacher(object): '''讲师类，定义teacher_name，teacher_salary，包含teacher_class''' def __init__(self, teacher_name, teacher_salary): self.teacher_name = teacher_name self.teacher_salary = teacher_salary self.teacher_calss = [] #班级列表 [s14,15] def teacher_add_class(self,class_name,class_obj): self.teacher_calss[class_name] = class_obj
内容最大，跟班级、课程、讲师都有关系的学校类： 包含学校名，学校地址，存放课程实例、班级实例、讲师实例，都是字典形式

class School(object): '''学校类，包含名称，地址，课程，班级，教师''' def __init__(self,school_name,school_addr): self.school_name = school_name self.school_addr = school_addr self.school_course = {} #学校所有的课程实例 {"课程名“：课程实例} self.school_class = {} self.school_teacher = {} #类型与course一致 #self.school_student = {} #可扩展学生
框架有了，类有了，业务逻辑还不so easy？！

		
