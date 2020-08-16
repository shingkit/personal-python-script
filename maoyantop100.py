import requests
import re


file = open('a.html')
html = file.read()
print(html)
pattern = re.compile("<dd>.*?board-index.*?>(.*?)</i>.*?<a.*?title=\"(.*?)\".*?<p class=\"star\">(.*?)</p>", re.S)
list = re.findall(pattern, string=html)
## 使用()包裹正则，findall获取到的就是括号里面的数据，就不需要再处理
for str in list:
    print(str[0] + ":" + str[1] + ":" + str[2].strip()[3:])

