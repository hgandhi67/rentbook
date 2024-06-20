"""
URL configuration for book_rental project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from book_rent_task import views 

urlpatterns = [
    path('admin-dashboard',views.dashboard, name = 'dashboard'),
    path("signup/",views.create_user, name="SignUp"),
    path("",views.open_signin,name='load_login'),
    path("signin/",views.singin, name="login"),
    # path("",views.search_book, name="search_books"),
    path("search-book/",views.openAPIdemo, name="view"),
    path("show-books/",views.load_page, name = 'load_view'),
    path('books-details/<path:key>/<int:pages>', views.load_book_details, name='load_details'),
    path('rent-book/<path:key>/<int:pages>/',views.rent_book, name="rent_book_mon"),
    path("signout/",views.signout, name="logout"),
    path("rent-conform-book/",views.rent_conform_book, name="conform-rent"),
    path("payment-success/",views.payment_success, name="payment_success"),
    path("admin-add-book/",views.admin_add_new_book, name="admin_add_book")
]
