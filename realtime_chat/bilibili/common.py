import struct
import requests as rq
import re

HEAD_FORMAT = '!IHHII'

HEAD_SIZE = 16
VERSION = 1

OPR_AUTH_REQ = 7
OPR_AUTH_RESP = 8
OPR_HEART_REQ = 2
OPR_HEART_RESP = 3
OPR_NORMAL = 5

SEQ = 1


def getRoomInfo(short_id):
    api_url = 'https://api.live.bilibili.com/room/v1/Room/room_init'
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7',
        'Host': 'api.live.bilibili.com',
        'Proxy-Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Mobile Safari/537.36'
    }
    params = {
        'id': short_id
    }
    resp = rq.get(api_url, headers = headers, params = params)
    if resp.status_code != 200:
        raise IOError('接口错误', resp.status_code, resp.text)
    data = resp.json()
    if data['code'] != 0:
        raise IOError('参数错误', resp.status_code, resp.content)
    return data


def getRoomId(uid: int):
    headers = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Mobile Safari/537.36'
    }
    url = 'https://live.bilibili.com/%d' % uid
    resp = rq.get(url, headers = headers)
    if resp.status_code != 200:
        raise IOError('站点错误', [url, resp.status_code, resp.content])

    return re.findall('[.]{30,30}12235923[.]{30,30}', resp.text)
