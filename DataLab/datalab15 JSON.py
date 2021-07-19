# JSON : 자바스크립트 방식으로 데이터 저장하면서 확장성잇게 저장하는 방식
# 웹에서 많이사용 / key-value pair 형식

import json

empdata= {
    'id': 1,
    'name': '홍길동',
    'part': [
        {'data1' : '2021-07-13', '서울': '010-5412-21421'}
    ]
}

# dumps 기능 사용함

jsonstring= json.dumps(empdata, ensure_ascii= False)
print(jsonstring)

jsonstring2= json.dumps(empdata, indent=4, ensure_ascii= False)    # ensure_ascii 쓰면 한글 안꺠찜
print(jsonstring2)

jsonstring3= json.dumps(empdata, indent=2)
print(jsonstring3)

tmep=0
