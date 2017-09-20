from django.shortcuts import render
from repository import models
from utils.page import PageInfo

# Create your views here.


def home(request):
    return render(request,'home.html')

def order(request):
    return render(request, 'order.html')

def host(request):
    return render(request, 'host.html')


def user(request):
    return render(request, 'user.html')

def answer(request):

    comment_list = [
        {'id': 1, 'news_id': 1, 'user_id': 10, 'content': "脸长，额头窄。告诉我，哪里好看了？", 'reply_id': None},
        {'id': 2, 'news_id': 1, 'user_id': 11, 'content': "并不觉得她有多美。她下海拍片我都懒得下载。 ", 'reply_id': 1},
        {'id': 3, 'news_id': 1, 'user_id': 12, 'content': "知不知道天天这么炒，还没草就够了 ", 'reply_id': 1},
        {'id': 4, 'news_id': 1, 'user_id': 11, 'content': "抽屉越来越… ", 'reply_id': 3},
        {'id': 5, 'news_id': 1, 'user_id': 19, 'content': "比当年的朱莉还是差点 ", 'reply_id': None},
        {'id': 6, 'news_id': 1, 'user_id': 11, 'content': "还有杂技。。 ", 'reply_id': 4},
        {'id': 7, 'news_id': 1, 'user_id': 11, 'content': "抱着我的妹妹上花轿", 'reply_id': 6},
        {'id': 9, 'news_id': 1, 'user_id': 11, 'content': "小数点", 'reply_id': 7},
        {'id': 10, 'news_id': 1, 'user_id': 11, 'content': "边上这顶碟子伴舞的是中国杂技团的吧，这咱的传统项目啊", 'reply_id': 2},
        {'id': 11, 'news_id': 1, 'user_id': 11, 'content': "大脸盘子傻白甜", 'reply_id': 5},
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
    # return render(request,'comment.html',{'cmt_str': cmt_str})
    return render(request,'answer.html',{'cmt_str': cmt_str})

def create_child_node(child_comment):
    prev = """
        <div class="comment">
            <div class="content3">
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
    <div class="comment3">
        <div class="content3">
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
    # return render(request, 'answer.html')


def news(request):
    all_count = models.News.objects.all().count()
    page_info = PageInfo(request.GET.get("p"),3,all_count,request.path_info)
    news_list = models.News.objects.all()[page_info.start():page_info.end()]
    return render(request,"news.html",{"news_list":news_list,"page_info":page_info})


