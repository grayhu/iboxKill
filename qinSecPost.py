import string

import requests
import time
import hashlib
import requests
import traceback
import json
from time import  sleep

#requests.adapters.DEFAULT_RETRIES = 5
# session = requests.session()
# session.keep_alive = True
import random

# 先定义一个目标子串
GRAMMAR = "ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789"


def get_cookie(cookies):
    cookie_json = json.dumps(cookies)
    with open('./cookies.txt', 'w', encoding='utf-8') as f:
        f.write(cookie_json)


def random_str1(length):
    """生成随机长度str"""
    target = ""
    grammar_length = len(GRAMMAR)-1
    if length > 0:
        for i in range(length):
            tmp_str = random.choice(GRAMMAR)	# 使用random.choice()
            tmp_str = GRAMMAR[random.randint(0, grammar_length)]	# 使用random.randint()
            target += tmp_str
        return target
    else:
        raise IndexError()


class TokenInfo:
    def __init__(self, accessToken=None, tokenType=None):
        self.accessToken = accessToken
        self.tokenType = tokenType

    def getFormat(self):
        return self.tokenType + " " + self.accessToken

class qingUtil:
    def __init__(self):
        print("init qingUtil")

    def getGoodInfo(self, activityId=None, producturl: str="https://api.nftqin.com/api/presell/activity?sign={0}&ts={1}&activity_id={2}"):
        ts = int(round(time.time() * 1000))
        param = "activity_id={0}&ts={1}&key=NiPcywkZs2eWmTIYZWHj1oTLNOggog95".format(activityId, ts)
        h1 = hashlib.md5()
        h1.update(param.encode(encoding='utf-8'))
        sign = h1.hexdigest().upper()
        getProductUrl = producturl.format(sign,ts,activityId)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        }
        res = requests.get(getProductUrl, headers=headers)
        print(res.json())
        if res.status_code == 200:
            return res.json()['data']['id']
        else:
            return ""

    def checkAuthOption(self, url:str="https://api.nftqin.com/api/payment/purchase", session=None):
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        #     'Host': 'api.nftqin.com',
        #     'Access-Control-Request-Method': 'POST',
        #     'Access-Control-Request-Headers':'authorization,content-type',
        #     'Origin':'https://www.nftqin.com',
        #     'Sec-Fetch-Mode':'cors',
        #     'Sec-Fetch-Site':'same-site',
        #     'Sec-Fetch-Dest':'empty',
        #     'Referer':'https://www.nftqin.com/',
        #     'Accept-Encoding':'gzip, deflate, br',
        #     'Accept-Language':'zh-CN,zh;q=0.9',
        #     'Accept': '*/*'
        # }

        headers = {
            'Host': 'api.nftqin.com',
            'Connection':'keep-alive',
            'Accept': '*/*',
            'Access-Control-Request-Method':'POST',
            'Access-Control-Request-Headers': 'authorization,content-type',
            'Origin':'https://www.nftqin.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15',
            #'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            #'Sec-Fetch-Mode':'cors',
            #'Sec-Fetch-Site': 'same-site',
            #'Sec-Fetch-Dest':'empty',
            'Referer': 'https://www.nftqin.com/',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9'
        }




        # reqCokies = {
        #     'CNZZDATA1280816245':'9943033-1650509372-%7C1651110218',
        #     'UM_distinctid':'1804a7cc37f456-00a757293bf359-6b3e555b-151800-1804a7cc380322'
        # }
        res = session.options(url=url, headers=headers)
        print( "auth res cookeid:" + str(res.cookies) +  " res headers" + str(res.headers))


    def testPost(self):
       ts = int(round(time.time() * 1000))
       key = "activity_id=47&product_id=69&ts={0}&key NiPcywkZs2eWmTIYZWHj1oTLNOggog95".format(ts)
       url= "https://api.nftqin.com/api/presell/tickets"
       h1 = hashlib.md5()
       h1.update(key.encode(encoding='utf-8'))
       try:
           sign = h1.hexdigest().upper()
           form_data = {'activity_id': 47,
                        'product_id': '69',
                        'ts': ts,
                        'sign': sign}
           accessToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLm5mdHFpbi5jb21cL2FwaVwvYXBwXC9sb2dpbiIsImlhdCI6MTY1MDk5MTUxNiwiZXhwIjoxNjUzNTgzNTE2LCJuYmYiOjE2NTA5OTE1MTYsImp0aSI6IjBSTjdGNllGUTVGNmhmRmQiLCJzdWIiOjMzMjEyMCwicHJ2IjoiMjNiZDVjODk0OWY2MDBhZGIzOWU3MDFjNDAwODcyZGI3YTU5NzZmNyJ9.t6ncs4xQMDrnY5iH4Aj4NuAVPxhYfxcsZ0SFsnZHZWw"

           headers = {
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
               'Authorization': accessToken,
           }
           requests.adapters.DEFAULT_RETRIES = 1
           session = requests.session()
           session.keep_alive = True
           res = requests.post(url=url, data=form_data, headers=headers, verify=False)
           print(res.text)
           print(res.status_code)
       except:
           print('fail')





    def purchaseGood(self, goodsId=None,
                     url: str="https://api.nftqin.com/api/payment/purchase",
                     payType: str="sand_h5", accessToken=None):
        requests.adapters.DEFAULT_RETRIES = 1
        session = requests.session()
        session.keep_alive = False
        #self.checkAuthOption(session=session)
        purcharseSucess = False
        ts = int(round(time.time() * 1000))
        signParam = "id={0}&pay_type={1}&ts={2}&key=NiPcywkZs2eWmTIYZWHj1oTLNOggog95".format(goodsId,payType,ts)
        h1 = hashlib.md5()
        h1.update(signParam.encode(encoding='utf-8'))
        sign = h1.hexdigest().upper()
        form_data = {'id': goodsId,
                     'pay_type': 'sand_h5',
                     'ts': ts,
                     'sign': sign
                     }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'Authorization': accessToken,
            'Host': 'api.nftqin.com'
        }

        res = session.post(url=url, data=form_data, headers=headers, verify=False, timeout=1)
        statusCode = res.status_code
        print(res.text)
       # print("status_code:" + str(statusCode) + " req cookie:" + str(session.cookies))
        if res.status_code == 200:
            resData = res.json()['data']
            if res.json()['code'] == 200:
                qrCodeUrl = resData['qrcode_url']
                print("purchase success qrCodeUrl:" + qrCodeUrl)
                purcharseSucess = True
        # cookies = ""
        # with open('./cookies.txt', 'r', encoding='utf-8') as f:
        #     data = f.read()
        #     cookies = json.loads(data)
        #for key, value in cookies.items():
         #   session.cookies.set(key, value)
        #print(session.cookies)

        #tc = random_str1(62)
        #requests.utils.add_dict_to_cookiejar(session.cookies, {'acw_tc': tc})

       # res = session.post(url=url, data=form_data, headers=headers, verify=False)




