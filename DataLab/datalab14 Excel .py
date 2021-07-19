# 엑셀은 자체적으로 처리불가, pip install openpyxl 해주야 됌

import openpyxl

exfile = openpyxl.load_workbook(r'c:\lab\datalab\mydata.xlsx')
exsheet = exfile.active  # 현재활성화되고 있는 시트 가져옴

# 특정시트 가져올경우 코드
# exsheet = exfile.get_sheet_by_name('시트이름')

for data in exsheet.rows:
    indexd = data[0].row   # 행인덱스 row
    name= data[1].value     # 값 가져옴 valule
    part= data[2].value
    region= data[3].value

    print(indexd,name,part,region)

exfile.save(r'c:\lab\datalab\mydata.xlsx')    # 저장 안해줘도되는듯??

exfile.close()   # 항상 닫기 마지막엔