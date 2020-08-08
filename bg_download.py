import requests
import re
from contextlib import closing


def down_load(file_url, file_full_name):
    # 开始下载图片
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }
    with closing(requests.get(file_url, headers=headers, stream=True)) as response:
        chunk_size = 1024  # 单次请求最大值
        content_size = int(response.headers['content-length'])  # 文件总大小
        data_count = 0  # 当前已传输的大小
        with open(file_full_name, "wb") as file:
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)


def get_download_url(url):
    resp = requests.get(url)
    html = resp.text
    info = re.search('<a href="/download/\?desktop=\d*">', html)
    return "http://simpledesktops.com" + info.group(0).split("\"")[1]


def parse(pageNo):
    resp = requests.get(f'http://simpledesktops.com/browse/{pageNo}/')
    # pattern = re.compile("<a href=\"browse/desktops/.*?\">")
    # print(resp.text)
    list = re.findall("<a href=\"/browse/desktops/.*?/\">\n", resp.text)
    for str in list:
        path = str.split("\"")[1]
        path = "http://simpledesktops.com" + path
        url = get_download_url(path)
        print(url)
        down_load(url, url.split("=")[1] + ".jpg")


for page in [1, 2, 3, 4, 5]:
    parse(page)
