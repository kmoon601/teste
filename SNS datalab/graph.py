from matplotlib import font_manager 
import matplotlib.pyplot as plt

# 한글지원 코드, 잘안함
# fontlocation = "C:\Windows\Fonts\ITCBLKAD"
# fontname = font_manager.fontproperties(fname=fontlocation).get_name()
# matplotlib.rc('font',family=fontname)


plt.plot([1,2,3,4,5],[1,2,3,4,5],'ro',color='b')   # ro는 점그래ㅡㅍ
plt.xlabel('x축')
plt.ylabel('y축')

plt.axis([0,10,0,20])   # 표시범위: x축범위 0~10  / y축 범위 0~20
plt.show()
