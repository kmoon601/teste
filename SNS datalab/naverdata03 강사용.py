import urllib.request
import datetime
import json

client_id = "CQCsnDZ8wiijjXAq2zNw"
client_secret = "gt3P6SxFnu"

def get_request_url(url): # 데이터 요청하여 가져오기 - 크럴러 작업
    req = urllib.request.Request(url) 
    req.add_header("X-Naver-Client-Id", client_id) 
    req.add_header("X-Naver-Client-Secret", client_secret) 

    try:
        response = urllib.request.urlopen(req) 
        if response.getcode() == 200: 
            print("[%s] Url 요청 성공 : " % datetime.datetime.now())    
            return response.read().decode('utf-8')
    except Exception as ex:
        print(ex)
        print("[%s] 오류 : %s " % datetime.datetime.now(), url)
        return None


#크롤러로 데이터 가져오기 전 분류 / 인증 절차 등 사전 준비 작업
def GetNaverSearchResult(searchNode, searchText, pageStart, display): 
    baseurl = "https://openapi.naver.com/v1/search/" 
    nodedata = "%s.json" % searchNode 
    parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(searchText), 
                                                        pageStart , 
                                                        display) 
    url = baseurl + nodedata + parameters 

    reqDataResult = get_request_url(url) 
    #reqDataResult : DataLake 저장
    if(reqDataResult == None): 
        print("Data가 없습니다.")
        return None
    else:
        return json.loads(reqDataResult) 

def GetDateChange(data, jsonResult):             # 정제함수
    resultTitle = data['title']         
    resultDesc = data['description']
    resultOrgLink = data['originallink']
    naverLink = data['link']

    changeDate = datetime.datetime.strptime(data['pubDate'], 
                            '%a, %d %b %Y %H:%M:%S +0900')#표시형식
    changeDateResult = changeDate.strftime('%Y-%m-%d  %H:%M:%S') #기사들 날짜형식 변경하는거임 : 년-월-일 시:분:초

    jsonResult.append({ 'title':resultTitle, 
                        'description': resultDesc,
                        'link': naverLink,
                        'originallink': resultOrgLink,
                        'pubDate': changeDateResult})

    return 

def main():       
    jsonDataResult = []      # 리스트는 업데이트됨  함수옮길떄
    sNode = 'news'              # string은 업데이트안됨  함수옮길떄
    sText = '코로나'
    dCount = 100
    # 원시 데이터 가져옴(DataLake 에서 정형 데이터를 가져옴)
    jsonSearchResult = GetNaverSearchResult(sNode, sText, 1, dCount) # 결과 확인 하는 함수 호출

   # while ((jsonSearchResult != None) and (jsonSearchResult['display'] != 0)): 
    for data in jsonSearchResult['items']:
        GetDateChange(data, jsonDataResult)            # 데이터 하나씪 가져오면서 정제함수로 이동

    with open('%s_naver_%s.json' % (sText, sNode), 'w', encoding='utf-8') as filedata:
        rJson = json.dumps(jsonDataResult, 
                            indent=4,                    # json 할떄는 dump 해주야함
                            sort_keys=True,
                            ensure_ascii=False )
        filedata.write(rJson)

    print('%s_naver_%s.json 저장완료' % (sText, sNode))

if __name__ == '__main__':
    main()

  


    # 영화 가져와서 평점 낮은거 이런거도볼수있다
    # 블로그가져오거나

