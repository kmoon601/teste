# Insert 데이터를 저장(한줄만= 행 단위로 저장 = row)

# 구조 틀

#  import pymysql

#  try:

#  except Exception as ex:

#  finally:

import pymysql

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

    curs.execute(sqlquery, (7,'홍7','관리', '수업'))
    curs.execute(sqlquery, (8,'홍8','관리', '수원'))
   
    con.commit()    # 커밋 나옴

except Exception as ex:
    print(ex)

finally:
    con.close()