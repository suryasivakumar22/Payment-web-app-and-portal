"""pkpay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from payments import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('index/about',views.about),
    path('index/clients',views.clients),
    path('index/contact',views.contact),
    path('index/login',views.login),
    path('index/signup',views.signup),
    path('index/mobile',views.mobile),
    path('index/money',views.money),
    path('index/toll',views.toll),
    path('index/dth',views.dth),
    path('index/invlg',views.invlg),
    path('index/paygate',views.paygate),
    path('index/packs',views.packs),
    path('index/chbank',views.chbank),
    path('index/amt',views.amt),
    path('index/dybank',views.dybank),
    path('index/dybank2',views.dybank2),
    path('index/dybank3',views.dybank3),
    path('index/paysuccess',views.paysuccess),
    path('index/payfail',views.payfail),
    path('index/heyu',views.heyu)

]
