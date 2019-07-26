import urllib.request
import re

response = urllib.request.urlopen('https://maoyan.com/board/4?offset=0')
rsp = response.read().decode('utf-8')

#用search只能匹配到第一个
result1 = re.search('<p class="name">.*?title="(.*?)"', rsp )
print(result1.group(1))

#用findall()
result2 = re.findall('<p class="name">.*?title="(.*?)"', rsp )
print(type(result2))
print(result2)
print(result for result in result2)
for result in result2:
    print(result)

