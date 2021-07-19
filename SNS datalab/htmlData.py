# pip install beautifulsoup4 해줫음

import urllib.request
from bs4 import BeautifulSoup     # bequtifulsoup3= 파이선2 지원이라서  bs4(버전4)꼭 써주야함


htmlDocu= urllib.request.urlopen('https://www.ncloud.com/product/applicationService/maps')
result = BeautifulSoup(htmlDocu, 'html.parser')

print(result.prettify())

