import time
import base64
import random
import requests
import execjs
import json
import queue
import threading
import re
from urllib.parse import quote
import os
import logging
import colorlog
from datetime import datetime

logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    '%(log_color)s%(levelname)s - %(message)s',
    log_colors={
        'DEBUG': 'white',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    }
))
logger.addHandler(handler)
logger.addHandler(handler)

MY_FLAG = '骆驼'

logging.getLogger('urllib3').setLevel(logging.WARNING)
logging.getLogger('requests').setLevel(logging.WARNING)

# ack='AKID1868a7a1447eb9e2052ddc3f39fb8d2f'
# secuid='MS4wLjABAAAAnYuCe2VNwFdRbwov14wgRCU0wcJv6a44I59NKEH2N7c'
# ck='ttwid=1%7CrHWkZ4Xdr9UADCirUzYhzOxjYTv1Qa0T9PCBo_MOpro%7C1698838181%7C535dcb6d1b1dd6fe4b56e7524540e89d6bb04ffe65d53373b854a5953c4cb8a4; dy_swidth=1280; dy_sheight=720; passport_csrf_token=177f781c79dec693797e09498ca8552b; passport_csrf_token_default=177f781c79dec693797e09498ca8552b; bd_ticket_guard_client_web_domain=2; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%2C%22isForcePopClose%22%3A1%7D; publish_badge_show_info=%220%2C0%2C0%2C1705324238722%22; _bd_ticket_crypt_doamin=2; __security_server_data_status=1; my_rd=2; pwa2=%220%7C0%7C3%7C1%22; store-region-src=uid; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.5%7D; download_guide=%223%2F20240115%2F1%22; s_v_web_id=verify_lrgalaxq_IKWR3ocs_Edh7_41No_B1TS_kCFJX79NWLLC; passport_assist_user=CjzqMhZfZfiRFJw7KprII7YFWtn4aiuN7302zKuqPm5xKBMCsz3MzJS1M5L-Z_dQRdIamf2947LFQXIhr6YaSgo8FzKT_ZFAv6DrstQpzlyZ27mJtL71wbx5UVZsknHih_aetv72Eq1uLrVQNGWgr3vXjECsKe8IRhnKgbKREKboxg0Yia_WVCABIgED9ntf_A%3D%3D; n_mh=1491Fb82VTDROVhtASfL5pUV0NFuk8gCo5Jwq-D80t4; sso_auth_status=e331106a41b1e1f2cf6e436308724302%2Cb359542358136a18d1b625f940094783; sso_auth_status_ss=e331106a41b1e1f2cf6e436308724302%2Cb359542358136a18d1b625f940094783; sso_uid_tt=257e44d81ea01e7d946988f55ccf2a10; sso_uid_tt_ss=257e44d81ea01e7d946988f55ccf2a10; toutiao_sso_user=d1b9e0514783025e464310e680f19da6; toutiao_sso_user_ss=d1b9e0514783025e464310e680f19da6; sid_ucp_sso_v1=1.0.0-KDBmY2ZjY2FlNDRlNzhmYWI2NmYzYzhkYjQ0YjI5YjA3ZTVjOTk5ODUKHQiy-aKKvQIQmtuZrQYY7zEgDDDcvtLSBTgCQPEHGgJobCIgZDFiOWUwNTE0NzgzMDI1ZTQ2NDMxMGU2ODBmMTlkYTY; ssid_ucp_sso_v1=1.0.0-KDBmY2ZjY2FlNDRlNzhmYWI2NmYzYzhkYjQ0YjI5YjA3ZTVjOTk5ODUKHQiy-aKKvQIQmtuZrQYY7zEgDDDcvtLSBTgCQPEHGgJobCIgZDFiOWUwNTE0NzgzMDI1ZTQ2NDMxMGU2ODBmMTlkYTY; passport_auth_status=24f1fb8c09781846e8ee07c7f2459ba7%2Ca9218f04f71a6430457f1d7d05491d9e; passport_auth_status_ss=24f1fb8c09781846e8ee07c7f2459ba7%2Ca9218f04f71a6430457f1d7d05491d9e; uid_tt=2b63d8f44e376da71559ba25f283fed6; uid_tt_ss=2b63d8f44e376da71559ba25f283fed6; sid_tt=1d71bc60f0b36053896895cd3c9deb0e; sessionid=1d71bc60f0b36053896895cd3c9deb0e; sessionid_ss=1d71bc60f0b36053896895cd3c9deb0e; LOGIN_STATUS=1; _bd_ticket_crypt_cookie=f6d7d97dbf5319b96fbceff4857aaf5e; store-region=cn-gd; sid_guard=1d71bc60f0b36053896895cd3c9deb0e%7C1705405865%7C5183988%7CSat%2C+16-Mar-2024+11%3A50%3A53+GMT; sid_ucp_v1=1.0.0-KGJjMDE3ZWViNDIwMjljYjM5N2JiNmI0MGYyMDljMzFmYTE2NzE2NTYKGQiy-aKKvQIQqduZrQYY7zEgDDgCQPEHSAQaAmxxIiAxZDcxYmM2MGYwYjM2MDUzODk2ODk1Y2QzYzlkZWIwZQ; ssid_ucp_v1=1.0.0-KGJjMDE3ZWViNDIwMjljYjM5N2JiNmI0MGYyMDljMzFmYTE2NzE2NTYKGQiy-aKKvQIQqduZrQYY7zEgDDgCQPEHSAQaAmxxIiAxZDcxYmM2MGYwYjM2MDUzODk2ODk1Y2QzYzlkZWIwZQ; strategyABtestKey=%221705632706.366%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAnYuCe2VNwFdRbwov14wgRCU0wcJv6a44I59NKEH2N7c%2F1705680000000%2F0%2F1705670082778%2F0%22; tt_scid=raXFtZ4sQ1RtI6UeJto2Agjoywr2686kNhLripwkcRyuXbnb0fxR29r-BZtinm1-6445; __ac_nonce=065aa8a2500f423cf9657; __ac_signature=_02B4Z6wo00f01sOf1nAAAIDCNfbfVAZSl0rDv9LAANVaoj85cz7yfcKRO7jAuwCKmmdzV7dASBaG70jxUvBb8kpjYWI.8CphkUSFbAlDD6amv2OLgzvcUcsBWK4MIPeI0gC9PPXq4TOSLFXG49; douyin.com; xg_device_score=7.353461053692719; device_web_cpu_core=8; device_web_memory_size=8; architecture=amd64; IsDouyinActive=true; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1280%2C%5C%22screen_height%5C%22%3A720%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A1.65%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A250%7D%22; csrf_session_id=a4274f00c0414ac46965e1d8ffe8e5aa; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAnYuCe2VNwFdRbwov14wgRCU0wcJv6a44I59NKEH2N7c%2F1705680000000%2F0%2F0%2F1705675907177%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSE5ZaHo2cGxXd044clpqM3ZQR0hjb0c4djhxelNtNUtYV0RvQi9lTkFWY2Z2OWxPOUtWOW1Ya05zalp3RGVLeGwrSHV6WG05K1ZCeVVsZzNLNVBaNU09IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A1%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A1%7D%22; passport_fe_beating_status=true; odin_tt=693a0ddd87a5bc25b3249a1762121a4fba737642126f2787c063aaca1846cd8b54fe5cecdcdc62037260eeb5020b0bb9; home_can_add_dy_2_desktop=%221%22; msToken=vq3ErfHhGtToRk4dIM3HOjjOD3ZBbJpxQm2MDCXLM2zlWjGzftuf__NEkMPV2B8mCoiwnRWSA_5BAG6i1uEcckMGphb0ZUtUfa1Y6ILQZjZGwxF4GygBBA==; msToken=9_S7ZGxch7zsM7KwL0zerHU3R2M_ZWdmVFaiFoHk1pLx2tMRYQYCzVzldY2cUTsTBgZvHUixo1E7ZXOt8Zn5Q3Mun-EyUsGYcRXB0oN5ihI8ncFsSiCuew=='
# btc
# btk
# failue  失败次数，超过退出


