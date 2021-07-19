
import pymysql
data1= (
    (13,'홍9','영업','서울'),  
    (10,'홍10','개발','부산'),
    (11,'홍11','관리','대전'),
    (12,'홍12','영업','경기'),
)
try:
    con= pymysql.connect(host='localhost', 
                     user='root',
                     password='kang2096@', 
                     db='testdb',                            
                     charset= 'utf8')      
    
    curs = con.cursor()

    
    sqlquery= ''' INSERT INTO 
                        emptb(empid,empname,emppart,empregion)
                     VALUES (%s,%s,%s,%s)    
    '''

    curs.executemany(sqlquery,data1)    # excutemany 로 여러쿼리 실행가능

   
    con.commit()    # 커밋 나옴

except Exception as ex:
    print(ex)

finally:
    con.close()