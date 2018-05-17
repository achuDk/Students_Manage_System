from django.shortcuts import render,redirect
from app.models_pymysql import *

def get_teachers(request):
    tch_list = sql_exe('select * from teachers')
    # print('11111111',tch_list)
    cls_list = sql_exe('select distinct t.id,t.name,c.title from teachers t,classes c,cls_tch ct where t.id=ct.tid and c.id=ct.cid order by t.id')
    print('11111111111',cls_list)
    # cid_list = []
    # title_list = []
    # for obj in tch_list:
    #     tid = obj['id']
    #     ret = sql_exe("select cid from teachers inner join cls_tch as ct on teachers.id = ct.tid where tid=%s" % tid)
    #     for cid in ret:
    #         cid = list(cid.values())[0]
    #         cid_list.append(cid)
    #
    #     for cid in cid_list:
    #         title = sql_exe("select title from classes where id=%s" % cid)[0]['title']
    #         # print('222222',title)
    #         title_list.append(title)
    # print("111111111", cid_list)
    # print("333333333",title_list)

    return render(request,'get_teachers.html',{'tch_list':tch_list,'cls_list':cls_list})


def add_teachers(request):
    if request.method == "GET":
        return render(request,'add_teachers.html',locals())
    elif request.method == "POST":
        name = request.POST.get('name')
        sql_exe("insert into teachers (name) value ('%s')"%name)
        return redirect('/get_teachers')


def del_teachers(request):
    tid = request.GET.get('tid')
    # print(tid)
    ret = sql_exe('delete from teachers where id=%s'%tid)
    return redirect('/get_teachers')


def edit_teachers(request):
    if request.method == "GET":
        tid = request.GET.get('tid')
        old_name = sql_exe('select name from teachers where id=%s'%tid)
        return render(request,'edit_teachers.html',{'old_name':old_name,'tid':tid})
    elif request.method == "POST":
        """ 根据前端提交传参的形式(get 或 post)来获取 tid 参数值 """
        # tid = request.GET.get('tid')
        tid = request.POST.get('tid')
        new_name = request.POST.get('name')
        ret = sql_exe("update teachers set name='%s' where id=%s"%(new_name,tid))
        return redirect('/get_teachers')


def appoint_classes(request):


    return