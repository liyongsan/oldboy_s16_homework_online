from django.shortcuts import render,HttpResponse,render_to_response,redirect
from app01 import models

# Create your views here.


def login(request):
    if request.method=="POST":
        username=request.POST.get("username",None)
        password=request.POST.get("pwd",None)

        if username == "alex" and password=="123":
            return redirect("/show/")
    return render(request,"login.html")


def home(request):
    return render(request,"back.html",locals())


def profile(request):
    return render(request,"profile.html")


def message(request):
    return render(request,"message.html")


def show(request):
    if request.method == 'POST':
        a_user = request.POST['a_user']
        a_pwd = request.POST['a_pwd']
        models.UserInfo.objects.create(user=a_user,pwd=a_pwd)
    user_list = models.UserInfo.objects.all()
    return render(request,"show.html",{'user_list':user_list})


def show_del(request):
    # if request.method == 'POST':
        # a_user = request.POST['a_user']
    nid=request.GET.get("id")
    models.UserInfo.objects.filter(id=nid).delete()
    user_list = models.UserInfo.objects.all()
    return render(request,"show.html",{'user_list':user_list})


def show_edit(request):
    if request.method == 'POST':
        a_user = request.POST['a_user']
        a_pwd = request.POST['a_pwd']
        models.UserInfo.objects.filter(user=a_user).update(pwd=a_pwd)
    user_list = models.UserInfo.objects.all()
    return render(request,"show.html",{'user_list':user_list})


