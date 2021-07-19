import oauth2    # oauth 2.0 버전 써야댐
import json

# 인증절차
mydata= oauth2.consumer("key",'pw')  #트위터에서받은 키, secret
passcard = oauth2.Token(key='key',secret= 'pw')
clientResult = oauth2.client(mydata,passcard)


