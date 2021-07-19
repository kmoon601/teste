count=0  # 클래스 밖의 변수

class Rectangle:
    count = 0  #클래스의 변수
   
    def __init__(self, fdata, sdata):
        self.fdata = fdata
        self.sdata = sdata 
        Rectangle.count += 1    

    def calcArea(self): 
        tdata = self.fdata * self.sdata
        return tdata


    @staticmethod  # 정적메서드선언
    def myStatic(data1, data2):
        pass

    @classmethod
    def myclsmethod(my):
        my.count
        my.calcArea


r= Rectangle(11,22)
result= r.calcArea()
print(result)
