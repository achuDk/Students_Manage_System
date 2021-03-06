"""Student_Manager_System_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from app.views import classes,students,teachers

urlpatterns = [
    path('admin/', admin.site.urls),

    path('get_classes/',classes.get_classes),
    path('add_classes/',classes.add_classes),
    re_path(r'del_classes',classes.del_classes),
    re_path(r'edit_classes',classes.edit_classes),
    re_path(r'appoint_teachers',classes.appoint_teachers),

    re_path(r'get_students',students.get_students),
    re_path(r'add_students',students.add_students),
    re_path(r'del_students',students.del_students),
    re_path(r'edit_students',students.edit_students),

    re_path(r'get_teachers',teachers.get_teachers),
    re_path(r'add_teachers',teachers.add_teachers),
    re_path(r'del_teachers',teachers.del_teachers),
    re_path(r'edit_teachers',teachers.edit_teachers),
    re_path(r'appoint_classes',teachers.appoint_classes),
]