PROJECT_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(PROJECT_DIR, "xbogusss")

result_queue = queue.Queue()
try:
    fileJson = open('ltpeizhi.txt', encoding="utf-8").read().replace(" ","").replace("\\n","")
except:
    logger.ERROR("{}: 无法找到当前配置文件".format(MY_FLAG))
    time.sleep(15)
    exit()


def getToken():
    headers = {
        'authority': 'www.douyin.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'cookie': ck,
        'pragma': 'no-cache',
        'referer': 'https://www.douyin.com/discover',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-secsdk-csrf-request': '1',
        'x-secsdk-csrf-version': '1.2.22',
    }

    response = requests.head('https://www.douyin.com/service/2/abtest_config/', headers=headers)
    return response.headers['x-ware-csrf-token'].split(',')[1]


def cheak():
    url2 = 'http://43.224.248.116:8071/getSige?sec_user_id=' + secuid
    res2 = requests.get(url2,timeout=(5,5))
    return res2.json()

bwBaseUrl =  "http://121.62.23.148:8118/"
lzBaseUrl =  "http://119.188.210.55:58001/"
def getBwToken(userName,passWord):
    try:
        bwBody = {
            "userName": userName,
            "password": passWord
        }
        bwLogin = requests.post(bwBaseUrl+"api/userLogin",data=json.dumps(bwBody)).json()
        return bwLogin['data']['token']
    except:
        logger.error("百威登录失败,重新登录")
        return getLzToken(userName,passWord)
