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
                    empregion= '서울'
                  '''

    curs.execute(sqlQuery)

    con.commit()
    con.close()      # commit 후에 close 한다고 봐도됌

except Exception as ex:
    print(ex)
