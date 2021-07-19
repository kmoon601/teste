data2=999

def myfunction():# 파라미터없고 리턴없음
    data1 = 1

def myfunction3(data): # 함수 호출할때 초기값을 전달할때사용
    temp1= data   # 파라미터/ 매개변수 통해서 함수에 값 전달

                                  # **중단점 찍은거만 디버깅 돌아감( 함수3은 안돌아갓)/안 볼거면 안찎어도됌

def myfunction4(data):  # 파라미터 , 리턴잇음
    returndata = data + '님'
    return returndata

def myfunction5(): #  리턴잇음
    returndata=20
    return returndata


                    # 함수는 4가지 형식

myfunction()
myfunction3('홍길동')   # 함수 호출할때 초기값 **전달**    
  
strdata= ' 안태일'
myfunction3(strdata)
name= myfunction4(strdata)
age= myfunction5()

temp=0

