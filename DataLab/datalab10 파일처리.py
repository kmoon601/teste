#파일처리 : 1. 텍스트파일  2. CSV  3. 엑셀   4. JSON

# READ, WIRTE            Readline   Writeline

# f1= open(파일이름, 모드=읽기/쓰기 선택, 인코딩방식)
f1= open('test.txt', mode= 'wt', encoding= 'utf-8' )    # 쓰기

f1.write('helloworld\n')
f1.write('다음은?')
f1.close()

#모드= r 읽기 /  w,x 쓰기 / a 추가 / + 수정: t(텍스트파일), b(바이너리파일)
                # w는 파일이 있으면 내용 삭제하고 새로시작
                # x는 파일이 있으면 오류
  


f2= open('test.txt', mode= 'rt', encoding= 'utf-8')     # 읽기

data1= f2.readline()   # 한줄씩 가져옴  -> helloworld만 가져옴
data2= f2.read()        # 다가져옴  -> helloworld 다음은? 까지 다가져옴
print(data1)
print(data2)