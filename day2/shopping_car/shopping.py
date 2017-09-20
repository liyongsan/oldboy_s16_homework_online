# -*- coding:utf-8 -*-
#购物车程序

shopping_car = []
product_list_tatol = "\033[31m---product list----\033[0m"
welcome = "\033[33m-----------welcome to shopping marketi----------\033[0m"
product_list = [
    ('iphone',6888),
    ('clothes',1000),
    ('car',200000),
    ('pc',5000),
    ('camera',1200),
    ('lenovo',998),
    ('cup',12),
    ('thinkpad',4500),
    ('notebook',6)
]
print(welcome)
salary = input("\033[32minput your salary: >>>\033[0m")
if salary.isdigit():
    salary = int(salary)
while True:
    print(product_list_tatol)
    for item in product_list:
        print(product_list.index(item)+1,item)
    choice = input("0 ('exit--------->>>')\n\033[36mchoice you want to buy:>>> ___ \033[0m")
    if choice.isdigit():
        choice = int(choice)
    if choice > 9 or choice < 0:
        print("\033[31mno this goods,请重新选择\033[0m")
        continue
    elif choice <=9 and choice >=1:
        if salary < product_list[choice-1][1]:
            print("\033[33m账户余额不足，请购买其他商品或者退出\033[0m")
            continue
        else:
            pass
        item_choice = product_list[choice-1]
        shopping_car.append(item_choice)
        print("\033[34myou buy goods is %s\033,"%(shopping_car))
        salary = salary - product_list[choice-1][1]
        print("\033[35myour balance is %d \033[0m"%(salary))

    elif choice == 0:
        print("\033[34myou buy goods is %s\033,"%(shopping_car))
        print("\033[35myour balance is %d\033[0m"%(salary))
        exit(0)
