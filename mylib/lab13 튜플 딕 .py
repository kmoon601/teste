# 리스트, 튜플, 딕셔너리= 자료구조 : 컬렉션에서 제공

list=[1,2,3,4,5,'이름']
tuple=(4234,52,6,5,4234,'나이')        # 읽기전용
dict={1:'이름', 2:'나이', '우편':1111}  

data= tuple[0]
try:
    tempdata= list.count(1) # 1 개수찾아줌, 빈괄호면 except로 감
    count_value=tuple.count()

except:
    tempdate = "예외발생"  # 예외가발생할떄 종합보험, 전용보험
finally:
    temp # 정상일때 무조건 실행되어야 하는 코드/ 
        # 넣어노면 비정상일떄도 실행됨/ 필요없으면 넣지마라
data2= dict[1]


temp=0