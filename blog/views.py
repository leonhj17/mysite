# _*_ encoding:utf-8 _*_

from django.shortcuts import render
from django.http import HttpResponse

from .models import PersonalInfo
# Create your views here.
def blogtest(request):

    return  render(request,'blog/blogtest.html',{'content':'this is a test'})
    # return HttpResponse('haha')

def get_form(request):
    p=PersonalInfo()
    p.name = request.POST['name']
    p.sex = request.POST['sex']
    p.save()

    print p.name
    print p.sex

    return HttpResponse(u'提交个人信息')
