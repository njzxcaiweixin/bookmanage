# Create your views here.
from datetime import date
from django import forms

from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from book.models import Bookinfo, Figure, District
from book.forms import ContactForm

def my_render(request, template_path, context_dict):
    # temp = loader.get_template(template_path)
    # context = RequestContext(request, context_dict)
    # res_html = temp.render(context)
    # return HttpResponse(res_html)
    return render(request, template_path, context_dict)


def home(request):
    return HttpResponse('你好，Django!')


def index(request):
    # return HttpResponse('你好，伙计们!')
    # cont = '这是模板参数传递数据 '
    # views_list = ["菜鸟教程1", "菜鸟教程2", "菜鸟教程3"]
    # views_str = "<a href='https://www.runoob.com/'>点击跳转</a>"
    views_num = 95
    return HttpResponse(my_render(request, 'index.html', {'parm': views_num}))


def show_books(request):
    books = Bookinfo.objects.all()
    return render(request, 'show_books.html', {'books': books})


def detail(request, bid):
    book = Bookinfo.objects.get(id=bid)
    # figure = book.figure_set.all() # 对象查询
    figure = Figure.objects.filter(bid__id=bid)  # 模型查询
    return render(request, 'detail.html', {'book': book, 'figure': figure})


def create(request):
    b = Bookinfo()
    b.bname = '流星蝴蝶剑'
    b.pubdata = date(1990, 1, 1)
    b.save()
    # return HttpResponse('添加成功')
    return HttpResponseRedirect('/book')


def delete(request, bid):
    book = Bookinfo.objects.get(id=bid)
    book.delete()
    # return HttpResponseRedirect('/book')
    path = reverse('book:book') #动态路由
    # return redirect('/book')
    return redirect(path)

def areas(request):
    # form = NameForm
    name = forms.cleaned_data['name']
    area = District.objects.get(name=name)
    area_id = area.parent_id
    # children = District.objects.filter(Q(district__parent=area_id) & Q(district__level=area_id))
    if area.level == 1:
        parent_id = int(str(area_id)[0:2] + '0000')
        # parent_name = District.objects.get(id=parent_id)
        parent_name = area.name
        children_ids = int(str(area_id)[0:2] + '9999')
        children = District.objects.filter(Q(parent__gt=parent_id) & Q(parent__lt=children_ids) & Q(level=2))
    elif area.level == 2:
        parent_id = int(str(area_id)[0:2] + '0000')
        parent_name = District.objects.get(id=parent_id)
        children = area.district_set.all()
    return render(request, 'areas.html', {'area': area, 'parent': parent_name, 'children': children})
