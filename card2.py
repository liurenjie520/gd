import datetime
import json
import os
import requests
import urllib





def chuyi():
    headers = {
        "Host": "www.iamwawa.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Cookie": "PHPSESSID=d41i5vvp52a119knuokqk2ilh0; Hm_lpvt_ca368c21c1d2aa60e6f63d598c4cb02a=1624081986"
    }
    url = "https://www.iamwawa.cn/nongli/api"
    year = datetime.datetime.today().year
    year = str(year)
    params = {
        'type': 'lunar',
        'year': year,
        'month': 1,
        'day': 1
    }

    r = requests.post(url, headers=headers, data=params)
    js = json.loads(r.text)
    # print(js)
    save_str = js["data"]["solar"]
    a1=save_str.replace('年', '')
    a2=a1.replace('月', '')
    a3=a2.replace('日', '')
    a3 = a3[4:]
    # print(type(save_str))
    # print(a3)
    return a3

def yuanxiao():
    headers = {
        "Host": "www.iamwawa.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Cookie": "PHPSESSID=d41i5vvp52a119knuokqk2ilh0; Hm_lpvt_ca368c21c1d2aa60e6f63d598c4cb02a=1624081986"
    }
    url = "https://www.iamwawa.cn/nongli/api"
    year = datetime.datetime.today().year
    year = str(year)
    params = {
        'type': 'lunar',
        'year': year,
        'month': 1,
        'day': 15
    }

    r = requests.post(url, headers=headers, data=params)
    js = json.loads(r.text)
    # print(js)
    save_str = js["data"]["solar"]
    a1=save_str.replace('年', '')
    a2=a1.replace('月', '')
    a3=a2.replace('日', '')
    a3 = a3[4:]
    # print(type(save_str))
    # print(a3)
    return a3


def duanwu():
    headers = {
        "Host": "www.iamwawa.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Cookie": "PHPSESSID=d41i5vvp52a119knuokqk2ilh0; Hm_lpvt_ca368c21c1d2aa60e6f63d598c4cb02a=1624081986"
    }
    url = "https://www.iamwawa.cn/nongli/api"
    year = datetime.datetime.today().year
    year = str(year)
    params = {
        'type': 'lunar',
        'year': year,
        'month': 5,
        'day': 5
    }

    r = requests.post(url, headers=headers, data=params)
    js = json.loads(r.text)
    # print(js)
    save_str = js["data"]["solar"]
    a1=save_str.replace('年', '')
    a2=a1.replace('月', '')
    a3=a2.replace('日', '')
    a3 = a3[4:]
    # print(type(save_str))
    # print(a3)
    return a3


def qixi():
    headers = {
        "Host": "www.iamwawa.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Cookie": "PHPSESSID=d41i5vvp52a119knuokqk2ilh0; Hm_lpvt_ca368c21c1d2aa60e6f63d598c4cb02a=1624081986"
    }
    url = "https://www.iamwawa.cn/nongli/api"
    year = datetime.datetime.today().year
    year = str(year)
    params = {
        'type': 'lunar',
        'year': year,
        'month': 7,
        'day': 7
    }

    r = requests.post(url, headers=headers, data=params)
    js = json.loads(r.text)
    # print(js)
    save_str = js["data"]["solar"]
    a1=save_str.replace('年', '')
    a2=a1.replace('月', '')
    a3=a2.replace('日', '')
    a3 = a3[4:]
    # print(type(save_str))
    # print(a3)
    return a3

def zhongyuan1():
    headers = {
        "Host": "www.iamwawa.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Cookie": "PHPSESSID=d41i5vvp52a119knuokqk2ilh0; Hm_lpvt_ca368c21c1d2aa60e6f63d598c4cb02a=1624081986"
    }
    url = "https://www.iamwawa.cn/nongli/api"
    year = datetime.datetime.today().year
    year = str(year)
    params = {
        'type': 'lunar',
        'year': year,
        'month': 7,
        'day': 14
    }

    r = requests.post(url, headers=headers, data=params)
    js = json.loads(r.text)
    # print(js)
    save_str = js["data"]["solar"]
    a1=save_str.replace('年', '')
    a2=a1.replace('月', '')
    a3=a2.replace('日', '')
    a3 = a3[4:]
    # print(type(save_str))
    # print(a3)
    return a3


