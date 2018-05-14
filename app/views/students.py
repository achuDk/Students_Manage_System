from django.shortcuts import render,redirect
from app.models_pymysql import *

def get_students(request):
    stu_list = sql_exe(" select students.id,name,age,gender,classes.title "
                       "from students inner join classes on students.cid = classes.id")
    return render(request,'get_students.html',locals())

def add_students(request):
    if request.method == "GET":
        cls_list = sql_exe("select * from classes")
        return render(request,'add_students.html',locals())
    elif request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        cid = request.POST.get('cid')
        ret = sql_exe("insert into students (name,age,gender,cid) values ('%s',%s,'%s',%s)"%(name,age,gender,cid))
        return redirect('/get_students')

def del_students(request):
    sid = request.GET.get('sid')
    sql_exe('delete from students where id=%s'%sid)
    return redirect('/get_students')

def edit_students(request):
    if request.method == "GET":
        cls_list = sql_exe("select * from classes")
        sid = request.GET.get('sid')
        old_name = sql_exe('select name from students where id=%s'%sid)[0]['name']
        old_age = sql_exe('select age from students where id=%s'%sid)[0]['age']
        old_gender = sql_exe('select gender from students where id=%s'%sid)
        old_class = sql_exe('select title from classes where id=(select cid from students where id=%s)'%sid)
        return render(request,'edit_students.html',locals())
    if request.method == "POST":
        sid = request.GET.get('sid')
        new_name = request.POST.get('name')
        new_age = request.POST.get('age')
        new_gender = request.POST.get('gender')
        new_cid = request.POST.get('cid')
        print('>>>>>>>>>>>',new_name,new_age,new_gender,new_cid)
        ret = sql_exe("update students set name='%s',age=%s,gender='%s',cid=%s where id=%s"%(new_name,new_age,new_gender,new_cid,sid))
        return redirect('/get_students')