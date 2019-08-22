# import requests
#
# headers = {
#     'Referer': 'https://www.bilibili.com/v/anime/finish/',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
# }
# data = {
#     'callback': 'jqueryCallback_bili_8346872241417846',
#     'rid': 32,
#     'type': 0,
#     'pn': 1,
#     'ps': 20,
#     'jsonp': 'jsonp',
#     '': 1566437100880,
# }
#
# r = requests.get('https://api.bilibili.com/x/web-interface/newlist?callback=jqueryCallback_bili_8346872241417846&rid=32&type=0&pn=1&ps=20&jsonp=jsonp&_=1566437100880', params=data)
#
# print(r.text)


from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://www.bilibili.com/v/anime/finish/#/')
r.html.render()

