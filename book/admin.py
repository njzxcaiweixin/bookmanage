from django.contrib import admin
from book.models import Bookinfo, Figure, Bookshop, District


# Register your models here.

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['bname', 'author', 'pub', 'price', 'pubdate', 'bread', 'isdelete']


class FigureAdmin(admin.ModelAdmin):
    list_display = ['fname', 'gender', 'zhiye', 'age', 'wenhua', 'bid']


class BookShopAdmin(admin.ModelAdmin):
    list_display = ['bsname', 'bookid']


class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'parent']


admin.site.register(Bookinfo, BookInfoAdmin)
admin.site.register(Figure, FigureAdmin)
admin.site.register(Bookshop, BookShopAdmin)
admin.site.register(District, DistrictAdmin)
