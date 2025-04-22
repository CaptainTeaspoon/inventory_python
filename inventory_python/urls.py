"""
URL configuration for inventory_python project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_page, name='landing_page'),
    path('kontrolluebersicht/', views.kontrolluebersicht, name='kontrolluebersicht'),
    path('item/create/', views.item_create, name='item_create'),
    path('user/create/', views.user_create, name='user_create'),
    path('usergroup/create/', views.user_group_create, name='usergroup_create'),
    path('warehouse/create/', views.warehouse_create, name='warehouse_create'),
    path('item/update/<int:pk>/', views.item_update, name='item_update'),
    path('user/update/<int:pk>/', views.user_update, name='user_update'),
    path('usergroup/update/<int:pk>/', views.user_group_update, name='usergroup_update'),
    path('warehouse/update/<int:pk>/', views.warehouse_update, name='warehouse_update'),
    path('item/delete/<int:pk>/', views.item_delete, name='item_delete'),
    path('user/delete/<int:pk>/', views.user_delete, name='user_delete'),
    path('usergroup/delete/<int:pk>/', views.user_group_delete, name='usergroup_delete'),
    path('warehouse/delete/<int:pk>/', views.warehouse_delete, name='warehouse_delete'),
    path('item/delete/confirm/', views.item_delete, name='item_delete_confirm'),
    path('user/delete/confirm/', views.user_delete, name='user_delete_confirm'),
    path('usergroup/delete/confirm/', views.user_group_delete, name='usergroup_delete_confirm'),
    path('warehouse/delete/confirm/', views.warehouse_delete, name='warehouse_delete_confirm'),
    path('warehouses/', views.warehouse_list, name='warehouse_list'),
    path('search/', views.item_search, name='item_search'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    #path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
