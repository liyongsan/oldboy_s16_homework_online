#-*- coding:utf-8 -*-
province = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}
flag = True
try_province = 0
try_city = 0
try_area = 0
try_num = 0
try_input = 'No such %s about your query，try again!!!'
try_do = 'Three operation error, exit...'
#try_i = 0

while flag:
    if try_province < 3 : 
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        for sheng in province.keys():
            #try_i += 1
            #print(try_i,sheng)
            print(sheng)
        print('============================================================')
        province_choice1 = input('Please input the provinces to query：')
        #print(try_i)
 
        city_flag = True
        while city_flag:
            if try_city < 3 :    
                if province_choice1.strip() in province:
                    print('Please input city information:')
                    print('============================================================')
                    for city in province[province_choice1].keys():
                        print(city)
                    print('============================================================')
                    city_input = input('Please input city name：')
                    area_flag = True
                    while area_flag:
                        if try_area < 3 :
                            if city_input.strip() in province[province_choice1]:
                                print('Please input  area information: ')
                                print('============================================================')
                                for city_area in province[province_choice1][city_input]:
                                    print(city_area)
                                print('============================================================')
                                area_input = input('Please enter the area information to query：')
                                if area_input.strip() in province[province_choice1][city_input]:
                                    print('Your select is:',province_choice1,city_input,area_input)
                                    flag = False
                                    city_flag = False
                                    break
                                else:
                                    print(try_input %area_input)
                                    try_area += 1
                            else:
                                print(try_input % city_input)
                                try_city +=1
                                area_flag = False
                                
                        else:
                            print(try_do)
                            flag = False
                            city_flag = False
                            area_flag = False
                else:
                    print(try_input %('city'))
                    try_province += 1
                    city_flag = False
            else:
                print(try_do)
                flag = False
                city_flag = False

    else :
        print(try_do)
        flag = False