def login(userName,pwd):
    ts = int(round(time.time() * 1000))

    param = "phone={0}&ts={1}&verify={2}&key=NiPcywkZs2eWmTIYZWHj1oTLNOggog95".format(userName, ts, pwd)

    logUrl = "https://api.nftqin.com/api/app/login"
    h1 = hashlib.md5()
    h1.update(param.encode(encoding='utf-8'))
    sign = h1.hexdigest().upper()

    form_data = {'verify': pwd,
                 'phone': userName,
                 'ts': ts,
                 'sign': sign,
                 'invite_code': ''
                 }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    requests.adapters.DEFAULT_RETRIES = 1
    session = requests.session()
    session.keep_alive = False
    res = session.post(url=logUrl, data=form_data, headers=headers, verify=False)
    print(session.cookies)
    print(res.cookies)
    print(res.text)
    if res.status_code==200:
        resCode = res.json()['code']
        if resCode == 200:
            resData = res.json()['data']
            accessToken = resData['access_token']
            tokenType = resData['token_type']
            tokenInfo = TokenInfo(accessToken, tokenType);
            print("token:" + accessToken)
            return tokenInfo
    else:
        print("login error userName:" +  userName)
        return None



def getProxy():
    getIpUrl = "http://api.sgxz.cn:12080/getip?token=d31bd5229d371e412e9de7a22c933e5e&protocol=HTTP&num=199&result_format=JSON&separator=%5Cn&ip_dedup=1&time_avail=1"
    requests.adapters.DEFAULT_RETRIES = 1
    session = requests.session()
    session.keep_alive = False
    res = session.get(getIpUrl)
    resData = res.json()
    ipData = resData['data']
    return  ipData


def quickBuy(goodsId, accessToken, tokenType: str="Bearer"):
    tokenInfo = TokenInfo(accessToken, tokenType)
    reqUtil = qingUtil()
    headToken = tokenInfo.getFormat()
    tryTime = 1;
    maxTryTime = 2

    successCount = 0
    purchaseSuccess = False
    while True:
        try:
            purchaseSuccess = reqUtil.purchaseGood(goodsId, accessToken=headToken)
            if purchaseSuccess == True:
                successCount = successCount + 1
                break
            if  tryTime >= maxTryTime:
                break
            else:
                tryTime += 1
        except Exception as e:
            traceback.print_exc()
            if purchaseSuccess == True or tryTime > maxTryTime:
                break
            else:
                tryTime +=1
        finally:
            sleep(0.8)

    print("sucessCount" + str(successCount))

