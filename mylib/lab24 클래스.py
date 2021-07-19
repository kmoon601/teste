# 객체지향 프로그래밍
# 객체는 클래스를 사용하기위한 변수
# 클래스는 함수 모음
# 
# 1.class 이름 -> 2.메서드 및 변수정의 -> 3.클래스 내부에 데이터 표현하는것( 속성)


count=0  # 클래스 밖의 변수

class Rectangle:
    count = 0  #클래스의 변수

    #초기값 사용한다 (fdata, sdata)
    def __init__(self, fdata, sdata):
        self.fdata = fdata
        self.sdata = sdata 
        Rectangle.count += 1    # 클래스밖의 변수와 구분하기위해 REctanle.count로 씀


# 인스턴스 메서드 : 기본이 되는 메서드    # 인스턴스 메서드는  매개변수로 self를 가짐     # self : 첫번쨰 파라미터(매개변수)에 객체 자신을 의미
    def calcArea(self): 
        tdata = self.fdata * self.sdata
        return tdata

            # 파이썬은 기본적으로 모두 public 선언, 누구나 메서드에 접근가능
            # 근데 객체지향언어는 가끔 다른사람이 접근못하게 하려면-> 메서드 이름앞에 __ 붙이면 해당 클래스 안에서만 사용가능
                                                                                 # ex) def__calcArea()   

# 정적메서드  = self 안함, 인스턴스없이 직접 클래스의 메서드를 가져다쓸수잇음
    @staticmethod  # 정적메서드선언
    def myStatic(data1, data2):
        pass

# 클래스메서드  
    @classmethod
    def myclsmethod(my):
        my.count
        my.calcArea

# 스페셜메서드(Magic Method):  객체를 사용하면 다 사용햇다고 신고,  신고할때 소멸  ex) __del__ / __add__  / __sub__ / __cmp__ / __str__


# 클래스사용방법 :  인스턴스 사용
# 변수명= 클래스이름() : 클래스 호출할때 초기값이 있으면 괄호안에 값 넣어줌
# 객체는 클래스의 변수( 인스턴스의 결과물)  : r

r= Rectangle(11,22)
result= r.calcArea()
print(result)

