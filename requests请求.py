#!/usr/bin/env python
#coding=utf-8

import requests

'''
	1.使用requests
	要通过GET访问一个页面，只需要几行代码：
	'''
r = requests.get('https://www.douban.com/')#豆瓣首页
requestCode = r.status_code
print('请求状态值:',requestCode)
requestData = r.text
# print('请求 Data',requestData);
'''
	2.对于带参数的 URL,传入一个 dict 作为 params 参数
	'''
r1 = requests.get('https://www.douban.com/search',params={'q':'python','cat':'1001'})
requestsUrl = r1.url
print('请求的 url:',requestsUrl)
#requests自动检测编码，可以使用 encoding 属性来查看：	
requestsEncode = r.encoding
print('requests自动检测编码:',requestsEncode)
# 无论响应是文本还是二进制内容，我们都可以用 content 属性获得 bytes 对象
requestsBytes = r.content
# print('requests bytes 对象:',requestsBytes)

'''
	3.requests的方便在于对于特定类型的响应，例如 JSON，可以直接获取
	'''
r2 = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json') 
requestsJson = r2.json()
# print('requestsJson:',requestsJson)

'''
	4.需要传入HTTP Header时，我们传入一个dict作为headers参数：
	'''
r3 = requests.get('https://www.douban.com/',headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}) 
requestsText = r3.text
# print('requestsText:',requestsText)

'''
	5.要发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据：
	'''

r4 = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
requestsR4 = r4.text
# print('requestsR4:',requestsR4)

'''
	requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数：
	'''

# params = {'key':'value'}
# r5 = requests.post(url,json=params)#内部自动序列化 JOSN
# # 类似的，上传文件需要更复杂的编码格式，但是requests把它简化成files参数：
# upload_files = {'file':open('report.xls','rb')}
# r6 = requests.post(url,file=upload_files)


'''
	在读取文件时，注意务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度。

	把post()方法替换为put()，delete()等，就可以以PUT或DELETE方式请求资源。

	除了能轻松获取响应内容外，requests对获取HTTP响应的其他信息也非常简单。例如，获取响应头：
	'''

 
# requestsHeaders = r4.headers
# print('requestsHeaders:',requestsHeaders)

# requests对Cookie做了特殊处理，使得我们不必解析Cookie就可以轻松获取指定的Cookie：
# requestsCookies = r3.cookies['ts']
# print('requestsCookies:',requestsCookies)

'''
	要在请求中传入Cookie，只需准备一个dict传入cookies参数：
	'''
url = 'https://www.douban.com/'
# cs = {'token':'12345','status':'working'}
# r6 = requests.get(url,cookies=cs)
# print('requestsr6:',r6.content)

'''
	最后，要指定超时，传入以秒为单位的timeout参数：
	'''
# r7 =  requests.get(url,timeout=2.5)
# print('requestsr7:',r7.text)


'''
	练习一：获取请求头
'''
# rd = requests.get('https://www.douban.com/search', params={'q':'python', 'cat':'1001'})
# print(rd.status_code, rd.url)
# h = rd.headers
# print('练习一:获取请求头')
# for k, v in h.items():
#     print(k,': ', v)









