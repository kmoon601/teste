# folium

import folium

tip='확인'

map_data= folium.Map(location = [37.1515,127.51515], zoom_start=20)    # 위도 경도 입력
map_data= folium.Marker([37.1515,127.51515],popup='check', tooltip=tip).add_to(map_data)  # 지도에 갖다대면 툴팁에 'chech'라고 뜬다
map_data.save(r'C:\LAB\map1.html')   # html 문서로저장