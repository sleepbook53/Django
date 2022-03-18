# - 웹 브라우저를 조작..
# - 웹 브라우저에 보이는 HTML 태그속에서 
#   텍스트 데이터를 분리해서 가지고오는 라이브러리
# selenium 설치명령 : conda install -c conda-forge selenium
# conda install로 설치가 안되면 : pip install selenium

import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By

# DeprecationWarning: executable_path has been deprecated 해결을 위해
# 자체 pc에서 사용하는 웹브라우저의 크롬드라이버를 직접 사용..
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 자체 PC의 크롬드라이버를 조회하여 리턴받아서 사용하기.
def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

def getDf_Melon() :
    
    # 2. selenium 방식

    # 자체 PC의 크롬드라이버를 조회하여 리턴받아서 사용하기.
    driver = set_chrome_driver()
    #driver = webdriver.Chrome("c:/ChromeDriver_exe/chrome_99_driver.exe")

    url = "http://www.melon.com/chart/index.htm"
    driver.get(url)

    #html = driver.page_source

    # 이하 부분이 BeautifulSoup 방식 적용
    # select() 함수를 이용하여 태그 정보 가지고 옵니다.
    #soup = BeautifulSoup(html, "html.parser")

    # selenium 방식 시작...
    # find_elements_by_css_selector() 함수 사용

    # 순위 10 뽑기
    #songs = driver.find_elements_by_css_selector("tr")[1 : 11]
    songs = driver.find_elements(By.CSS_SELECTOR, "tr")[1 : 11]

    df = pd.DataFrame()

    for i in range(0, len(songs)) :

        df_temp = pd.DataFrame()

        # find_elements(BY.CSS_SELECTOR, 'ul.popular_order li.list')
        # 노래 제목만 가지고 오기..
        #title = songs[i].find_elements_by_css_selector("div.ellipsis.rank01 > span > a")[0].text
        title = songs[i].find_elements(By.CSS_SELECTOR, "div.ellipsis.rank01 > span > a")[0].text

        # 가수 이름만 가지고 오기...
        #singer = songs[i].find_elements_by_css_selector("div.ellipsis.rank02 > a")[0].text
        singer = songs[i].find_elements(By.CSS_SELECTOR, "div.ellipsis.rank02 > a")[0].text

        # 조회
        #print("순위[{}], 제목[{}], 가수[{}]".format((i+1), title, singer))

        df_temp["노래 순위"] = [(i+1)]
        df_temp["노래 제목"] = [title]
        df_temp["가수 이름"] = [singer]

        df = df.append(df_temp, ignore_index=False)

    return df