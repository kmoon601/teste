import os
import sys
import urllib.request           # 여기까찌 naver 예제코드 

import datetime
import time
import json
from config import *

client_id = "qECWDDhbjuYcgp4lbNET"
client_secret = "nmxmbPGXMf"


def get_request_url(url):              # 데이터 요청해서 가져오기
    req = urllib.request.Request(url)  # 검색할 url 경로지정
    req.add_header("X-Naver-Client-Id", client_id)    # 경로 접근하기위한 아이디   - naver에서 발급한거
    req.add_header("X-Naver-Client-Secret", client_secret)    # 경로 접근하기위한 비밀번호-  naver에서 발급한거

    try:
        response = urllib.request.urlopen(req)         # URL을 통해 데이터 요청해서 결과받음
        if response.getcode() == 200:            # 200 이면 정상
            print("[%s] Url 요청성공:" % datetime.datetime.now())
            return response.read().decode('utf-8')       # 결과값 받는거잉

    except Exception as ex:
        print( "[%s] Url 오류: %s" % datetime.datetime.now(), url )
        return None       # 에러낫으니까 돌려줄게 없다



baseurl=  "https://openapi.naver.com/v1/search/"      # naver에서 호출에 경로명잇는거 가져온거임  ,  필수로 지정한 url
nodedata= '%s.json' % "news"                        # news를 json 파일로 가져와라
parameters= "?query= %s & start=%s & display=%s" % (urllib.parse.quote("코로나"), 1,  100)   # 경로 완성/  검색할단어(코로나) 1에서 start, 100개 가져옴 
                                                      # ?query                ,start, display


url= baseurl+ nodedata+ parameters               # 모든것 합쳐서 url 경로명 완성
reqDataResult= get_request_url(url)       #  가져오기위해서 URL 완성  /  함수호출

if(reqDataResult == None):
    print('data가 없습니다.')
else:
    print(json.loads(reqDataResult))               # json 형식으로 화면에 띄어줌


