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

    return render(request,'edit_students.html')