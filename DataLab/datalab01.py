# python DB API :ORM (Object Relational Mapping)'
#
#  Mysql 사용할떄는 pip 설치
# Pymysql 모듈을 import / connect()/ cursor() / execute() (insert/d/u/s)
# fetchall(), fetchone(), fetchmany() 데이터를 가져옴
# Python 에서 자료구조에 저장후 처리
# 그 전에  commit()함
# 마지막에 close()로 끝


# import- connet- cursor - execute - fetch - commit - close

import pymysql

con= pymysql.connect(host='', 
                     user='',
                     password='', 
                     db='', 
                     charset= '')

curs = con.cursor()

sqlquery = "명령어" # SQL 명령어
curs.execute()  # 괄호안에 구문 or 변수 넣어ㅜ주


rows= curs.fetchall()

con.close()

print(rows)

