from django.shortcuts import render,HttpResponse,render_to_response,redirect

# Create your views here.

import datetime

def sayHello(request):
    s = 'Hello World!'
    current_time = datetime.datetime.now()
    html = '<html><head></head><body><h1> %s </h1><p> %s </p></body></html>' % (s, current_time)
    return HttpResponse(html)

def showStudents(request):
    list = [{id: 1, 'name': 'Jack'}, {id: 2, 'name': 'Rose'}]
    return render_to_response('student.html',{'students': list})


def login(request):
    # print("method",request.method)
    if request.method=="POST":
        # print("post",request.POST)
        username=request.POST.get("username",None)
        password=request.POST.get("pwd",None)

        if username == "alex" and password=="123":
            # return HttpResponse("登录成功!")

            return redirect("/back/")
    # return render(request,"login.html")
    return render(request,"login.html")

from student.models import *   #导入book
def add_books(request):
    #创建记录的两种方式： 1 create  2. sava
    # Books.objects.create(title="python",author="egon",price=12,pub_date="2000-12-12")

    b=Books(title="PHP",author="SAN",price=18.12,pub_date="2016-11-17")
    b.save()
    # return HttpResponse("添加成功！")
    return redirect("/back/")

def back(request):
    obj_list=Books.objects.all()
    return render(request,"back.html",locals())


def delete_books(request):
    nid=request.GET.get("id")
    Books.objects.filter(id=nid).delete()
    return redirect("/back/")


def edit_books(request):
    nid=request.GET.get("id")
    message=request.GET.get("message-text1",None)
    # b=Books.objects.get(id=nid)  #get获取的是单一对象  filter取到的是集合对象
    # b.price=100
    # b.save()   #效率较低
    Books.objects.filter(id=nid).update(price=100)
    return redirect("/back/")
    # return HttpResponse(request,nid)