from django.shortcuts import render,HttpResponse,redirect
from app.models_pymysql import *


def get_classes(request):
    cls_list = sql_exe("select * from classes;")

    return render(request,'classes.html',locals())


def add_classes(request):
    if request.method == "POST":
        t = request.POST.get('title')
        ret = sql_exe("insert into classes (title) value ('%s')" %t)
        return redirect('/get_classes/')
    elif request.method == "GET":
        return render(request,'add_classes.html')
