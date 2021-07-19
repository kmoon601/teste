# join(), split(), partition(), format()

data1= "".join(['이름:','홍길동', '나이:','20'])
data2= ','.join(['이름', '홍길동',' 나이:', '2000'])
data3= '-'.join(['010','1234','5331'])

# split ( 리스트로)
data4= '010-4-52352'.split('-')

# partition  ( 튜플로자름)
data5,_,data6= 'seoul-jeju-log'.partition('-')

# format
data7= "직원이름: {0} / 부서명:{1}/ 직급:{2}".format("홍길동","개발","프로")
data8= "이름:{name}, 나이: {age}".format(name="기동", age=20)

# 나중에 많이쓸수잇음 
data9= (100,200)
data10= " X: {x[0]} /  Y:{x[1]}".format(x=data9)


temp=0
