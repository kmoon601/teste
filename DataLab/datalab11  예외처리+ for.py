try:
    f2= open('test.txt', mode= 'rt', encoding= 'utf-8')     # 읽기
    for f in f2:
        print(f)
finally:
    f2.close()
# 함수중에 메서드를 사용하면 열기 후 닫기

# with 를 사용하면 열기후 닫기 자동으로 해버림
with open('test.txt', mode= 'rt', encoding= 'utf-8') as f3:
    for f in f3:
        print(f)
