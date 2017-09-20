from django.shortcuts import render,HttpResponse,redirect
from repository import models
from utils import check_code as ac
from io import BytesIO
import json
# Create your views here.


def do_favor(request):
    # ret = {"status":False,"error":""}
    ret = {"status":0,"error":""}
    if request.session.get("is_login"):
        news_id = request.GET.get("nid")
        current_user_id = request.session["user_info"]["user_id"]
        ct = models.Favor.objects.filter(user_info_id=current_user_id,news_id=news_id).count()
        if ct:
            models.Favor.objects.filter(user_info_id=current_user_id,news_id=news_id).delete()
            news_obj = models.News.objects.filter(nid=news_id).first()
            temp = news_obj.favor_count - 1
            models.News.objects.filter(nid=news_id).update(favor_count=temp)
            ret["status"] = 1
            return HttpResponse(json.dumps(ret))
        else:
            models.Favor.objects.create(user_info_id=current_user_id,news_id=news_id)
            news_obj = models.News.objects.filter(nid=news_id).first()
            temp = news_obj.favor_count + 1
            models.News.objects.filter(nid=news_id).update(favor_count=temp)
            ret["status"] = 2
            return HttpResponse(json.dumps(ret))
    else:
        return HttpResponse(json.dumps(ret))


def index(request):
    news_list = models.News.objects.all()
    return render(request,"index.html",{"news_list":news_list})



def login(request):
    back_code = ""
    if request.method == "GET":
        return render(request,"login.html")
    else:
        code = request.POST.get("code")
        if code.upper() == request.session["check_code"].upper():
            u = request.POST.get("username")
            p = request.POST.get("password")
            obj = models.UserInfo.objects.filter(username=u,password=p).first()
            if obj:
                request.session['is_login'] = True
                request.session['user_info'] = {'user_id': obj.nid,'user_name': obj.username}
                # return redirect('/index/')
                return redirect('/backend/news/')
            else:
                return render(request,"login.html")
        else:
            print("验证码错误")
            back_code = "验证码错误，请重新输入"
            return render(request,"login.html",{"back_code":back_code})


def check_code(request):
    img_obj,code = ac.create_validate_code()
    stream = BytesIO()
    img_obj.save(stream,'png')
    request.session["check_code"] = code
    return HttpResponse(stream.getvalue())

def comment(request):
    comment_list = [
        {'id': 1, 'news_id': 1, 'user_id': 10, 'content': "写的什么玩意呀", 'reply_id': None},
        {'id': 2, 'news_id': 1, 'user_id': 11, 'content': "还真不是玩意 ", 'reply_id': 1},
        {'id': 3, 'news_id': 1, 'user_id': 12, 'content': "写的真好 ", 'reply_id': 1},
        {'id': 4, 'news_id': 1, 'user_id': 11, 'content': "写的真好 ", 'reply_id': 3},
        {'id': 5, 'news_id': 1, 'user_id': 19, 'content': "sdfsfsdsd ", 'reply_id': None},
        {'id': 6, 'news_id': 1, 'user_id': 11, 'content': "你可以趣事了 ", 'reply_id': 2},
        {'id': 7, 'news_id': 1, 'user_id': 11, 'content': "好的", 'reply_id': 6},
    ]

    comment_dict = {}
    for row in comment_list:
        row['child'] = []
        comment_dict[row['id']] = row

    for row in comment_list:
        if row['reply_id']:
            reply_id = row['reply_id']
            comment_dict[reply_id]['child'].append(row)

    commen_reuslt = {}
    for k, v in comment_dict.items():
        if v['reply_id'] == None:
            commen_reuslt[k] = v
    cmt_str = create_html(commen_reuslt)
    return render(request,'comment.html',{'cmt_str': cmt_str})
    # return render(request,'answer.html',{'cmt_str': cmt_str})

def create_child_node(child_comment):
    prev = """
        <div class="comment">
            <div class="content">
        """
    for child in child_comment:
        tpl = '<div class="item">%s</div>'
        content = tpl % child['content']
        prev = prev + content
        if child['child']:
            node = create_child_node(child['child'])
            prev = prev + node

    end = """
            </div>
        </div>
        """
    return prev + end

def create_html(comment_result):
    prev = """
    <div class="comment">
        <div class="content">
    """

    for k,v in comment_result.items():
        tpl = '<div class="item">%s</div>'
        content = tpl %v['content']
        prev = prev + content
        if v['child']:
            node = create_child_node(v['child'])
            prev = prev + node

    end = """
        </div>
    </div>
    """
    return prev + end