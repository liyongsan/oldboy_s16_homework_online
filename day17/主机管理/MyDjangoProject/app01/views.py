from django.shortcuts import render,HttpResponse,redirect
from app01 import models

# Create your views here.

# def host(request):
#
#     # return HttpResponse("<h1>主机管理</h1>")
#     return render(request, "home_170525.html")

def home(request):
    # v = request.COOKIES.get('user')
    v = request.session.get('user')
    if v:
        nid=request.GET.get("id")
        user_list = models.HostList.objects.all()
        obj = models.HostList.objects.values('userinfo__username')
        if request.method == "POST":
            ipp = request.POST.get("ppp")
            portt = request.POST.get("ttt")
            res = models.HostList.objects.filter(hostname=ipp,port=portt).first()
            ret = {'status':True,'error':None}
            import json
            if res:
                return HttpResponse(json.dumps(ret))
            else:
                ret['status'] = False
                request['error'] = "主机名和端口已存在，请更换信息提交"
                return HttpResponse(json.dumps(ret))

        return  render(request, "home.html", {'user_list':user_list}, {'obj':obj})
    else:
        return redirect('/login/')


def login(request):
    if request.method == "POST":
        user = request.POST.get("uuu")
        pwd = request.POST.get("ppp")
        obj = models.UserInfo.objects.filter(username=user,password=pwd).first()
        ret = {'status':True,'error':None}
        import json
        if obj:
            request.session['user'] = user
            request.session['pwd'] = pwd

            return HttpResponse(json.dumps(ret))
        else:
            ret['status'] = False
            ret['error'] = "用户名或密码错误"
            return HttpResponse(json.dumps(ret))
    elif request.method == "GET":
        return render(request,"login.html")

def add(request):
    if request.method == 'POST':
        a_user = request.POST['a_user']
        a_port = request.POST['a_port']
        a_bm = request.POST['a_bm']
        models.HostList.objects.create(hostname=a_user,port=a_port,dp_id=a_bm)
    user_list = models.HostList.objects.all()
    return render(request, "home.html", {'user_list':user_list})

def del_host(request):
    nid=request.GET.get("id")
    models.HostList.objects.filter(id=nid).delete()
    user_list = models.HostList.objects.all()
    return render(request, "home.html", {'user_list':user_list})

def kk(request):

    return render(request,"模态对话框.html")


def aj(request):
    if request.method == "POST":
        user = request.POST.get("uuu")
    return HttpResponse("<h1>欢迎登录</h1>")


def add_host(request):
    if request.method == 'POST':
        a_user = request.POST['a_user']
        a_port = request.POST['a_port']
        a_bm = request.POST['a_bm']
        models.HostList.objects.create(hostname=a_user,port=a_port,dp_id=a_bm)
    user_list = models.HostList.objects.all()
    return render(request,"add_host.html",{'user_list':user_list})