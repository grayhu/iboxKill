from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By

import settings as utils_settings
import os
import json
import platform
import datetime
import time
import hashlib
import requests
import browsercookie
from selenium import webdriver
from time import sleep


session = requests.session()


#def default_chrome_path():

    #driver_dir = getattr(utils_settings, "DRIVER_DIR", None)
    # if platform.system() == "Windows":
    #     if driver_dir:
    #         return os.path.abspath(os.path.join(driver_dir, "chromedriver.exe"))
    #
    #     raise Exception("The chromedriver drive path attribute is not found.")
    # else:
    #     if driver_dir:
    #         return os.path.abspath(os.path.join(driver_dir, "chromedriver"))
    #
    #     raise Exception("The chromedriver drive path attribute is not found.")



class ChromeDrive:
    def __init__(self, chrome_path='D:\program\chromedriver.exe', seckill_time=None, password=None):
        self.chrome_path = chrome_path
        self.seckill_time = seckill_time
       # self.seckill_time_obj = datetime.strptime(self.seckill_time, '%Y-%m-%d %H:%M:%S')
        self.password = password

    def start_driver(self):
        browser = webdriver.Chrome(executable_path=self.chrome_path)
        return browser


    def login(self, login_url: str ="https://www.nftqin.com/login"):
        if login_url:
            self.driver = self.start_driver()
            self.driver.get(login_url)
           # sleep(60)
            #accessToken =  self.getAccessToken()
            #print(accessToken)
        else:
            print("Please input the login url.")
            raise Exception("Please input the login url.")




            # try:
            #     if self.driver.find_element(By.LINK_TEXT, "登录"):
            #         print("没登录，开始点击登录按钮...")
            #         #self.driver.find_element_by_link_text("亲，请登录").click()
            #         print("请在30s内扫码登陆!!")
            #         sleep(30)
            #         if self.driver.find_element(By.CLASS_NAME,"ni ni-user"):
            #             print("登陆成功")
            #             self.getAccessToken()
            #             break
            #         else:
            #             print("登陆失败, 刷新重试, 请尽快登陆!!!")
            #             sleep(6000000)
            #             continue
            # except Exception as e:
            #     print(str(e))
            #     if self.driver.find_element(By.CLASS_NAME, "ni ni-user"):
            #         self.getAccessToken()
            #         print("登录成功")
            #         break
            #     break

     #查询商品信息
    def getGoodsInfo(self):
        ts = int(round(time.time() * 1000))
        activityId = getattr(utils_settings, "ACTIVITY_ID", None)
        param = "activity_id={0}&ts={1}&key=NiPcywkZs2eWmTIYZWHj1oTLNOggog95".format(activityId,ts)
        h1 = hashlib.md5()
        h1.update(param.encode(encoding='utf-8'))
        sign = h1.hexdigest().upper()
        getProductUrl = "https://api.nftqin.com/api/presell/activity?sign={0}&ts={1}&activity_id={2}".format(sign, ts,
                                                                                                             14)
        res = session.get(url=getProductUrl)
        if res.status_code == 200:
            print(res.json())
            return

        print("getProductUrl" + getProductUrl)

    def get_cookies(self):
        """
        手动操作浏览器，用browsercookie获取浏览器cookie
        :return:
        """
        ck = browsercookie.chrome()
        for i in ck:
            if 'nftqin' in i.domain:
                session.cookies.set(i.name, i.value)


    def getAccessToken(self):
        #self.driver.get('http://www.baidu.com/')
        accessToken = self.driver.execute_script('return localStorage.getItem("access_token");')
        return accessToken
    


    #结算商品
    def purchaseGoods(self):
        self.get_cookies()
        ts = int(round(time.time() * 1000))
        signParam = "id=61454&pay_type=sand_h5&ts={0}&key=NiPcywkZs2eWmTIYZWHj1oTLNOggog95".format(ts)
        h1 = hashlib.md5()
        h1.update(signParam.encode(encoding='utf-8'))
        sign = h1.hexdigest().upper()
        purchaseUrl = "https://api.nftqin.com/api/payment/purchase"
        accessToken = self.getAccessToken()
        accessToken = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLm5mdHFpbi5jb21cL2FwaVwvYXBwXC9sb2dpbiIsImlhdCI6MTY1MDg1OTg0OCwiZXhwIjoxNjUzNDUxODQ4LCJuYmYiOjE2NTA4NTk4NDgsImp0aSI6IkViZzBRMmh1M01paXhFZmYiLCJzdWIiOjMzMjEyMCwicHJ2IjoiMjNiZDVjODk0OWY2MDBhZGIzOWU3MDFjNDAwODcyZGI3YTU5NzZmNyJ9.XvJafbBxEU1O8GImNleMbDVpd5eJ2G_a35VzKIaMUKI"
        #accessToken = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLm5mdHFpbi5jb21cL2FwaVwvYXBwXC9sb2dpbiIsImlhdCI6MTY1MDgwNDI1MywiZXhwIjoxNjUzMzk2MjUzLCJuYmYiOjE2NTA4MDQyNTMsImp0aSI6Ik1QNzYyQkZBMndTZzQ2NUIiLCJzdWIiOjMxNDQyOCwicHJ2IjoiMjNiZDVjODk0OWY2MDBhZGIzOWU3MDFjNDAwODcyZGI3YTU5NzZmNyJ9.tHeYATkEURtflDhwpGsTEwKTetdLeCpQV4Mkt_JbMe4"
        headers = {'Accept':'application/json,text/plain,*/*',
                   'Accept-Encoding':'gzip,deflate,br',
                   'Accept-Language':'zh-CN,zh;q=0.9',
                   'Authorization':accessToken,
                   'Connection':'keep-alive',
                   'Host':'api.nftqin.com',
                   'Origin':'https://www.nftqin.com',
                   'Referer':'https://www.nftqin.com/',
                   'sec-ch-ua':'"Not A;Brand";v="99","Chromium";v="100","Google Chrome";v="100"',
                   'sec-ch-ua-mobile':'?0',
                   'sec-ch-ua-platform':'Windows',
                   'Sec-Fetch-Dest':'empty',
                   'Sec-Fetch-Mode':'cors',
                   'Sec-Fetch-Site':'same-site',
                   'Content-Type': 'application/json',
                   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
                   }
        form_data = {'id': '61454',
                     'pay_type': 'sand_h5',
                     'ts': ts,
                     'sign': sign
                     }

        res = session.post(url=purchaseUrl, data = form_data, headers = headers, verify = False)
        #res = requests.post(url=purchaseUrl, data = form_data, headers = headers, verify = False)
        print(res.encoding)
        #print(res.content.decode(encoding="utf-8"))
        print(res.json())
        if res.status_code == 200:
            print('成功提交订单')


def startKillSec():
    # ChromeDrive(seckill_time='2022-04-25 14:00:00', password='test').login('"https://www.nftqin.com/login')
    chromePost = ChromeDrive(seckill_time='2022-04-25 14:00:00', password='test')
    #chromePost.getGoodsInfo();
    chromePost.login("https://www.nftqin.com/login")
    chromePost.purchaseGoods()

if __name__ == '__main__':
    startKillSec()




