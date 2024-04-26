import requests
import time
# import json
url = 'https://n.hongbaoquanzi.com/addons/skaitooln/rain/status'

headers2 = {

           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309092b) XWEB/8555 Flue', 
           'token': 'da4cdc15-4b37-4221-9542-7bd4fa61b1e3', 
#		  'content-type': 'application/json', 
           'Accept-Encoding': 'gzip, deflate, br', 

           }

# data = {"time":"18"}        1开会员接口 2升级接口
t=time.localtime().tm_hour
# print(t)
while(True):
    if t<10:
        now='0'+str(t)
    else:
        now=str(t)

    print("当前时间:"+now)
    
    #签到  和打开小程序奖励  抽奖
    if(t==1 or t==2):
        #升级
        url3='https://n.hongbaoquanzi.com/addons/skaitooln/user/upgrade'
        html = requests.get(url3, headers=headers2)
        print(html.json())
        
        #使用能量
        url3='https://n.hongbaoquanzi.com/addons/skaitooln/user/makestone'
        html = requests.post(url3, headers=headers2,data={"make_power":100})
        print(html.json())
        
        #签到
        url3='https://n.hongbaoquanzi.com/addons/skaitooln/user/sign'
        html = requests.get(url3, headers=headers2)
        print(html.json())
        #打开小程序
        url4='https://n.hongbaoquanzi.com/addons/skaitooln/task/mp?appid=wx6ff53bbc82bd55b7'
        html = requests.get(url4, headers=headers2)
        print(html.json())
           
    if(t<=2):
        #抽奖
        url4='https://n.hongbaoquanzi.com/addons/skaitooln/lottery/take'
        html = requests.post(url4, headers=headers2,data={"id":2})
        print(html.json())

# 抽奖
# POST https://n.hongbaoquanzi.com/addons/skaitooln/lottery/take HTTP/1.1
# token: a20f8aa5-92aa-4b7b-a60e-85b7980584d1
# user-agent: Mozilla/5.0 (Linux; Android 13; 23049RAD8C Build/TKQ1.221114.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/34.18182)
# Content-Type: application/json
# Content-Length: 8
# Host: n.hongbaoquanzi.com
# Connection: Keep-Alive
# Accept-Encoding: gzip

# {"id":2}

# {"code":1,"msg":"OK","time":"1709180333","data":{"stone":"11905.00"}}
        
    if(t<12):
    #广告能量
        url2='https://n.hongbaoquanzi.com/addons/skaitooln/task/video'   
        # {"code":1,"msg":"OK","time":"1708938528","data":{"addpower":"10","power":105,"ad_video_num":6}}
        
        html = requests.get(url2, headers=headers2)
        print(html.json())

    html = requests.post(url, headers=headers2, data= {"time":now})
    print(html.json())
    #整点红包
    url = 'https://n.hongbaoquanzi.com/addons/skaitooln/rain/open'
    # headers = {'Host': 'n.hongbaoquanzi.com', 'Connection': 'keep-alive', 'Content-Length': '13', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309092b) XWEB/8555 Flue', 'token': '24b58be4-d234-4c84-8383-491b822a9d31', 'content-type': 'application/json', 'Accept': '*/*', 'Origin': 'https://nmqz.hongbaoquanzi.com', 'Sec-Fetch-Site': 'same-site', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://nmqz.hongbaoquanzi.com/', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9'}
    # cookies = {}
    # data = {}

    html = requests.post(url, headers=headers2,  data={"time":now})
    print(html.text)

    t+=1
    if(t==24):
        t=0
    # {"code":1,"msg":"OK","time":"1708607068","data":{"addmoney":"1.00"}}
    time.sleep(3599.8)




# POST https://n.hongbaoquanzi.com/addons/skaitooln/rain/status HTTP/1.1

# {"time":"21"}

# {"code":1,"msg":"可领取~","time":"1708607068","data":null}

# POST https://n.hongbaoquanzi.com/addons/skaitooln/rain/open HTTP/1.1


# {"time":"21"}
# {"code":1,"msg":"OK","time":"1708607068","data":{"addmoney":"1.00"}}