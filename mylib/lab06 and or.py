data1 = 100
data2 = 200

result5 = data1 & data2
result6 = data1 | data2
result7 = data1
# and or 할떄 
# 256 128 64 32 16 8 4 2 1
# 200일떄 128, 64, 8 에서 1
# 100일떄는 64,32, 4 에서 1
# 1인거 다 더하면 됌

result8 = False & False
result9 = False & data1
result10 = False | data1


temp=0