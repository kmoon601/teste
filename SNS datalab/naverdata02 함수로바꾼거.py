# naver에서 데이터 긁어와서 정제해서 출력날리기 (ETL) 

import os
import sys
import urllib.request           # 여기까찌 naver 예제코드 
import datetime
import time
import json
#from config import *

client_id = "qECWDDhbjuYcgp4lbNET"
client_secret = "nmxmbPGXMf"


### 값가져오는함수/ 크롤러함수
def get_request_url(url):              # 데이터 요청해서 가져오기  /  
    req = urllib.request.Request(url)  # 검색할 url 경로지정
    req.add_header("X-Naver-Client-Id", client_id)    # 경로 접근하기위한 아이디   - naver에서 발급한거 ( 헤더 인증)
    req.add_header("X-Naver-Client-Secret", client_secret)    # 경로 접근하기위한 비밀번호-  naver에서 발급한거

    try:
        response = urllib.request.urlopen(req)         # URL을 통해 데이터 요청해서 결과받음
        if response.getcode() == 200:            # 200 이면 정상
            return response.read().decode('utf-8')       # 결과값 받는거잉

    except Exception as ex:
        return None       # 에러낫으니까 돌려줄게 없다



### url 완성용 함수/ 크롤러로 데이터 가져오기 전 분류, 인증절차 등 사전준비 작업 함수
def GetNaverSearchResult(searchNode,searchText,pageStart,display):             
    baseurl=  "https://openapi.naver.com/v1/search/"      # naver에서 호출에 경로명잇는거 가져온거임  ,  필수로 지정한 url
    nodedata= '%s.json' % searchNode                     
    parameters= "?query= %s and start=%s and display=%s" % (urllib.parse.quote(searchText), pageStart, display)   # 경로 완성/  검색할단어(코로나) 1에서 start, 100개 가져옴 
                                                       
    url= baseurl+ nodedata+ parameters               # 모든것 합쳐서 url 경로명 완성

    ###비정형(반정형)으로 가지고 온 초기 데이터( 정형일수도잇음)
    reqDataResult= get_request_url(url)       #  가져오기위해서 URL 완성  /  함수호출
    ## reqDateResult : DataLake에 저장
    if(reqDataResult == None):
        print('data가 없습니다.')
        return None
    else:
        print(json.loads(reqDataResult))               # 데이터를 json 형식으로 화면에 띄어줌

def main():
    jsonDataResult= []    
    sNode='news'   # news, blog, 등등 선택
    sText=' 코로나'
    dCount= 100

### 여기까지만 하면 원시 데이터 가져옴( DATALAKE에서 정형데이터를 가져옴)
    jsonSearchResult= GetNaverSearchResult(sNode,sText,1,dCount)             # 결과확인 하는 함수 호출


    # while ( (jsonSearchResult != None) and (jsonSearchResult['display'] != 0) ):      # 정제작업하는 부분임 여기가
        #pass


    with open('%s_naver_%s.json' %(sText, sNode), 'w', encoding='utf-8') as filedata:
        rJson = json.dump(jsonSearchResult, # jsonDataResult 
                                indent=4,
                                sort_key= True,
                                ensure_ascii=False )
        filedata.write(rJson)

    print('%s_naver_%s.json 저장완료' %(sText, sNode))

if __name__ == '__main__':      
    main()           # 시작을 main 함수를 실행하겟다
    #GetNaverSearchResult()    # 시작을  이 함수를 실행하겟다




    # __name__ : 내장변수, 글로벌변수 - 파이썬에서 정한 이미있는 변수
    # naverdata.py 일 경우 __name__ = naverdata ( 파일이름이라고 보면됌)
    # 이 파일 안에서 함수를 실행 