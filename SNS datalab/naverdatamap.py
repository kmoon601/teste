import urllib.request
import datetime
import json
import folium

client_id = "xa25ja6nca"
client_secret = "1a3NIZFJLWWpgOnc1tgDJMFYTTKQLzVsXTH7T4X2"

def get_request_url(url): # 데이터 요청하여 가져오기 - 크럴러 작업
    req = urllib.request.Request(url) #검색 URL 경로 지정
    req.add_header("X-NCP-APIGW-API-KEY-ID", client_id) # 경로 접근하기 위한 아이디 - naver에서 발급
    req.add_header("X-NCP-APIGW-API-KEY", client_secret) #경로 접근하기 위한 비밀번호 - naver에서 발급

    try:
        response = urllib.request.urlopen(req) # URL을 통해 데이터 요청해서 결과 받음
        if response.getcode() == 200: # 200 코드 번호면 성공 400/500 은 Naver 문서에서 확인
            print("[%s] Url 요청 성공 : " % datetime.datetime.now())    
            return response.read().decode('utf-8')
    except Exception as ex:
        print(ex)
        print("[%s] 오류 : %s " % datetime.datetime.now(), url)
        return None

def GetGeoLocationData(addr):
    baseUrl = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"
    paraData = "?query=%s" % urllib.parse.quote(addr)
    resulturl = baseUrl + paraData

    resultData = get_request_url(resulturl)

    if(resultData == None):
        return None
    else:
        # Naver 데이터 정제
        xdata = 0
        ydata = 1

    return [xdata, ydata]

def Main():
    addrData = GetGeoLocationData('필동로1길 30')
    tip = '병원'
    map_data = folium.Map(location=[addrData], zoom_start=15)
    map_data = folium.Marker(addrData, popup='확인', tooltip=tip).add_to(map_data)
    map_data.save(r'c:\temp\navermap.html')
    # 다른 방법 Naver API 를 이용한 Naver Map 사용(Static Map)

if __name__ == '__main__':
    Main()
