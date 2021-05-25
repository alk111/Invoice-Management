"""DjangoInvoice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from invoice.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',NAV,name='nav'),
    path('login',USERLOGIN,name='login'),
    path('admin-login',ADMINLOGIN,name='admin-login'),
    path('admin_nav',ADMIN_NAV,name="admin_nav"),
    path('admin_logout',ADMINLOGOUT,name="admin_logout"),
    path('view_users',VIEWUSERS,name="view_users"),
    path('delete_users/<int:pid>',DELETEUSERS,name="delete_users"),
    path('signup',SIGNUP,name="signup"),
    path('user_nav',USERNAV,name="user_nav"),
    path('user_profile',USERPROFILE,name="user_profile"),
    path('edit_profile',EDITPROFILE,name="edit_profile"),
    path('user_logout',USERLOGOUT,name="user_logout"),
    path('change_pwd',CHANGEPASSWORD,name="change_pwd"),
    path('Add_Plan',AddPlan,name="Add_Plan"),
    path('Add_Subscription',AddSubscription,name="Add_Subscription"),
    path('invoice',INVOICE,name="invoice"),
    path('invoice-detail', view_invoice, name='invoice-detail'),
]
