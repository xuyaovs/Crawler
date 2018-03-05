# coding:utf8
import re
import requests
import json

url = 'https://foofish.net'
response = requests.get(url)

# 状态码
print response.status_code
# 原因短语
print response.reason
# 响应首部
for name, value in response.headers.items():
    print ("%s:%s" % (name, value))
# 响应内容
print response.content

args = {"p": 4, "s": 20}
response = requests.get(url, params=args)
print response.url

# 构建请求首部 Headers
response = requests.get(url, headers={'user-agent': 'Mozilla/5.0'})

# 作为表单数据传输给服务器
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.post("http://httpbin.org/post", data=payload)

# 作为 json 格式的字符串格式传输给服务器
url = 'http://httpbin.org/post'
payload = {'some': 'data'}
response = requests.post(url, json=payload)

# content 是 byte 类型，适合直接将内容保存到文件系统或者传输到网络中
response = requests.get("https://pic1.zhimg.com/v2-2e92ebadb4a967829dcd7d05908ccab0_b.jpg")
print type(response.content)
# 另存为 test.jpg
with open("test.jpg", "wb") as f:
    f.write(response.content)

# text 是 str 类型，比如一个普通的 HTML 页面，需要对文本进一步分析时，使用 text
response = requests.get("https://foofish.net/understand-http.html")
print type(response.text)
re.compile('xxx').findall(response.text)

# 如果使用第三方开放平台或者API接口爬取数据时，返回的内容是json格式的数据时，那么可以直接使用json()方法返回一个经过json.loads()处理后的对象
response = requests.get('https://www.v2ex.com/api/topics/hot.json')
print response.json()

# 代理设置
proxies = {
  'http': 'http://10.10.1.10:3128',
  'https': 'http://10.10.1.10:1080',
}
response = requests.get('http://example.org', proxies=proxies)

# 超时设置,5秒后报错
response = requests.get("http://www.google.coma", timeout=5)

# Session
login_url = 'www.baidu.com'
home_url = 'www.baidu.com'
username = 'admin'
password = '123'
# 构建会话
session = requests.Session()
# 登录url
session.post(login_url, data={username, password})
# 登录后才能访问的url
response = session.get(home_url)
session.close()