def zhongyuan2():
    headers = {
        "Host": "www.iamwawa.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Cookie": "PHPSESSID=d41i5vvp52a119knuokqk2ilh0; Hm_lpvt_ca368c21c1d2aa60e6f63d598c4cb02a=1624081986"
    }
    url = "https://www.iamwawa.cn/nongli/api"
    year = datetime.datetime.today().year
    year = str(year)
    params = {
        'type': 'lunar',
        'year': year,
        'month': 7,
        'day': 15
    }

    r = requests.post(url, headers=headers, data=params)
    js = json.loads(r.text)
    # print(js)
    save_str = js["data"]["solar"]
    a1=save_str.replace('年', '')
    a2=a1.replace('月', '')
    a3=a2.replace('日', '')
    a3 = a3[4:]
    # print(type(save_str))
    # print(a3)
    return a3


def zhongqiu():
    headers = {
        "Host": "www.iamwawa.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Cookie": "PHPSESSID=d41i5vvp52a119knuokqk2ilh0; Hm_lpvt_ca368c21c1d2aa60e6f63d598c4cb02a=1624081986"
    }
    url = "https://www.iamwawa.cn/nongli/api"
    year = datetime.datetime.today().year
    year = str(year)
    params = {
        'type': 'lunar',
        'year': year,
        'month': 8,
        'day': 15
    }

    r = requests.post(url, headers=headers, data=params)
    js = json.loads(r.text)
    # print(js)
    save_str = js["data"]["solar"]
    a1=save_str.replace('年', '')
    a2=a1.replace('月', '')
    a3=a2.replace('日', '')
    a3 = a3[4:]
    # print(type(save_str))
    # print(a3)
    return a3


def chongyang():
    headers = {
        "Host": "www.iamwawa.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Cookie": "PHPSESSID=d41i5vvp52a119knuokqk2ilh0; Hm_lpvt_ca368c21c1d2aa60e6f63d598c4cb02a=1624081986"
    }
    url = "https://www.iamwawa.cn/nongli/api"
    year = datetime.datetime.today().year
    year = str(year)
    params = {
        'type': 'lunar',
        'year': year,
        'month': 9,
        'day': 9
    }

    r = requests.post(url, headers=headers, data=params)
    js = json.loads(r.text)
    # print(js)
    save_str = js["data"]["solar"]
    a1=save_str.replace('年', '')
    a2=a1.replace('月', '')
    a3=a2.replace('日', '')
    a3 = a3[4:]
    # print(type(save_str))
    # print(a3)
    return a3


def laba():
    headers = {
        "Host": "www.iamwawa.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Cookie": "PHPSESSID=d41i5vvp52a119knuokqk2ilh0; Hm_lpvt_ca368c21c1d2aa60e6f63d598c4cb02a=1624081986"
    }
    url = "https://www.iamwawa.cn/nongli/api"
    year = datetime.datetime.today().year
    year = str(year)
    params = {
        'type': 'lunar',
        'year': year,
        'month': 12,
        'day': 8
    }

    r = requests.post(url, headers=headers, data=params)
    js = json.loads(r.text)
    # print(js)
    save_str = js["data"]["solar"]
    a1=save_str.replace('年', '')
    a2=a1.replace('月', '')
    a3=a2.replace('日', '')
    a3 = a3[4:]
    # print(type(save_str))
    # print(a3)
    return a3

