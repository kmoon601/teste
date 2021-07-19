# CSV :  콤마 기준으로 

import csv
# 파일 생성,쓰기
f= open('test.csv', 'w',encoding='utf-8', newline='')       # csv 파일만들어주는거임  # csv는 w,r 만쓰면됌 t/b 노노
csvw = csv.writer(f)
csvw.writerow([1,'홍길동','개발','서울'])
csvw.writerow([21,'홍길2동','개2발','서2울'])
f.close()

# 생성한 파일 읽기
f= open('test.csv', 'r',encoding='utf-8')
csvr= csv.reader(f)  # 읽기완료
for data in csvr:     # 결과값 출력하려면
    print(data)
f.close()


# tsv 파일  : 탭기준으로 데이터저장
f= open('test.tsv', 'r',encoding='utf-8')
tsvr= csv.reader(f, delimiter= '\t')  #  tsv파일은 csv.reader로 그대로 읽고  delimiter 추가
for data in csvr:   
    print(data)
f.close()