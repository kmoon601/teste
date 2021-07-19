import os
import sys
import urllib.request
import datetime
import time
import json
#from config import * 

client_id = 'qECWDDhbjuYcgp4lbNET'
client_secret = 'nnxmbPGXMf'

def get_request_url(url): 
    req = urllib.request.Request(url) 
    req.add_header("X-Naver-Client-Id", client_id) 
    req.add_header("X-Naver-Client-Secret", client_secret) 

    try:
        response = urllib.request.urlopen(req) 
        if response.getcode() == 200: 
            print("[%s] Url 요청 성공  " % datetime.datetime.now())    
            return response.read().decode('utf-8')
    except Exception as ex:
        print(ex)
        print("[%s] 오류 : %s " % datetime.datetime.now(), url)
        return None


def GetNaverSearchResult(searchNode, searchText, pageStart, display): 
    baseurl = "https://openapi.naver.com/v1/search/" 
    nodedata = "%s.json" % searchNode 
    parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(searchText), 
                                                        pageStart , 
                                                        display) 
    url = baseurl + nodedata + parameters 
    # 비정형(반정형) 가지고 온 초기 데이터(또는 정형일 수 있다) 
    reqDataResult = get_request_url(url)
    #reqDataResult : DataLake 저장
    if(reqDataResult == None): 
        print("Data가 없습니다.")
        return None
    else:
        return json.loads(reqDataResult)


def main(): 
    jsonDataResult = []

    sNode = 'news'
    sText = '코로나'
    dCount = 100
    # 원시 데이터 가져옴(DataLake 에서 정형 데이터를 가져옴)
    jsonSearchResult = GetNaverSearchResult(sNode, sText, 1, dCount)

    while ((jsonSearchResult != None) and (jsonSearchResult['display'] != 0)):   # 무한루프 가능성 높음
        for data in jsonSearchResult['items']:
            GetDateChange(data,jsonDataResult)


def GetDateChange(data,jsonResult):    # 데이터 정제하는 부분임 여기가      #json 파일 보면서함
    resultTitle = data['title']
    resultDesc= data['description']
    resultOrgLink = data['originallink']
    naverLink = data['link']

    changeDate= datetime.datetime.strptime(data['pubDate'],
                                                '%a %d %b %Y %H:%M:%S +0900') # 표시형식 j
    changeDateResult= changeDate.strptime('%Y-%m-%d  %H:%M:%S')      # 표시형식 이렇게 변경/ 날짜정제// (m: 월 / M: 분)

    jsonResult.append({'title': resultTitle,
                        'description': resultDesc,
                        'link': naverLink,
                        'originallink':resultOrgLink,
                        'pubDate':changeDateResult})
    return    # 더이상 할것 없으니 날 호출한함수로 돌아가기:  return 아래 코드가 있어서 실행되지않는다

    with open('%s_naver_%s.json' % (sText, sNode), 'w', encoding='utf-8') as filedata:
        rJson = json.dumps(jsonSearchResult, 
                            indent=4,
                            sort_keys=True,
                            ensure_ascii=False )
        filedata.write(rJson)

    print('%s_naver_%s.json 저장완료' % (sText, sNode))





if __name__ == '__main__':
    main()
