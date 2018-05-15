from django.shortcuts import render,HttpResponse,redirect
from app.models_pymysql import *

# 查看数据
def get_classes(request):
    cls_list = sql_exe("select * from classes")
    return render(request,'get_classes.html',locals())

# 增加数据
def add_classes(request):
    if request.method == "POST":
        t = request.POST.get('title')
        ret = sql_exe("insert into classes (title) value ('%s')" %t)
        return redirect('/get_classes/')
    elif request.method == "GET":
        return render(request,'add_classes.html')

# 删除数据
def del_classes(request):
    cls_id = request.GET.get('cls_id')
    # print("=++++++>",cls_id)
    ret = sql_exe("delete from classes where id=%s"%cls_id)
    return redirect('/get_classes/')

# 修改数据
def edit_classes(request):
    if request.method == "GET":
        cls_id = request.GET.get('cls_id')
        print("=++++++>", cls_id)
        ret = sql_exe("select title from classes where id=%s"%cls_id)
        # print(">>>>>>",old_title)
        # print(old_title[0]['title'])
        old_title = ret[0]['title']
        return render(request,'edit_classes.html',locals())
    elif request.method == "POST":
        cls_id = request.POST.get('cls_id')
        # print("=++++++>", cls_id)
        new_title = request.POST.get('title')
        # print(">>>>>>",new_title)
        ret = sql_exe("update classes set title='%s' where id=%s"%(new_title,cls_id))
        return redirect('/get_classes/')


def appoint_teachers(request):
    return