def getLzToken(userName,passWord):
    try:
        LzLogin = requests.get(lzBaseUrl + "Home/getToken?userName=" + userName + "&passWord=" + passWord).json()
        return LzLogin['token']
    except:
        logger.error("龙珠登录失败,重新登录")
        return getLzToken(userName,passWord)
byHeaders = {
    "token": ""
}
lzToken = ""
def getIp(expire):
    if isProxy == 1:
        if ip == '':  # or int(time.time()) + 10 > int(0 if expire is  not None  else expire_timestamp):
            logger.info("时间到期 或 初始化时没有ip 更换ip")
            resp = requests.post(proxyUrl,data={'belongPlace': "",'domestic': "",'groupId': "",'ipAddress': "",'isAsc': "desc",'markText': "",'orderByColumn': "timeAt",'pageNum': '1','pageSize': '10'}).json()
            fileJson['ip'] = str(resp['rows'][0]['ipAddress'])+":"+str(resp['rows'][0]['httpPort'])
            fileJson['expire_time'] = str(resp['rows'][0]['timeAt'])
            fileJson["expire_timestamp"] = int(resp['rows'][0]['endTime'])
            with open('ltpeizhi.txt', 'w') as file:
                file.write(json.dumps(fileJson, indent=4) + '\n')
            return {
                "http":"http://7LEYCu9z:JoiMIq1q@"+str(resp['rows'][0]['ipAddress'])+":"+str(resp['rows'][0]['httpPort'])
                    }
        else:
            return {
                "http": "http://7LEYCu9z:JoiMIq1q@" +ip
            }
    else:
        return  None
# i=0
try:
    fileJson = json.loads(fileJson)
    ack = fileJson['ack']
    secuid = fileJson['secuid']
    ck = fileJson['COOKIE']
    btc = fileJson['bd_ticket_guard_client_data']
    btk = fileJson['bd_ticket_guard_ree_public_key']
    sctk = getToken()
    byUserName = fileJson['byUserName']
    byPassWord = fileJson['byPassWord']
    lzUserName = fileJson['lzUserName']
    lzPassWord = fileJson['lzPassWord']
    isLt = int(fileJson['isLt'])
    isBy = int(fileJson['isBy'])
    byHeaders = {
        "token": getBwToken(byUserName, byPassWord) if isBy == 1 else None
    }
    isLz = int(fileJson['isLz'])
    isDz = int(fileJson['isDz'])
    isProxy = int(fileJson['isProxy'])
    proxyUrl = fileJson['proxyUrl']
    ip = fileJson['ip']
    expire_time = fileJson['expire_time']
    expire_timestamp = fileJson['expire_timestamp']
    lzToken = getLzToken(lzUserName,lzPassWord) if isLz == 1 else None
    failuresum = int(fileJson['errorCount'])
    slepptime = int(fileJson['sleep'])
    proxy = getIp(None)
    ip = fileJson['ip']
    expire_time = fileJson['expire_time']
    expire_timestamp = fileJson['expire_timestamp']
    logger.info("{}: 配置文件读取成功！".format(MY_FLAG))
    cheakJson = cheak()
    uid = cheakJson['data']['user']['uid']
    logger.info("{}:启动,用户名称:{}".format(MY_FLAG, cheakJson['data']['user']['nickname']))
    logger.info("{}:启动,用户sec_uid:{}".format(MY_FLAG, secuid))
    logger.info("{}:启动,用户uid:{}".format(MY_FLAG, uid))
    logger.info("{}:启动,是否启用代理:{}{}".format(MY_FLAG, True if isProxy == 1 else False,proxy))
except Exception as e:
    logger.error("{}: 配置文件错误请检查！".format(MY_FLAG))
    time.sleep(15)
    exit()
url = 'http://112.74.176.127:8020/studio/api/task/get?key=' + ack + '&platform=dy&type=dz&uid=' + uid + '&sec_uid=' + secuid

urldz = 'https://www.douyin.com/aweme/v1/web/commit/item/digg/?'

