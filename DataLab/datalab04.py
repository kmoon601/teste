
import pymysql 
from pymysql.err import MySQLError

connectCheck = False

try:

    con= pymysql.connect(host='localhost', 
                     user='root',
                     password='kang2096@', 
                     db='testdb',                            
                     charset= 'utf8')       

    connectCheck = True

except MySQLError as ex:   # MYSQL 전용 보험   /  보통전용보험 먼저 써줌
    error= ex
except Exception as ex:  # 종합보험    / 종합보험은 왠만하면 항상 써줌
    error = ex

if connectCheck:
    curs = con.cursor()

    sqlquery = '''SELECT empid,empname,emppart,empregion 
                  from emptb 
                  where empregion = %s'''    # 광주 대신 %s 로 바꾸기  
    curs.execute(sqlquery,('광주'))                   

    rows= curs.fetchall()

# 애초에 오류나기떄문에 finally 안쓴다??


# 출력
for row in rows:
    print(row[0],row[1],row[2],row[3])   # row['empid'], row['empname'],row['emppart']로 해도됌

