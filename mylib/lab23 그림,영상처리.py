# 그림, 동영상, 음악 처리

# 비트,워드 ,바이트, 킬로바이트 ,메가바이트, 기가바이트 
# 바이트단위로 처리하는 방법

data1= b"HELLoworld"       # 실제 데이터를 ASCII 코드로 변환
for d in data1:
    print(d)

#data2= data1.encode()   #오류 : data1이 이미 바이트로 처리되어서

data2= "helloworld"
data3= data2.encode()
print(data3)
data4= data3.decode()
print(data4)

print("----------------------")


data5= "안녕".encode("UTF-8")  # 유니코드로
print(data5)
data6= data5.decode("UTF-8")
print(data6)