# def findProxyIp():
#     url = "https://mail.163.com/"
#    # proxies = {"https": "203.30.191.46:80", "http": "222.65.228.96:8085"}
#     session.keep_alive = False
#     res = session.get(url=url)
#     print(res.status_code)





if __name__ == '__main__':

     #accessToken2 = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLm5mdHFpbi5jb21cL2FwaVwvYXBwXC9sb2dpbiIsImlhdCI6MTY1MDk5MTUxNiwiZXhwIjoxNjUzNTgzNTE2LCJuYmYiOjE2NTA5OTE1MTYsImp0aSI6IjBSTjdGNllGUTVGNmhmRmQiLCJzdWIiOjMzMjEyMCwicHJ2IjoiMjNiZDVjODk0OWY2MDBhZGIzOWU3MDFjNDAwODcyZGI3YTU5NzZmNyJ9.t6ncs4xQMDrnY5iH4Aj4NuAVPxhYfxcsZ0SFsnZHZWw"
     #accessToken2 = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLm5mdHFpbi5jb21cL2FwaVwvYXBwXC9sb2dpbiIsImlhdCI6MTY1MDk5MTUxNiwiZXhwIjoxNjUzNTgzNTE2LCJuYmYiOjE2NTA5OTE1MTYsImp0aSI6IjBSTjdGNllGUTVGNmhmRmQiLCJzdWIiOjMzMjEyMCwicHJ2IjoiMjNiZDVjODk0OWY2MDBhZGIzOWU3MDFjNDAwODcyZGI3YTU5NzZmNyJ9.t6ncs4xQMDrnY5iH4Aj4NuAVPxhYfxcsZ0SFsnZHZWw"
     #quickBuy(goodsId=341870, accessToken=accessToken2)
     #ecUtil = qingUtil()
     ecUtil = qingUtil()
     ecUtil.getGoodInfo(47)
     # for i in range(20):
     #      ecUtil.testPost()



      # ecUtil = qingUtil()
      # for count in range(1):
      #     ecUtil.checkAuthOption()

       #print(random_str1(62))
       # secUtil = qingUtil()
       # for count in range(19):
       #     secUtil.getGoodInfo(42)


     #
     #
     # accessToken1 = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLm5mdHFpbi5jb21cL2FwaVwvYXBwXC9sb2dpbiIsImlhdCI6MTY1MDkzOTI1OCwiZXhwIjoxNjUzNTMxMjU4LCJuYmYiOjE2NTA5MzkyNTgsImp0aSI6IjN3N2dNVUVpRE16WHdSbVQiLCJzdWIiOjMxNDQyOCwicHJ2IjoiMjNiZDVjODk0OWY2MDBhZGIzOWU3MDFjNDAwODcyZGI3YTU5NzZmNyJ9.Zh8_6GmauUpnhBIcDiTTJST19OOPogeRKFsfCYRawp4"
     # quickBuy(goodsId=55, accessToken=accessToken1)

    # loopCount = 1
    # loginUser = None
    # while loopCount < 3:
    #     try:
    #        loginUser = login(userName=15727023402, pwd=846363)
    #        if loginUser != None:
    #            break
    #     except Exception as e:
    #         traceback.print_exc()
    #     finally:
    #         loopCount += 1
    #
    # if loginUser != None:
    #     token = loginUser.accessToken
    #     quickBuy(goodsId=29541, accessToken=token)
    #     print("loop" + str(loopCount))


    # findProxyIp();

    #读取账号文件
    # accountFile = open('account')
    # reqUtil = qingUtil()
    # for item in accountFile:
    #     userName=""
    #     pwd = ""
    #     accountItem = item.split(",")
    #     for i, info in enumerate(accountItem):
    #         if i == 0:
    #             userName = info
    #         if i == 1:
    #             pwd = info
    #     if len(userName) > 0 and len(pwd) > 0:
    #         loginUser = login(userName, pwd)
    #         if loginUser == None:
    #             print("登录失败，请检查验证码是否过期")
    #             break
    #         else:
    #             tokenInfo = TokenInfo(loginUser.accessToken, loginUser.tokenType)
    #             headToken = tokenInfo.getFormat()
    #             while True:
    #               purchaseSuccess = reqUtil.purchaseGood(goodsId=55,accessToken=headToken)
    #               if purchaseSuccess == True:
    #                   break
    #               else:
    #                   sleep(1)





