# 공공데이타 가져오기
import urllib.request
import datetime
import json

        # 명세확인가이드 보기

def GetRequestURL(url):
    req = urllib.request.Request(url) 
    # 인증키 확인해서 request url 가져오기
    #https://api.odcloud.kr/api/15077586/v1/centers?page=1&perPage=10&serviceKey=8ztdUn%2FQXgIyDjfqE9JaKZHvISRDASfEiG038K2k6cSX2tr7Lt7NF4HTf3VN4UURQ%2B2uQfKUEXA4osCpkTB3AQ%3D%3D
    try:
        response = urllib.request.urlopen(req) 
        if response.getcode() == 200: 
            print("[%s] Url 요청 성공 : " % datetime.datetime.now())    
            return response.read().decode('utf-8')
    except Exception as ex:
        print(ex)
        print("[%s] 오류 : %s " % datetime.datetime.now(), url)
        return None


def GetGoVSearchResult(pagevalue,perpagevalue):    # 여기서는 두개값만 보내면됌/  사전작업
    endPoint = 'https://api.odcloud.kr/api/15077586/v1/centers?'         # request url 에서 잘라서 가져온것들
    paraData1 = 'page=' + str(pagevalue)
    paraData2 = '&perPage=' + str(perpagevalue)
    keyvalue= '&serviceKey=8ztdUn%2FQXgIyDjfqE9JaKZHvISRDASfEiG038K2k6cSX2tr7Lt7NF4HTf3VN4UURQ%2B2uQfKUEXA4osCpkTB3AQ%3D%3D'

    url= endPoint+ paraData1+paraData2+keyvalue

    resultData= GetRequestURL(url)

    if(resultData ==None):
        return None
    else:
        return json.loads(resultData)

def main():
    pagedata= 5
    perpagedata=50

    jsonSearchResult= GetGoVSearchResult(pagedata,perpagedata)

    with open('%s_GovData_%s.json' % ('병원50','데이터50'),  'w', encoding='utf-8') as filedata:
        rJson = json.dumps(jsonSearchResult, 
                            indent=4,                    # json 할떄는 dump 해주야함
                            sort_keys=True,
                            ensure_ascii=False )
        filedata.write(rJson)

    #print('파일이름 : %s_GovData_%s.json 저장완료' % ('병원', '데이터'))
if __name__ == '__main__':
    main()