url3 = 'https://377858t20e.goho.co/checkXh'
query = "device_platform=webapp&aid=6383&channel=channel_pc_web&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1280&screen_height=720&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=120.0.0.0&browser_online=true&engine_name=Blink&engine_version=120.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=1.65&effective_type=4g&round_trip_time=250&msToken=9_S7ZGxch7zsM7KwL0zerHU3R2M_ZWdmVFaiFoHk1pLx2tMRYQYCzVzldY2cUTsTBgZvHUixo1E7ZXOt8Zn5Q3Mun-EyUsGYcRXB0oN5ihI8ncFsSiCuew=="
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

headers = {
    'authority': 'www.douyin.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'bd-ticket-guard-client-data': btc,
    'bd-ticket-guard-iteration-version': '1',
    'bd-ticket-guard-ree-public-key': btk,
    'bd-ticket-guard-version': '2',
    'bd-ticket-guard-web-version': '1',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': ck,
    'origin': 'https://www.douyin.com',
    'referer': 'https://www.douyin.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'x-secsdk-csrf-token': sctk,
}

# headers = {
#     'authority': 'www.douyin.com',
#     'accept': 'application/json, text/plain, */*',
#     'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
#     'bd-ticket-guard-client-data': btc,
#     'bd-ticket-guard-iteration-version': '1',
#     'bd-ticket-guard-ree-public-key': btk,
#     'bd-ticket-guard-version': '2',
#     'bd-ticket-guard-web-version': '1',
#     'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
#     'cookie': ck,
#     'origin': 'https://www.douyin.com',
#     'referer': 'https://www.douyin.com/user/self?modal_id=7320031142441159948&showTab=like',
#     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="120", "Google Chrome";v="120"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
#     'x-secsdk-csrf-token': '000100000001671dcfa943bc11244dd61a6144fca5ef19a2b80a33b4a4ccf56eecadd1d34b7e17ac15d0ef53807a',
# }

IsToofast = False
isParamsFlag = False

def dz(videoid):
    datas = "aweme_id=" + videoid + "&item_type=0&type=1"
    xbogus = execjs.compile(open(DATA_DIR + '.js', errors='ignore').read()).call('getXBogus', query, datas, user_agent)
    response = requests.post(
        urldz + query + "&X-Bogus=" + xbogus,
        headers=headers,
        data=datas,
        proxies=proxy,timeout=(5,5)
    )
    if (response.json()['status_code'] == 8 and response.json()['status_msg'] == "用户未登录"):
        logger.error("用户未登录")
        time.sleep(86400)
    if (response.json()['status_code'] != 0):
        print("点赞太快了，信息中...............")
        time.sleep(slepptime)
    return response.json()


def IsDz(video_id):
    xhBaseUrl = "https://www.douyin.com/aweme/v1/web/aweme/favorite/?"
    xhquery = "device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=" + secuid + "&max_cursor=0&min_cursor=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=2056&screen_height=1329&browser_language=zh-CN&browser_platform=MacIntel&browser_name=Chrome&browser_version=120.0.0.0&browser_online=true&engine_name=Blink&engine_version=120.0.0.0&os_name=Mac+OS&os_version=10.15.7&cpu_core_num=10&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&msToken=5JbERfzF2Q7t3HBXJHSmMNcuru-2Abv3kaDvWhJGz_y__i2G47Tsmf948bG3XygRdjVTNHAwFujz1_E4-wpjcXSxOwdxvqLPBWV0sj_qgGbZW4LPlNocAAC0sbjvJw=="
    xhxb = execjs.compile(open(DATA_DIR + '.js', errors='ignore').read()).call('getXBogus', xhquery, '', user_agent)
    xhrep = requests.get(
        xhBaseUrl + xhquery + '&X-Bogus=' + xhxb,
        headers=headers,
    )
    aweme_list = xhrep.json()['aweme_list']

    for item in aweme_list:
        if item['aweme_id'] == video_id:
            print("点赞成功")
            return True

    print("点赞失败")
    return False


def generate_random_str(randomlength=128):
    """
    根据传入长度产生随机字符串
    """
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789-_='
    length = len(base_str) - 1
    for _ in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str


def ttwid():
    headers = {'content-type': 'application/json'}
    data = {
        'region': 'cn',
        'aid': 1768,
        'needFid': 'false',
        'service': 'www.ixigua.com',
        'migrate_info': {
            'ticket': '',
            'source': 'node'
        },
        'cbUrlProtocol': 'https',
        'union': 'true'
    }
    response = requests.post(
        'https://ttwid.bytedance.com/ttwid/union/register/',
        headers=headers,
        json=data,
    )
    match = re.search(r'ttwid=([^;]+)', response.headers['Set-Cookie'])
    return match.group(1)


