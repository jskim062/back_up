from flask import Flask
app = Flask (__name__)
 
import time

# -*- coding: utf-8 -*-
from urllib.request import urlopen, Request
import urllib
import bs4


#local_time = "%04d년%02d월%02d일 %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
'''
location = '수내동'
enc_location = urllib.parse.quote(location + '+날씨')

url = 'https://search.naver.com/search.naver?ie=utf8&query='+ enc_location

req = Request(url)
page = urlopen(req)
html = page.read()
soup = bs4.BeautifulSoup(html,'html.parser')
#print()
'''
@app.route('/')
def hello_world():
    #return 'Hello, World!'
    while True:
        now = time.localtime()
        local_time = "%04d년%02d월%02d일 %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour - 3, now.tm_min, now.tm_sec)

        location = '수내동'
        enc_location = urllib.parse.quote(location + '+날씨')

        url = 'https://search.naver.com/search.naver?ie=utf8&query='+ enc_location

        req = Request(url)
        page = urlopen(req)
        html = page.read()
        soup = bs4.BeautifulSoup(html,'html.parser')
        #print()

        #print(local_time)
        return '<h1>현재 ' + location + ' 날씨는 ' + soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text + '도 입니다.' +  ' 현재 시각은' + local_time + '입니다' + '<h1>'
        #time.sleep(0.5)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)