def xiaonian1():
    headers = {
        "Host": "www.iamwawa.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Cookie": "PHPSESSID=d41i5vvp52a119knuokqk2ilh0; Hm_lpvt_ca368c21c1d2aa60e6f63d598c4cb02a=1624081986"
    }
    url = "https://www.iamwawa.cn/nongli/api"
    year = datetime.datetime.today().year
    year = str(year)
    params = {
        'type': 'lunar',
        'year': year,
        'month': 12,
        'day': 23
    }

    r = requests.post(url, headers=headers, data=params)
    js = json.loads(r.text)
    # print(js)
    save_str = js["data"]["solar"]
    a1=save_str.replace('年', '')
    a2=a1.replace('月', '')
    a3=a2.replace('日', '')
    a3 = a3[4:]
    # print(type(save_str))
    # print(a3)
    return a3



def xiaonian2():
    headers = {
        "Host": "www.iamwawa.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Cookie": "PHPSESSID=d41i5vvp52a119knuokqk2ilh0; Hm_lpvt_ca368c21c1d2aa60e6f63d598c4cb02a=1624081986"
    }
    url = "https://www.iamwawa.cn/nongli/api"
    year = datetime.datetime.today().year
    year = str(year)
    params = {
        'type': 'lunar',
        'year': year,
        'month': 12,
        'day': 24
    }

    r = requests.post(url, headers=headers, data=params)
    js = json.loads(r.text)
    # print(js)
    save_str = js["data"]["solar"]
    a1=save_str.replace('年', '')
    a2=a1.replace('月', '')
    a3=a2.replace('日', '')
    a3=a3[4:]
    # print(type(save_str))
    # print(a3)
    return a3


def qingming1():
    headers = {
        "Host": "www.iamwawa.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Cookie": "PHPSESSID=d41i5vvp52a119knuokqk2ilh0; Hm_lpvt_ca368c21c1d2aa60e6f63d598c4cb02a=1624081986"
    }
    url = "https://www.iamwawa.cn/nongli/api"
    year = datetime.datetime.today().year
    year = str(year)
    params = {
        'type': 'lunar',
        'year': year,
        'month': 4,
        'day': 4
    }

    r = requests.post(url, headers=headers, data=params)
    js = json.loads(r.text)
    # print(js)
    save_str = js["data"]["solar"]
    a1=save_str.replace('年', '')
    a2=a1.replace('月', '')
    a3=a2.replace('日', '')
    a3=a3[4:]
    # print(type(save_str))
    # print(a3)
    return a3

def qingming2():
    headers = {
        "Host": "www.iamwawa.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Cookie": "PHPSESSID=d41i5vvp52a119knuokqk2ilh0; Hm_lpvt_ca368c21c1d2aa60e6f63d598c4cb02a=1624081986"
    }
    url = "https://www.iamwawa.cn/nongli/api"
    year = datetime.datetime.today().year
    year = str(year)
    params = {
        'type': 'lunar',
        'year': year,
        'month': 4,
        'day': 5
    }

    r = requests.post(url, headers=headers, data=params)
    js = json.loads(r.text)
    # print(js)
    save_str = js["data"]["solar"]
    a1=save_str.replace('年', '')
    a2=a1.replace('月', '')
    a3=a2.replace('日', '')
    a3=a3[4:]
    # print(type(save_str))
    # print(a3)
    return a3

def qingming3():
    headers = {
        "Host": "www.iamwawa.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Cookie": "PHPSESSID=d41i5vvp52a119knuokqk2ilh0; Hm_lpvt_ca368c21c1d2aa60e6f63d598c4cb02a=1624081986"
    }
    url = "https://www.iamwawa.cn/nongli/api"
    year = datetime.datetime.today().year
    year = str(year)
    params = {
        'type': 'lunar',
        'year': year,
        'month': 4,
        'day': 6
    }

    r = requests.post(url, headers=headers, data=params)
    js = json.loads(r.text)
    # print(js)
    save_str = js["data"]["solar"]
    a1=save_str.replace('年', '')
    a2=a1.replace('月', '')
    a3=a2.replace('日', '')
    a3=a3[4:]
    # print(type(save_str))
    # print(a3)
    return a3


if __name__ == '__main__':
    print(xiaonian2())

