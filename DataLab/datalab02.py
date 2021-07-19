
import pymysql

con= pymysql.connect(host='localhost', 
                     user='root',
                     password='kang2096@', 
                     db='testdb',                            
                     charset= 'utf8')       # 오류나면 여기

try:
    curs = con.cursor()

    sqlquery = "SELECT * FROM emptb"        # 오류 대부분
    curs.execute(sqlquery)                   # 오류나면  여기2

    rows= curs.fetchone()
except:
    error = '오류'
finally:
    con.close()

# 활용 : 튜플 저장한다.
print(rows)

##
'''total=0
for i in range(11):
    total = total+1

print(total)'''
