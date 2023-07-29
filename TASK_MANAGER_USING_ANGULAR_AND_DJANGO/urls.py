"""TASK_MANAGER_USING_ANGULAR_AND_DJANGO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path
from CRUDTASKS import views

urlpatterns = [
    re_path(r'^task$', views.tasksApi),
    re_path(r'^task$', views.tasksApi),
    path('task/<int:id>', views.tasksApi),
    path('admin/', admin.site.urls),
    path('',views.working)
]
