"""gfg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from gfg.views import home
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('signout',views.signout,name='signout'),
    path('project',views.project,name='project'), #now i created this for project link
    path('add',views.ADD,name='add'),
    path('edit',views.EDIT,name='edit'),
    path('Update/<str:id>',views.Update,name='Update'),
    path('delete/<str:id>',views.delete,name="delete"),
    path('inovate',views.inovate,name='inovate'),
    path('donate',views.Donate,name='donate'),
    path('fund',views.Fund,name='fund'),
    path('addamt',views.addamt,name='AddAmt'),
    path('donaters1',views.donaters1,name='donaters1'),
    path('view',views.view,name='view'),
    path('payment',views.payment,name='payment'),
    path('addvalue',views.addvalue,name='addvalue'),
]
