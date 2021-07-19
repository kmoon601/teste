import pymysql 

try:
    con= pymysql.connect(host='localhost', 
                     user='root',
                     password='kang2096@', 
                     db='testdb',                            
                     charset= 'utf8')      
    
    curs = con.cursor()

    sqlQuery= ''' DELETE FROM 
                    emptb
            
                WHERE
                    empid= %s
                  '''

    curs.execute(sqlQuery,5)

    con.commit()    # 디버깅할떄 커밋전까찌는 db에 변화없고, commit 후에 바뀜
    con.close()      # commit 후에 close 한다고 봐도됌

except Exception as ex:
    print(ex)