def bdTicketGuardClientData():
    data = {
        "bd-ticket-guard-version": 2,
        "bd-ticket-guard-iteration-version": 1,
        "bd-ticket-guard-ree-public-key": "BI7otMt6UTc3wcaaqSe2a+B6dHw+93WB8dsIf1eAkofqKpKxkDFXGBLGiGKx0xkKhu2QkMvILrfSmkHjyM/3xJQ=",
        "bd-ticket-guard-web-version": 1
    }
    # 使用 JSON 序列化数据
    json_data = json.dumps(data)
    # 使用 Base64 编码
    base64_encoded = base64.b64encode(json_data.encode()).decode()
    return base64_encoded


def sendwork(workid):
    # 提交任务
    url3 = 'http://112.74.176.127:8020/studio/api/task/submit?platform=dy&type=dz&studiotask_id=' + workid + '&key=' + ack
    res = requests.get(url3).json()
    return res


def jishu(count):
    count += 1
    if (count > failuresum):
        return True


# def videoDetail(videoId, sec_user_id):
#     detail_headers = {
#         'authority': 'www.douyin.com',
#         'cookie': ck,
#         'referer': 'https://www.douyin.com/video/' + videoId,
#         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
#     }
#     user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
#     query = 'device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id=' + videoId + '&pc_client_type=1&version_code=190500&version_name=19.5.0&cookie_enabled=true&screen_width=2056&screen_height=1329&browser_language=zh-CN&browser_platform=MacIntel&browser_name=Chrome&browser_version=120.0.0.0&browser_online=true&engine_name=Blink&engine_version=120.0.0.0&os_name=Mac+OS&os_version=10.15.7&cpu_core_num=10&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&msToken=CpEZa8JCxyYRCSr0KcQX7g-RcYiK_AmCO6HQ1h1Sji7quEdJaWy6VbVl6A9jwmRtkhPJCeP_dXHhB7rtzzJuwVcPpmkRGbi8CIkLpAcR1rnz2uOrvhv-lD6eqkZvIQ=='
#     xbogus = execjs.compile(open(DATA_DIR + '.js', errors='ignore').read()).call('getXBogus', query, '', user_agent)
#     detail = requests.get(
#         'https://www.douyin.com/aweme/v1/web/aweme/detail/?device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id=' + videoId + '&pc_client_type=1&version_code=190500&version_name=19.5.0&cookie_enabled=true&screen_width=2056&screen_height=1329&browser_language=zh-CN&browser_platform=MacIntel&browser_name=Chrome&browser_version=120.0.0.0&browser_online=true&engine_name=Blink&engine_version=120.0.0.0&os_name=Mac+OS&os_version=10.15.7&cpu_core_num=10&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&msToken=CpEZa8JCxyYRCSr0KcQX7g-RcYiK_AmCO6HQ1h1Sji7quEdJaWy6VbVl6A9jwmRtkhPJCeP_dXHhB7rtzzJuwVcPpmkRGbi8CIkLpAcR1rnz2uOrvhv-lD6eqkZvIQ==&X-Bogus=' + xbogus,
#         headers=detail_headers,
#     ).json()
#     desc = detail['aweme_detail']['desc']
#     # desc = '阖家安康'
#     other_headers = {
#         'cookie': 'ttwid=' + ttwid() + ';bd_ticket_guard_client_data=' + bdTicketGuardClientData() + '; msToken=' + generate_random_str(
#             128) + ';',
#         'referer': 'https://www.douyin.com/video/' + sec_user_id,
#         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
#     }

