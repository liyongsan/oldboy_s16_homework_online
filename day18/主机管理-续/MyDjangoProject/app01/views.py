from django.shortcuts import render,HttpResponse,redirect
from app01 import models

# Create your views here.

def insert_data(request):
    # models.Depart.objects.create(title="市场")
    # models.Depart.objects.create(title="运营")
    # models.Depart.objects.create(title="销售")

    # for i in range(1,10):
    #     models.UserInfo.objects.create(
    #         username = "alex%s" %i,
    #         password = "123%s" %i
    #     )

    # for i in range(145,174):
    #     models.HostList.objects.create(
    #         hostname="gomeholdings%s.com" %i,
    #         system_version = "ubun14.4"
    #     )
    return HttpResponse("xxxx")


def users1(request):
    from django.core.paginator import Paginator
    current_page = request.GET.get("p")
    Host_list = models.HostList.objects.all()
    paginator = Paginator(Host_list,10)
    page_obj = paginator.page(current_page)

    # return render(request,"users.html",{"Host_list":Host_list})
    return render(request,"users.html",{"page_obj":page_obj})

from utils.page import PageInfo

def users(request):
    v = request.session.get('user')
    if v:
        all_count = models.HostList.objects.all().count()
        page_info = PageInfo(request.GET.get('p'),10,all_count,request.path_info)
        host_list = models.HostList.objects.all()[page_info.start():page_info.end()]
        return render(request,"users2.html",{"host_list":host_list,"page_info":page_info})
    else:
        return redirect("/login/")

from django import forms
from django.forms import fields
from django.forms import widgets
class HostForm(forms.Form):
    hostname = fields.CharField(
            required=True,
            error_messages={'required':"主机名不能为空"},
            widget = widgets.TextInput(attrs={'class':"form-control"})
    )
    system_version = fields.CharField(
            required=True,
            error_messages={"required":"系统版本不能为空"},
            widget=widgets.TextInput(attrs={"class":"form-control"})
    )
    dp_id = fields.IntegerField(
            required=True,
            widget=widgets.Select(
                    attrs={'class': 'form-control'},
                    choices= []
            )
    )
    UI_id = fields.IntegerField(
            required=True,
            widget=widgets.Select(
                    attrs={'class': 'form-control'},
                    choices= []
            )
    )

    def __init__(self,*args,**kwargs):
        super(HostForm,self).__init__(*args,**kwargs)
        self.fields['dp_id'].widget.choices = models.Depart.objects.values_list('id','title')
        self.fields['UI_id'].widget.choices = models.UserInfo.objects.values_list('id','username')

def add_users(request):
    if request.method == "GET":
        obj = HostForm()
        return render(request,"add_users.html",{"obj":obj})
    else:
        obj = HostForm(request.POST)
        if obj.is_valid():
            print("验证通过",obj.cleaned_data)
            models.HostList.objects.create(**obj.cleaned_data)
            return redirect("/users")
        else:
            print("错误信息",obj.errors)
        return render(request,"add_users.html",{"obj":obj})

def add_aj(request):
    if request.method == "GET":
        obj = HostForm()
        return render(request,"add_aj.html",{"obj":obj})
    else:
        import json
        # obj2 = HostForm(data=request.POST)
        ret = {'status':True,'error':None}
        obj2 = HostForm(request.POST)
        if obj2.is_valid():
            models.HostList.objects.create(**obj2.cleaned_data)
            return HttpResponse(json.dumps(ret))
            # return HttpResponse("OK")
        else:
            ret['status'] = False
            ret['error'] = "请确认填写信息是否完整"
            return HttpResponse(json.dumps(ret))
            # return HttpResponse("ERROR")

def edit_users(request,uid):
    if request.method == "GET":
        Host = models.HostList.objects.filter(id=uid).first()
        obj = HostForm(initial={"hostname":Host.hostname,"system_version":Host.system_version,"dp_id":Host.dp_id,"UI_id":Host.UI_id})
        return render(request,"edit_users.html",{"uid":uid,"obj":obj})
    else:
        obj = HostForm(data=request.POST)
        if obj.is_valid():
            models.HostList.objects.filter(id=uid).update(**obj.cleaned_data)
            return redirect('/users')
        return render(request,"edit_users.html",{"uid":uid,"obj":obj})


def login(request):
    if request.method == "POST":
        user = request.POST.get("uuu")
        pwd = request.POST.get("ppp")
        obj1 = models.UserInfo.objects.filter(username=user,password=pwd).first()
        ret = {"status":True,"error":None}
        import json
        if obj1:
            request.session["user"] = user
            request.session["pwd"] = pwd
            return HttpResponse(json.dumps(ret))
        else:
            ret["status"] = False
            ret["error"] = "用户名或密码错误"
            return HttpResponse(json.dumps(ret))
    elif request.method == "GET":
        return render(request,"login.html")
