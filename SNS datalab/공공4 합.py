#공공 데이터 가져오기 (godata.go.kr)   

import urllib.request
import datetime
import json

def Get_Request_Url(url): # 크롤러를 담당하는 부분
    req = urllib.request.Request(url)   
    # https://api.odcloud.kr/api/apnmOrg/v1/list?page=1&perPage=10   
    # &serviceKey=8ztdUn%2FQXgIyDjfqE9JaKZHvISRDASfEiG038K2k6cSX2tr7Lt7NF4HTf3VN4UURQ%2B2uQfKUEXA4osCpkTB3AQ%3D%3D
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200: 
            print("[%s] Url 요청 성공 : " % datetime.datetime.now())    
            return response.read().decode('utf-8')
    except Exception as ex:
        print(ex)
        print("[%s] 오류 : %s " % datetime.datetime.now(), url)
        return None

def GetGoVSearchResult(pageValue, perPageValue): # 사전 준비 작업 및 분류   
    endPoint = "https://api.odcloud.kr/api/apnmOrg/v1/list?"
    paraData = "page=" + str(pageValue)
    paraData += "&perPage=" + str(perPageValue)
    keyValue = "&serviceKey=8ztdUn%2FQXgIyDjfqE9JaKZHvISRDASfEiG038K2k6cSX2tr7Lt7NF4HTf3VN4UURQ%2B2uQfKUEXA4osCpkTB3AQ%3D%3D"
    url = endPoint+ paraData + keyValue

    resultData = Get_Request_Url(url)

    if(resultData == None):
        return None
    else:
        return json.loads(resultData)

def GetGoVSearchResult2(pagevalue,perpagevalue):    # 여기서는 두개값만 보내면됌/  사전작업
    endPoint = 'https://api.odcloud.kr/api/15077586/v1/centers?'         # request url 에서 잘라서 가져온것들
    paraData1 = 'page=' + str(pagevalue)
    paraData2 = '&perPage=' + str(perpagevalue)
    keyvalue= '&serviceKey=8ztdUn%2FQXgIyDjfqE9JaKZHvISRDASfEiG038K2k6cSX2tr7Lt7NF4HTf3VN4UURQ%2B2uQfKUEXA4osCpkTB3AQ%3D%3D'
    url= endPoint+ paraData1+paraData2+keyvalue

    resultData= Get_Request_Url(url)

    if(resultData ==None):
        return None
    else:
        return json.loads(resultData)


def GetdataChange(data,jsonDataResult,counter):
    
    data['id'] = counter
    del data['dywk']
    del data['endTm']
    del data['hldyYn']
    del data['lunchEndTm']
    del data['lunchSttTm']
    del data["sttTm"]

    data['centerName'] = None
    data["centerType"] = None
    data["facilityName"] = None
    data["lat"] = None
    data["lng"] = None
    data["updatedAt"] = None
    

    data['address'] = data.pop('orgZipaddr')
    data['org"'] = data.pop('orgnm')
    data['phoneNumber'] = data.pop('orgTlno')
    data['zipCode '] = data.pop('orgcd')

    changeDate = datetime.datetime.strptime(data["slrYmd"], '%Y%m%d')#표시형식

    changeDateResult = changeDate.strftime('%Y-%m-%d  %H:%M:%S')
    del data['slrYmd']
    data["createdAt"] = changeDateResult
    
    jsonDataResult.append(data)

def Main():
    jsonDataResult=[]

    pageData = 1
    perPageData = 100
    jsonSearchResult = GetGoVSearchResult(pageData, perPageData)
    jsonSearchResult2 = GetGoVSearchResult2(pageData, perPageData)

    counter = jsonSearchResult2['currentCount']

    for data in jsonSearchResult['data']:
        counter+=1
        GetdataChange(data, jsonDataResult,counter)
        
        print(data)

    jsonSearchResult2['data']+= jsonDataResult
    jsonSearchResult2['currentCount']=counter

    with open('%s_GovData_%s.json' % ('병원2', '데이터2'), 'w', encoding='utf-8') as filedata:
        

        rJson = json.dumps(jsonSearchResult2,#jsonDataResult, 
                            indent=4,
                            sort_keys=True,
                            ensure_ascii=False )
        filedata.write(rJson)

    #print('파일이름 : %s_GovData_%s.json 저장완료' % ('병원2', '데이터2'))

if __name__ == '__main__':
    Main()