def op(data,data2):
    return data+data2

result = op(100,200) # 2개 매개변수(파라미터)값 받음
###########################################################################3333


def op2(data,data2,data3):
    result=0

    if data3 == '+':
        result = data+data2
    elif data3 == '-':
        result = data-data2
    elif data3 == '*':
        result = data*data2
    elif data3 == '/':
        result = data/data2
    
    return result

result2 = op2(100,200,'-')
##########################################################################################333
def myfun(name,age):
    myname= name+"님"                          
    myage = age+'20'
    return myname,myage 

result3, result4 = myfun('홍길동','20')

temp=0



