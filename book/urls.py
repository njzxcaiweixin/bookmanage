from django.contrib import admin
from django.urls import path, re_path
from book import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('book/', views.show_books, name='book'),
    # path('books/', views.books)
    re_path(r'^book/(\d+)/$', views.detail, name='book'),
    path('create/', views.create),
    re_path(r'^delete/(\d+)/$', views.delete),
    # path('<int:bid>', views.delete()),
    path('areas/', views.areas, name='areas')
]