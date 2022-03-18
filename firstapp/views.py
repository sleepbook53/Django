from django.shortcuts import render

# Create your views here.

#views에서는 대게 함수로 사용(전체 컨트롤 영역)
from django.http import HttpResponse

def index1(request) :
    return HttpResponse("<u>Hello...</u>")

#index2
def index2(request) :
    return HttpResponse("<u>Hi</H>")

#main
def main(request) :
    return HttpResponse("<u>Main</u>")

#Home
def home(request) :
    return HttpResponse("<u>Home</u>")

from . models import Curriculum
def insert(request) :
    #1-linux 입력
    Curriculum.objects.create(name='linux')
    #2-python 입력
    c = Curriculum(name= 'python')
    c.save()
    #3-html/css/js 입력
    Curriculum(name='payton').save()
    #4-django 입력
    Curriculum(name='django').save()
    return HttpResponse('데이터 입력 완료')

def show(rquest) :
    curriculum = Curriculum.objects.all()
    result = ''
    for c in curriculum:
        result += c.name + '<br>'
    return HttpResponse(result)

def show2(rquest) :
    curriculum = Curriculum.objects.all()
    
    return render(
        rquest, 'firstapp/show.html', {'data' : curriculum}
    )

#html 페이지에 테이블(행과 열)형태로 그려보기
def show3(rquest) :
    curriculum = Curriculum.objects.all()
    
    return render(
        rquest, 'firstapp/show2.html', {'table' : curriculum}
    )