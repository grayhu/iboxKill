import requests
import json
import hashlib
import time

headers = """
Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: max-age=0
Connection: keep-alive
Cookie: UM_distinctid=1805b93b39c7a7-04e5f239e4a0b4-6b3e555b-151800-1805b93b39d9ff; acw_tc=0bc1599716508038514966113ed2c5eed751902686bc0f67a600e9a8800e92; SERVERID=7afbe97588e6615a05dcb865362f7800|1650803912|1650803851
Host: api.nftqin.com
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36
"""

def getGoodsInfoUrl():
    ts = int(round(time.time() * 1000))
    param = "activity_id=14&ts={0}&key=NiPcywkZs2eWmTIYZWHj1oTLNOggog95".format(ts)
    h1 = hashlib.md5()
    h1.update(param.encode(encoding='utf-8'))
    sign = h1.hexdigest().upper()
    getProductUrl = "https://api.nftqin.com/api/presell/activity?sign={0}&ts={1}&activity_id={2}".format(sign,ts,14)
    return getProductUrl

def create_headers(headers):
    headers = headers.strip().split('\n')
    headers = {x.split(':')[0].strip(): ("".join(x.split(':')[1:])).strip().replace('//', "://") for x in headers}
    return json.dumps(headers,indent=1)


if __name__ == '__main__':

    Headers = {
     "Accept": "application/json,text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
     "Accept-Encoding": "gzip, deflate, br",
     "Accept-Language": "zh-CN,zh;q=0.9",
     "Cache-Control": "max-age=0",
     "Connection": "keep-alive",
     "Cookie": "UM_distinctid=1805b93b39c7a7-04e5f239e4a0b4-6b3e555b-151800-1805b93b39d9ff; acw_tc=0bc1599716508038514966113ed2c5eed751902686bc0f67a600e9a8800e92; SERVERID=7afbe97588e6615a05dcb865362f7800|1650803912|1650803851",
     "Host": "api.nftqin.com",
     "sec-ch-ua": "'Not A;Brand';v='99', 'Chromium';v='100', 'Google Chrome';v='100'",
     "sec-ch-ua-mobile": "?0",
     "sec-ch-ua-platform": "Windows",
     "Sec-Fetch-Dest": "document",
     "Sec-Fetch-Mode": "navigate",
     "Sec-Fetch-Site": "none",
     "Sec-Fetch-User": "?1",
     "Upgrade-Insecure-Requests": "1",
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }
    goodUrl = getGoodsInfoUrl()
    #print(goodUrl)
    #print(Headers)
    resp  = requests.get(url=goodUrl)
    #print(resp.text.encode(encoding='utf-8').decode(encoding='utf-8'))  # resp.text 返回的是Unicode格式的数据
    print(resp.json())  # res.json() 返回的是json格式的数据
    goodDic = json.loads(resp.json())
    print(resp.json()['data'])
    #print(resp.content)  # resp.content返回的字节类型数据
    #print(resp.url)  # 查看完整url地址
   # print(resp.encoding)  # 查看响应头部字符编码
    #print(resp.status_code)  # 查看响应码
    #print(resp.cookies)  # 查看返回的cookies
    #print(resp.r.elapsed)  # 响应速度，从发送请求到响应到达所需要的时间