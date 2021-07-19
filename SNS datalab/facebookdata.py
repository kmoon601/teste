import urllib.request
import json

if __name__ =='__main__':
    pageName=''
    facebook_id = ''   # 페이습북에서 개발자등록 후 발행받은 access key
    facebook_pw = ''   

    accessCard= facebook_id + '' + facebook_pw

    baseurl = 'https://graph.face.com/버전/'
    node= pageName
    paraData = ' /?access_token=%s' %accessCard

    urlResult = baseurl + node+ paraData

    reqResult= urllib.request.Request(urlResult)

    try:
        response = urllib.request.urlopne(urlResult)
        if( response.getcode() == 200 ):
            data = json.loads(response.read().decode('utf-8'))
    except Exception as ex:
        print(ex)
