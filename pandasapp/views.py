from django.shortcuts import render
import pandas as pd

from pandasapp.df.melon.melon_df import getDf_Melon

# Create your views here.
def melon(request) :
    
    df = pd.DataFrame()
    df["mem_id"]    = ["a001", "b001", "c001"]
    df["mem_pass"]  = ["a001pwd", "b001pwd", "c001pwd"]
    df["mem_name"]  = ["홍길동", "춘향이", "길동이"]
    
    # DataFrame 데이터의 행과 열을 
    # HTML의 Table 형태로 변환하기
    context = {"df" : df.to_html()} #df.t0_html : html을 테이블 형태로 바꿔라
                                    #df : key 값
                                    #context : 변수
    
    return render(
        request, 'pandasapp/melon.html', context
    )

def melon_df(request) :
    df = getDf_Melon()
    
    #DataFrame 데이터의 행과 열을 HTML의 Table 형태로 변환
    context = {"df" : df.to_html()}
    
    return render(
        request, 'pandasapp/melon_df.html', context
    )