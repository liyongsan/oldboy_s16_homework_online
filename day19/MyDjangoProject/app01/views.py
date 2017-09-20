from django.shortcuts import render,HttpResponse,redirect
from app01 import models
from utils.utils import BaseReponse
# Create your views here.
from utils.page import PageInfo
from app01 import forms


def test(request):
    # models.UserInfo.objects.create(username="alex",password="123")
    # for i in range(115,135):
    #     models.News.objects.create(
    #             title="自信满满%s"%i ,
    #             img="守望棒棒锤%s" %i,
    #             summary="无连号也无6和8，这块普通车牌从5000元拍到74万，如今挂在2000万的拉法上！有些事让人想不明白 + %s" %i,
    #             nt_id=models.News_Type_Choices.objects.get(id=6),
    #             u=models.UserInfo.objects.get(id=3)
    #     )

    return HttpResponse("OK")

def chouti(request):
    v = request.session.get('user')
    if v:
        all_count = models.News.objects.all().count()
        page_info = PageInfo(request.GET.get('p'),10,all_count,request.path_info)
        all_list = models.News.objects.all()[page_info.start():page_info.end()]
        return render(request,"chouti.html",{"all_list":all_list,"page_info":page_info})
    else:
        return redirect("/login/")

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

import json
def ajax_upload(request):
    import os
    response = BaseReponse()
    try:
        obj = request.FILES.get('fffff')
        file_path = os.path.join('static',obj.name)
        f = open(file_path, 'wb')
        for chunk in obj.chunks():
            f.write(chunk)
        f.close()
        response.status = True
        response.data = file_path
    except Exception as e:
        response.status = False
        response.error = "上传失败"
    print(file_path)
    return HttpResponse(json.dumps(response.__dict__))


def login1(request):
    response = BaseReponse()
    try:
        obj = forms.LoginForm(request.POST)
        if obj.is_valid():
            # models.UserInfo.objects.filter(username=obj.cleaned_data['username'],pwd=obj.cleaned_data['pwd'])
            v = models.UserInfo.objects.filter(**obj.cleaned_data).count()
            if v:
                response.status = True
            else:
                response.status = False
                response.error = "用户名或密码错误"
        else:
            print(obj.errors)
            response.status = False
            response.error = "asdasdf"
            response.error = obj.errors
    except Exception as e:
        response.status = False
        response.error = '请求失败'
    return HttpResponse(json.dumps(response.__dict__, ensure_ascii=False))