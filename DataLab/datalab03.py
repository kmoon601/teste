
import pymysql

con= pymysql.connect(host='localhost', 
                     user='root',
                     password='kang2096@', 
                     db='testdb',                            
                     charset= 'utf8')       # 오류나면 여기


try:
    curs = con.cursor()

    sqlquery = '''SELECT empid,empname,emppart,empregion 
                  from emptb 
                  where empregion = %s'''    # 광주 대신 %s 로 바꾸기  
    curs.execute(sqlquery,('광주'))                   

    rows= curs.fetchall()

except Exception as ex:  # 종합보험
    error = ex

finally:
    con.close()

# 출력
for row in rows:
    print(row[0],row[1],row[2],row[3])   # row['empid'], row['empname'],row['emppart']로 해도됌