#     user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
#     query = 'device_platform=webapp&aid=6383&channel=channel_pc_web&publish_video_strategy_type=2&source=channel_pc_web&sec_user_id=' + sec_user_id
#     xbogus = execjs.compile(open(DATA_DIR + '.js', errors='ignore').read()).call('getXBogus', query, '', user_agent)
#     params = {
#         'device_platform': 'webapp',
#         'aid': '6383',
#         'channel': 'channel_pc_web',
#         'publish_video_strategy_type': '2',
#         'source': 'channel_pc_web',
#         'sec_user_id': sec_user_id,
#         'X-Bogus': xbogus,
#     }
#     try:
#         other = requests.get('https://www.douyin.com/aweme/v1/web/user/profile/other/', params=params,
#                          headers=other_headers).json()
#         uid = other['user']['uid']
#     except:
#         return False
#     headers = {
#         'authority': 'www.douyin.com',
#         'cookie': ck,
#         'referer': 'https://www.douyin.com/user/self?showTab=like',
#         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
#     }
#     url = 'device_platform=webapp&aid=6383&channel=channel_pc_web&search_channel=aweme_favorite_video&search_source=normal_search&search_scene=douyin_search&sort_type=0&publish_time=0&is_filter_search=0&query_correct_type=1&keyword=' + quote(
#         desc) + '&search_id=&offset=0&count=10&from_user=' + uid + '&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=2056&screen_height=1329&browser_language=zh-CN&browser_platform=MacIntel&browser_name=Chrome&browser_version=120.0.0.0&browser_online=true&engine_name=Blink&engine_version=120.0.0.0&os_name=Mac+OS&os_version=10.15.7&cpu_core_num=10&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&msToken=MMvIHJHuzIFpNQm8xghSRT7RxAIzsghdkqPao3AzspD2vz--Oqb7-cHaxjdesZCEnYpZZ0GP01tT350aeODopm-6TJJYBMTJxvUKdgz-cjrA8OB5MuY0pbADVL69xw=='
#     user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
#     xbogus = execjs.compile(open(DATA_DIR + '.js', errors='ignore').read()).call('getXBogus', url, '', user_agent)
#     response = requests.get(
#         'https://www.douyin.com/aweme/v1/web/home/search/item/?device_platform=webapp&aid=6383&channel=channel_pc_web&search_channel=aweme_favorite_video&search_source=normal_search&search_scene=douyin_search&sort_type=0&publish_time=0&is_filter_search=0&query_correct_type=1&keyword=' + quote(
#             desc) + '&search_id=&offset=0&count=10&from_user=' + uid + '&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=2056&screen_height=1329&browser_language=zh-CN&browser_platform=MacIntel&browser_name=Chrome&browser_version=120.0.0.0&browser_online=true&engine_name=Blink&engine_version=120.0.0.0&os_name=Mac+OS&os_version=10.15.7&cpu_core_num=10&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&msToken=MMvIHJHuzIFpNQm8xghSRT7RxAIzsghdkqPao3AzspD2vz--Oqb7-cHaxjdesZCEnYpZZ0GP01tT350aeODopm-6TJJYBMTJxvUKdgz-cjrA8OB5MuY0pbADVL69xw==&X-Bogus=' + xbogus,
#         headers=headers,
#     ).json()
#     if not response['aweme_list']:
#         print("可以点赞")
#         return True
#     else:
#         for item in response['aweme_list']:
#             if item['item']['aweme_id'] == videoId:
#                 logger.warning("重复点赞")

#                 return False
#     print("可以点赞")
#     return True

