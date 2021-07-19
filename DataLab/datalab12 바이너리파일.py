# 바이너리 파일 : jpeg, png 그림/ 동영상/ 음악



with open('test.jpg', 'rb') as f:  # rb = 바이너리 파일 읽기
    byte= f.read(1)
    while byte != b"":     # byte가 공백이 아닐때까지 돌려라
        print(byte)
        byte= f.read(1)     # 첫번쨰 녀석을 할당해놓는것  / 이게없으면 계속돌아가


data1= [1,2,3,4,5,6]
with open('test.bin','wb') as f:   # bin은 바이너리
    f.write(bytes(data1))


#***************************
# text로 읽어들이는것
# 이미지를 바이너리로 읽어들이는것 --0> 바이너리값 분석해서 태그값 이런거 분석해야됌