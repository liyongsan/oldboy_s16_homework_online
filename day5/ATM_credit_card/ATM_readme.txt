﻿一、主程序credit_card.py开始
   1、生成today今天的日期和星期数weekoftoday
   2、定义currusers：实例化modules下的users.py中的类Users
   3、初始化对账单report.create_statement_main()
       （1）、从database目录下的文件creditcard中读取信用卡列表
       （2）、循环列表调用 create_card_statement
       （3）、create_card_statement函数说明
            3.1 获取当前日期currday和today
            3.2 如果当天是22号出帐日：
              3.2.1 赋值startday,endday,startdate,enddate,statement_key出帐起始结束时间
              3.2.2 获取卡号对应的消费流水列表dbapi.load_bill_report(cardno, startdate, enddate)
              3.2.3 statement_dict的信息追加到信用卡帐单信息中。
   4、循环菜单
       （1）、判断用户是否登录，并输出相应用户信息
              未登录输出template.index_default_menu.format("", today, common.numtochr(weekoftoday))
              否则输出template.index_logined_menu.format("欢迎您: {0}".format(curruser.name), today,common.numtochr(weekoftoday))
       （2）、输出用户选择菜单
       （3）、输入5，则退出菜单
       （4）、输入1，首先加载当年用户信息curruser.db_load()，然后调用doshopping(curruser)
       （5）、输入2，首先加载当年用户信息curruser.db_load()，然后调用user_login(curruser, today, weekoftoday)
       （6）、输入3，调用card_center(curruser)信用卡中心
       （7）、输入4，调用manager(curruser)后台管理
   5、菜单1：doshopping商城函数
       （1）、实例化商城，调用shopping.Shopping()
       （2）、循环开始，输出商品菜单shoppobj.welcome_menu
       （3）、输入编号选择并赋值shop_cassify_id，并进行输入验证判断
       （4）、输入值为4，进行购物车商品显示shopping.Shopping.print_goods_list(shoppobj.shopping_cart)
              并显示common.show_message("当前购物车共有 {0} 件商品,合计 {1} 元）
       （5）、输入值为5，shoppobj.payfor_shopcart(userobj)，无错误，输出支付成功
       （6）、输入值为1-3，则调用shoppobj.get_goods_list_by_typeid()，显示商品分列表
       （7）、第二层循环开始，并显示指定商品分类下的所有商品列表(Shopping类静态方法)
              shopping.Shopping.print_goods_list(goods_list)
       （8）、选择商品编号goods_id,加入购物车，并对输入进行判断
            8.1 如果输入为q,返回上一层
            8.2 调用商品加入购物车函数shoppobj.add_shopping_card(goods_id)
            8.3 如果返回正确，则显示购物车所有商品信息shopping.Shopping.print_goods_list(shoppobj.shopping_cart)，并输出common.show_message("已将商品加入购物车!", "INFORMATION")
               第三层循环开始，显示“继续购物(y) or 返回上一级(q)”，
            8.4 如果返回失败，则输出common.show_message("添加购物车失败,请检查输入商品编号是否正确!", "ERROR")，并continue
   6、菜单2：user_login(curruser, today, weekoftoday)用户登录
       （1）、循环开始
       （2）、判断用户是否登录成功userobj.islogin，
            2.1 如果已经登录，则显示个人中心菜单 template.index_user_center.format(userobj.name, today, common.numtochr(weekoftoday)) 
            2.2 输出选择功能菜单，选择6，返回上级菜单
            2.3 如果选择1-5，则通过反射来执行，从 template 模块查找各按键对应的模块
                func_dict = template.user_center_func
            2.4 根据输出的数字，赋值相应的模块名称,modulepy = __import__(func_dict[_choose]["module"])
            2.5 如果选择的是1，2，5，则赋值modulesobj 、classobj、func
   7、菜单3：card_center(curruser)信用卡中心
       （1）、判断用户是否登录
            1.1 已登录，则重新load一下数据userobj.db_load()，并获取到绑定的信息卡信息cardno = userobj.bindcard
            1.2 获得信用卡对象card = CreditCard(cardno)
            1.3 如果未登录，则进行循环，让用户输入信用卡和密码进行认证
       （2）、显示登录输出菜单index_ATM，循环开始：
       （3）、输入common.input_msg("请选择功能: ", ("1", "2", "3", "4", "5"))
       （4）、如果输入是5，就返回上一层循环
       （5）、如果输入是1，则查看信用卡信息
       （6）、如果输入是2，则进行提现菜单
            6.1 如果card.frozenstatus状态是1，则提示“卡已冻结,请联系客服”
            6.2 否则提示“信用卡提现将收取 {0}% 的手续费!”
            6.3 循环开始，提示"请输入要提现的金额(q返回):"
            6.4 输入正确的话，提示输入信用卡密码进行确认
            6.5 执行提现函数card.fetch_money(float(cost), cardpasswd)，并根据返回结果进行输出相应信息
       （7）、如果输入是3，则进入转帐菜单
            7.1 如果card.frozenstatus状态是1，则提示“卡已冻结,请联系客服”
            7.2 否则提示“信用卡转帐将收取 {0}% 的手续费!”
            7.3 循环开始，提示"请输入要转账的卡号(q返回)"
            7.4 对卡号是数字，则生成一个trans_cardobj = CreditCard(trans_cardno)
            7.5 进行卡号判断存在的话，提示是转账的金额，
            7.6 如果金额正确并输入信用卡密码进行确认
            7.5 执行转帐函数card.translate_money(float(trans_cost), cardpasswd, trans_cardobj) ，并根据返回结果进行输出相应信息  
       （8）、如果输入是4，则进入还款菜单
            8.1 调用card.recreate_statement()函数，更新一下对账单信息
            8.2 循环开始，获取对账单所有列表interest_list = card.load_statement_list()
            8.3 获取还未还款的记录并显示message_info = report.print_statement_list(card.cardno, interest_list)
            8.4 如果有要还款的记录，则显示具体帐单信息
            8.5 请选择还款的16位账单号，然后进行判断，
            8.6 输出正确，则显示指定单号的相应对账单信息report.print_statement_detail
            8.7 输入还款金额，并更新已还款金额 = 现在还的金额 + 已经还的金额
            8.8 需要还款数 = 消费总费用 + 利息 ，并判断是否已还清，如果还清则设置interest_list[i][pay_serno]["isfinished"] = 1
            8.9 如果未还清，则显示“您尚未全部还款,请在还款日前尽快还款!”
            8.10 将还款后的信息写入数据库更新dbapi.write_statement_list(card.cardno, interest_list)
            8.11 显示是否继续还款。
   8、菜单4：主菜单后台管理模块manager(userobj):
       （1）、用户是否登录，是否是角色是否是admin
       （2）、是admin,进入循环，显示template.index_admin
       （3）、选择菜单，输入1时，进入创建新用户调用User类中的init_user_info()函数
       （4）、选择菜单，输入2时，进入删除用户菜单调用get_users()函数
            4.1 get_users() 显示用户的信息,用户新建、删除、解锁用户时显示用户基本信息
            4.2 输入操作的用户名
            4.3 创建一个用户实例_deluser = Users()，并赋值_deluser.username = username
            4.4 _deluser.load_user_info()判断，如果用户名存在,load用户信息成功，显示用户信息，返回用户
            4.5 用户不存在，返回失败
            4.6 调用_user.del_user()，并显示删除用户成功
       （5）、选择菜单，输入3时，进行锁定用户菜单调用get_users()函数，方式同上
       （6）、选择菜单，输入4时，进入发行信用卡菜单
            6.1 调用newcard = fill_card_info()函数，填充信用卡资料信息，返回一个信用卡对象
            6.2 循环开始，输入卡号，并判断卡号是否存在，不存在退出循环
            6.3 在依次输入密码，额度等信息，并返回一个信用卡对象
       （7）、选择菜单，输入5时，进入冻结信用卡
            7.1 输入要操作卡号
            7.2 card = CreditCard(cardno)，实例化信用卡
            7.3 判断信用卡是否存在card.card_is_exists
            7.4 存在则输入卡信息，并在次确定是否冻结
            7.5 card.frozenstatus = 1设置卡的标志位，card.update_card()更新信用卡文件
       （8）、选择菜单，输入0时，返回上层菜单

 
二、包conf说明：
   1、errorcode.py介绍:
       定义系统错误代码表：NO_ERROR，USER_NOT_EXISTS，CARD_NOT_BINDED，BALANCE_NOT_ENOUGHT，CARD_OWNER_ERROR，CARD_PASS_ERROR
   2、settings.py介绍：定义一系列变量值
       2.1 定义程序文件主目录BASE_DIR，并加入环境变量
       2.2 定义数据库信息DATABASE
       2.3 定义日志文件存放路径LOG_PATH
       2.4 定义账单报表文件路径REPORT_PATH
       2.5 定义用户登录失败最大次数ERROR_MAX_COUNT
       2.6 定义日息费率EXPIRE_DAY_RATE
       2.7 定义转账、提现手续费FETCH_MONEY_RATE
       2.8 定义信用额度CREDIT_TOTAL
       2.9 定义每月账单日期STATEMENT_DAY
   3、template.py介绍：该模块用来定义系统的菜单模板
       3.1 主程序中的主菜单index_default_menu
       3.2 主程序中的用户登录后的显示菜单index_logined_menu
       3.3 主程序中的用户中心菜单index_user_center
       3.4 用户中心按键对应功能模块user_center_func
       3.5 购物模块的主菜单, menu 菜单在shopping模块中内部构造shopping_index_menu 
       3.6 账单报表显示模板report_bill
       3.7 购物历史记录显示模板shopping_history
       3.8 后台管理模板index_admin
       3.9 ATM 管理模块index_ATM
       3.10 显示用户基本信息模板user_info
       3.11 显示信用卡基本信息模板card_info
       3.12 信用卡对账单列表模板report_statement_list
       3.13 信用卡对账单详细模板report_statement_detail

三、包database介绍：
   1、init_db.py介绍：
       1.1 定义商品列表_shopping_list
       1.2 定义用户列表_user_list
       1.3 定义信用卡列表_creditcard_list
       1.4 函数init_db_shoppingmark() 初始化购物商城数据表 shoppingmark.db
       1.5 函数init_db_users() 初始化用户数据表 users.db
       1.6 函数init_db_creditcard() 初始化信用卡数据表 creditcard.db
       1.7 执行init_database()，通过反射初始化数据表分别调用以上三个函数

四、包dbhelper介绍:
   1、dbapi.py介绍：
       1.1 函数append_db_json(contant, filename)，将信息以 json 格式写入数据表文件(追加)
       1.2 函数write_db_json(contant, filename)，将信息以 json 格式写入数据表文件（覆盖）
       1.3 函数load_data_from_db(tabename)，从指定的数据表中获取所有数据,通过 json 方式将数据返回
       1.4 函数load_bill_report(cardno, startdate, enddate)，从信用卡对账单中获取指定卡的对账信息数据, 获取某一个时间段内的数据
       1.5 函数load_shop_history(user, startdate, enddate)，查找报表记录中的指定用户的购物历史记录,将结果存入到列表中
       1.6 函数load_statement_list(cardno)，从对账单中获取记录
       1.7 函数write_statement_list(cardno, db_list)，将对账单记录写入对账单文件，更新


五、包modules介绍：
1、users.py介绍之类Users:
   1、定义私有变量：__database 值为database下的user.db
   2、定义用户的静态变量
   3、定义动态方法db_load(self.dict_user = dbapi.load_data_from_db(self.__database)),即调用dbapi模块中的load_data_from_db方法来展示用户信息
   4、定义login函数，输入用户名和密码
       （1）、调用user_exists，判断用户是否存在，不存在则使用common.show_message进行异常颜色输出。
       （2）、如存在则调用 用户登录模块_user_login ,首先对输入的密码参数进行md5计算_password = common.encrypt(password)，调用common模块中的encrypt函数，并进行用户信息的判断的赋值
       （3）、判断是否用户被锁定
       （4）、判断用户是否登录成功，成功则break退出，失败则输出异常信息
       （5）、连续三次登录失败，则设置用户锁定标识为1，并update_user更新到user.db
       （6）、重置trycount 重置次数
   5、update_user即为将dict_user用户列表信息进行回写文件
   6、定义用户存在函数user_exists、创建函数create_user、删除函数del_user、锁定函数unlock_user
   7、创建并init_user_info初始化用户信息，输入各种信息后，调用 create_user来生成用户
   8、定义静态方法user_auth，用于用户登录验证装饰器
   9、定义bind_card函数判断卡绑定
   10、注销用户函数logout，将系统属性置空
   11、个人中心 - 修改密码函数modify_password
   12、修改用户信息modify_user_info
       （1）、首先输出当前的用户信息
       （2）、输入新的用户信息
       （3）、输入新的信用卡信息，并创建一个新的卡对象，调用CreditCard模块：cardobj = CreditCard
       （4）、判断信用卡是否存在
       （5）、输入其他信息，并update_user回写文件
   13、根据用户名获取用户信息load_user_info


2、shopping.py之类Shopping：
   1、定义私有变量：__welcome_title 菜单标题、__database 数据库文件、__shop_report_file购物报表
   2、定义__init__: 特别定义方法
         （1）、获取数据表数据self._get_shop_market()
         （2）、购物商城欢迎菜单self._construct_title_menu() 
   3、_get_shop_market方法：加载购物商品信息dbapi.load_data_from_db(shoppingmarket.db)
   4、_construct_title_menu方法：输出购物商城菜单
       self.welcome_menu = self.__welcome_title.format(menu="".join(_menu))
   5、get_goods_list_by_typeid方法：根据用户选择的商品分类编号,获取该分类下所有商品
   6、定义静态方法print_goods_list：列表中的商品信息输出到屏幕,商品列表或购物车商品列表
         （1）、输出商品信息标题
         （2）、循环输出商品具体信息
   7、定义方法add_shopping_card(self, goodsid)：根据商品编号加入购物车
         （1）、定义变量_goods_tuple ，即具体的商品列表
         （2）、开始查找输入的商品编号，并加入购物车列表中，并计算金额
         （3）、成功后break
         （4）、返回return 成功与否
   8、定义payfor_shopcart结算方法，并调用@Users.user_auth认证模块作装饰器
       购物车结算模块,功能包括：购物车付款、购物记录写入文件
         （1）、判断用户是否绑定信用卡，如无，则返回错误，有，则继续、
         （2）、实例化信用卡类cardobj = CreditCard(userobj.bindcard)
         （3）、判断信用卡余额是否大于购买金额，如果不够，输出额度不够，否则继续
         （4）、调用common.create_serialno()，生成一个流水号
         （5）、调用卡的支付模块进行支付cardobj.card_pay(self.shopping_cost, 1, serno)
                    支付扣款 
                    记录消费流水对账单,将发生了费用还没有还款的账单信息写入文件 report_bill 中
                    更新信用卡可透支余额信息到数据库 creditcard.db
         （6）、记录购物流水shopping_record，并写入报表记录文件shopping_history
         （7）、购物结算完成后将对象的购物车清空shopping_cart.clear(), 购物车商品总价清0 ,待下次购物
         （8）、返回错误代码


3、creditcard.py之类CreditCard：
   1、指定数据表__database的表creditcard
   2、定义信用卡额度，信用卡透支余额，信用卡日息，提现手续费率，信用卡状态等变量
   3、定义_load_card_info函数，用户输入的卡号获取信用卡信息
   4、定义card_is_exists函数，判断输入的信用卡是否存在
   5、定义card_pay(self, cost, paytype, sereialno)函数，信用卡支付,从信用卡可透支余额中扣费
        （1）、根据传入的paytype的值，定义payfor的名称，例：1:消费、2:转账、3:提现、4:手续费
        （2）、支付扣款self.credit_balance -= cost
        （3）、定义_tmp_bill_record，记录消费流水对账单
        （4）、将消费流水对账单写回到文件report_bill
        （5）、更新信用卡可透支余额信息到数据库 creditcard.db
   6、定义新发行信用卡create_card函数，根据输入的卡号密码等信息并更新到creditcard.db
   7、定义信用卡更新update_card函数，根据输入的卡号密码等信息并更新到creditcard.db
   8、定义转账、提现时验证操作_pay_check函数，转账、提现时验证操作，判断卡的余额与支付密码是否正确。并   返回错误类型码
   9、定义提现函数fetch_money(self, count, passwd)
        （1）、根据传入的取现金额，计算取现+手续费总额
        （2）、调用_pay_check函数，根据返回值进行操作。
        （3）、如果返回值是errorcode.NO_ERROR，则调用card_pay函数将取现金额和手续费计帐，并回写文件
        （4）、并返回errorcode.NO_ERROR
   10、定义信用卡转账函数translate_money(self, trans_count, passwd, trans_cardobj)
        （1）、根据传入的转帐金额，计算转帐+手续费总额
        （2）、调用_pay_check函数，根据返回值进行操作。
        （3）、如果返回值是errorcode.NO_ERROR，则调用card_pay函数将转帐金额和手续费计帐，并回写文件
        （4）、并给对方卡充值,trans_cardobj.credit_balance += trans_count，并调用trans_cardobj.update_card()写入数据库文件
        （4）、并返回errorcode.NO_ERROR
   11、定义对账单列表数据函数load_statement_list，调用dbapi.load_statement_list(self.cardno)
   12、定义recreate_statement函数，实现今天的日期将当前卡的对账单重新生成,主要对过了还款日的账单重新生    成利息信息
        （1）、获取当前日期today
        （2）、获取卡的对账单信息card_statement = dbapi.load_statement_list(self.cardno)
        （3）、如果有记录，进行循环读取，并判断isfinished字段是否是1，是则加记录加到临时列表tmp_list
        （4）、未还款，则获取pdate还款时期，并判断是否过期
        （5）、如果过期则计算利息：record[k]["interest"] = v["total"] * settings.EXPIRE_DAY_RATE * day_delta
        （6）、将过期或非过期的记录都加到临时列表tmp_list
        （7）、将更新过的列表写入文件，替换原有信息dbapi.write_statement_list(self.cardno, tmp_list)

4、common.py介绍：
   1、函数verification_code()，用来生成一个4位的验证码，并返回验证码
   2、函数encrypt(string)，用来字符串加密
   3、函数write_log(content)，用来写错误日志
   4、函数get_chinese_num(uchar)，用来计算汉字的个数
   5、函数show_message(msg, msgtype)根据msgtype类型，对print函数进行封装，根据不同类型显示不同颜色
   6、函数create_serialno()，用来生成一个消费、转账、提款时的流水号，不重复
   7、函数numtochr(num_of_weekday)，将数字星期转换为中文数字
   8、函数input_msg(message, limit_value=tuple())，判断input输入的信息是否为空的公共检测函数,为空继续输入,不为空返回输入的信息
   9、函数input_date(msg, default_date)，对输入的日期进行判断是否正确 yyyy-mm-dd or yyyy-m-d

5、report.py介绍： 账单生成模块
   1、导入calendar，timedelta等模块
   2、函数get_date()，用来用户输入一个时间段,如果显示报表是要提供开始、结束日期,返回开始，结束时间
       2.1 调用common.input_date来生成一个开始日期startdate
       2.2 调用common.input_date来生成一个结束日期enddate
       2.3 返回一个时间的字典
   3、函数print_shopping_history(userobj)，个人中心 - 购物历史记录打印模块
   4、函数print_bill_history(userobj) ，个人中心-账单明细 打印模块
   5、函数create_card_statement(cardno)，生成信用卡对账单
   6、函数create_statement_main()，卡对账单初始化模块,从卡数据库文件中加载所有卡号，对所有卡调用生成对账单模块
   7、函数print_statement_list(cardno, list_info)，将卡号对应的未还款记录显示出来
   8、函数print_statement_detail(cardno, serino, details)，还款模块 - 用户选择还款的单号后，显示详细的还款对账单及流水信息