def videoDetail(videoId, sec_user_id):
    detail_headers = {
        'authority': 'www.douyin.com',
        'cookie': 'ttwid=' + ttwid() + '; bd_ticket_guard_client_data=' + bdTicketGuardClientData() + '; msToken=' + generate_random_str(
            128) + ';',
        'referer': 'https://www.douyin.com/video/' + videoId,
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    query = 'device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id=' + videoId + '&pc_client_type=1&version_code=190500&version_name=19.5.0&cookie_enabled=true&screen_width=2056&screen_height=1329&browser_language=zh-CN&browser_platform=MacIntel&browser_name=Chrome&browser_version=120.0.0.0&browser_online=true&engine_name=Blink&engine_version=120.0.0.0&os_name=Mac+OS&os_version=10.15.7&cpu_core_num=10&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&msToken=CpEZa8JCxyYRCSr0KcQX7g-RcYiK_AmCO6HQ1h1Sji7quEdJaWy6VbVl6A9jwmRtkhPJCeP_dXHhB7rtzzJuwVcPpmkRGbi8CIkLpAcR1rnz2uOrvhv-lD6eqkZvIQ=='
    xbogus = execjs.compile(open(DATA_DIR + '.js', errors='ignore').read()).call('getXBogus', query, '', user_agent)
    detail = requests.get(
        'https://www.douyin.com/aweme/v1/web/aweme/detail/?device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id=' + videoId + '&pc_client_type=1&version_code=190500&version_name=19.5.0&cookie_enabled=true&screen_width=2056&screen_height=1329&browser_language=zh-CN&browser_platform=MacIntel&browser_name=Chrome&browser_version=120.0.0.0&browser_online=true&engine_name=Blink&engine_version=120.0.0.0&os_name=Mac+OS&os_version=10.15.7&cpu_core_num=10&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&msToken=CpEZa8JCxyYRCSr0KcQX7g-RcYiK_AmCO6HQ1h1Sji7quEdJaWy6VbVl6A9jwmRtkhPJCeP_dXHhB7rtzzJuwVcPpmkRGbi8CIkLpAcR1rnz2uOrvhv-lD6eqkZvIQ==&X-Bogus=' + xbogus,
        headers=detail_headers,
    ).json()
    try:
        desc = detail['aweme_detail']['desc']
    except:
        logger.warning("detail出现异常")
        return False
    # desc = '阖家安康'
    headers = {
        'authority': 'www.douyin.com',
        'cookie': 'ttwid=' + ttwid() + '; bd_ticket_guard_client_data=' + bdTicketGuardClientData() + '; msToken=' + generate_random_str(
            128) + ';',
        'referer': 'https://www.douyin.com/user/self?showTab=like',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }
    url = 'device_platform=webapp&aid=6383&channel=channel_pc_web&search_channel=aweme_favorite_video&search_source=normal_search&search_scene=douyin_search&sort_type=0&publish_time=0&is_filter_search=0&query_correct_type=1&keyword=' + quote(
        desc) + '&search_id=&offset=0&count=10&from_user=' + uid + '&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=2056&screen_height=1329&browser_language=zh-CN&browser_platform=MacIntel&browser_name=Chrome&browser_version=120.0.0.0&browser_online=true&engine_name=Blink&engine_version=120.0.0.0&os_name=Mac+OS&os_version=10.15.7&cpu_core_num=10&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&msToken=MMvIHJHuzIFpNQm8xghSRT7RxAIzsghdkqPao3AzspD2vz--Oqb7-cHaxjdesZCEnYpZZ0GP01tT350aeODopm-6TJJYBMTJxvUKdgz-cjrA8OB5MuY0pbADVL69xw=='
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    xbogus = execjs.compile(open(DATA_DIR + '.js', errors='ignore').read()).call('getXBogus', url, '', user_agent)
    response = requests.get(
        'https://www.douyin.com/aweme/v1/web/home/search/item/?device_platform=webapp&aid=6383&channel=channel_pc_web&search_channel=aweme_favorite_video&search_source=normal_search&search_scene=douyin_search&sort_type=0&publish_time=0&is_filter_search=0&query_correct_type=1&keyword=' + quote(
            desc) + '&search_id=&offset=0&count=10&from_user=' + uid + '&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=2056&screen_height=1329&browser_language=zh-CN&browser_platform=MacIntel&browser_name=Chrome&browser_version=120.0.0.0&browser_online=true&engine_name=Blink&engine_version=120.0.0.0&os_name=Mac+OS&os_version=10.15.7&cpu_core_num=10&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&msToken=MMvIHJHuzIFpNQm8xghSRT7RxAIzsghdkqPao3AzspD2vz--Oqb7-cHaxjdesZCEnYpZZ0GP01tT350aeODopm-6TJJYBMTJxvUKdgz-cjrA8OB5MuY0pbADVL69xw==&X-Bogus=' + xbogus,
        headers=headers,
    ).json()
    try:
        if not response['aweme_list']:
            return True
        else:
            for item in response['aweme_list']:
                if item['item']['aweme_id'] == videoId:
                    logger.warning("重复点赞")
                    return False
        return True
    except:
        logger.warning("item出现异常")
        return False


loopCount = 0

def qd(type):
    if type == 1:
        return requests.get(url,proxies=proxy,timeout=(5,5)).json()
    elif type == 2:
        qdBody = {
            "sec_uid": secuid,
            "type": 1,
            "projectId": 1
        }
        return requests.post(bwBaseUrl+"api/workerPull",data=json.dumps(qdBody),headers=byHeaders,proxies=proxy,timeout=(5,5)).json()
    elif type == 3:
        lzUrl = lzBaseUrl+"Home/getTask?user_token="+lzToken+"&uId="+uid+"&secId="+secuid+"&type=1"
        rep  = requests.get(lzUrl,timeout=(5,5))
        return rep.json()

def sendBwWork(bwId,bwTaskId):
    bwBody = {
        "id": bwId,
        "taskId": bwTaskId
    }
    bwSendJson = requests.post(bwBaseUrl+"api/workerPull",data=json.dumps(bwBody),headers=byHeaders).json()
    if bwSendJson["code"] == 200:
        return True
    return False
def sendLzWork(id):
    lzSendJson = requests.get(lzBaseUrl+"/Home/saveTask?user_token="+lzToken+"&id="+id).json()
    if lzSendJson["code"] == 1:
        return True
    return False
def check_result():
    count = 0
    i = 0
    dzErrorCount = 0
    type = 1
    qzErrorCount = 0
    global proxy
    global sctk
    global ip
    global expire_time
    global expire_timestamp
    while True:
        try:
            if type == 1:
                if isLt == 0:
                    continue
                MY_FLAG = '骆驼'
            try:
                res = qd(type)
                qzErrorCount = 0
            except Exception as e:
                qzErrorCount +=1;
                if qzErrorCount % 10 == 0:
                    proxy = getIp(0)
                    ip = fileJson['ip']
                    expire_time = fileJson['expire_time']
                    expire_timestamp = fileJson['expire_timestamp']
                logger.error("{}:抢单失败".format(MY_FLAG))
                continue
            flag = False
            if type == 1:
                if res['msg'] == 'success':
                    flag = True
                    logger.info("{}:抢单成功,返回链接:{}".format(MY_FLAG, res))
                else:
                    logger.warning("{}:{}:{}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),MY_FLAG, res))
                    continue
            elif type == 2:
                if res["code"] == 200:
                    flag = True
                    logger.info("{}:抢单成功,返回链接:{}".format(MY_FLAG, res))
                else:
                    logger.warning("{}:{}:{}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),MY_FLAG, res))
            elif type == 3:
                if res["code"] == 1:
                    flag = True
                    logger.info("{}:抢单成功,返回链接:{}".format(MY_FLAG, res))
                else:
                    logger.warning("{}:{}:{}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),MY_FLAG, res))
            if flag:
                logger.info("开始点赞:{}".format(res))
                if type == 1:
                    videoid = res['data']['params']['video_id']
                    workid = res['data']['studiotask_id']
                elif type == 2:
                    videoid = res['data']['aweme_id']
                    bwId = res['data']['id']
                    bwTaskId = res['data']['taskId']
                elif type == 3:
                    videoid = res['data']['videoId']
                    lzId = res['data']['id']
                cheakJson = cheak()
                favoritingCount = cheakJson['data']['user']['favoriting_count']
                dzJson = dz(videoid)
                logger.info("点赞返回：{}".format(dzJson))
                logger.info("检测是否成功点赞")
                isDzFlag = False
                if (isDz == 1):
                    xhcount = 1
                    while True:
                        cheakJson1 = cheak()
                        favoritingCount1 = cheakJson1['data']['user']['favoriting_count']
                        logger.info("第{}次检测".format(xhcount))
                        if favoritingCount1 > favoritingCount:
                            logger.info("点赞之后数量：{}".format(favoritingCount1))
                            isDzFlag =True
                            break
                        xhcount += 1
                        if xhcount > 10:
                            logger.info("检测失败：{}".format(favoritingCount1))
                            break
                        time.sleep(0.8)
                else:
                    if dzJson['is_digg'] == 0:
                        isDzFlag = True
                if isDzFlag:
                    isSubmit = True
                    while isSubmit:
                        try:
                            if type == 1:
                                submitFlag = sendwork(workid)
                                isSubmit = False
                            elif type == 2:
                                submitFlag = sendBwWork(bwId,bwTaskId)
                                isSubmit = False
                            elif type == 3:
                                submitFlag = sendLzWork(lzId)
                                isSubmit = False
                        except:
                            isSubmit = True
                    if submitFlag:
                        dzErrorCount = 0
                        i += 1
                        logger.info("点赞成功已提交,本次运行成功点赞数:{}".format(str(i)))
                        count = 0
                    else:
                        logger.error("点赞无效")
                else:
                    count += 1
                    logger.error("无效点赞（当前连续数：{}）".format(str(count)))
                    if jishu(count):
                        # print('\033[31m无效次数大于50,进行退号.............\033[0m')
                        logger.error("无效次数大于设定,进行退号.............")
                        return
        except Exception as e:
            dzErrorCount += 1
            logger.error("点赞错误（当前连续数：{}）".format(str(dzErrorCount)))
            if dzErrorCount % 5 == 0:
                sctk = getToken()
            if jishu(dzErrorCount):
                logger.error("无效次数大于设定,进行退号.............")
                return
        finally:
            if int(time.time()) + 10 > int(fileJson['expire_timestamp']):
                proxy = getIp(0)
                ip = fileJson['ip']
                expire_time = fileJson['expire_time']
                expire_timestamp = fileJson['expire_timestamp']
            time.sleep(0)
check_result()
# 点赞 'studiotask_id': '1748374332515557376' 'video_id': '735048198483971378' 'share_url': 'https://v.douyin.com/iLU7LomS/',
