from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request) :
    return HttpResponse("<u>2/Main</u>")

from .models import Course
def insert(request) :
    #1-데이터분석
    Course.objects.create(name='데이터 분석', cnt =30)
    #2-데이터 수집
    c = Course(name= '데이터 수집', cnt = 20)
    c.save()
    #3-웹계발입력
    Course(name='웹계발', cnt = 25).save()
    #4-인공지능
    Course(name='인공지능', cnt = 20).save()
    return HttpResponse('데이터 입력 완료')