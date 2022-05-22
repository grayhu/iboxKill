# Press the green button in the gutter to run the script.
from datetime import datetime

from selenium import webdriver
import time
import traceback
import  hashlib

#跳转登录流程
from selenium.webdriver.common.by import By

userName = 15727023402
smsCode = 724820


def toLoginPage(userName,smsCode):
    print("跳转登录页面")
    browser.get("https://www.nftqin.com/login")
    #browser.find_element(By.NAME, "phone").text(userName);
    #browser.find_element(By.NAME, "phone").text(userName);
    formText = browser.find_elements(By.CLASS_NAME, "form-control");
    for i in formText:
        if i.get_attribute("name") == "phone":
            print("找到电话号码搜索框")
            i.send_keys(userName)
        if i.get_attribute("placeholder") == "Verify":
            print("找到验证码输入框")
            i.send_keys(smsCode)
    agreeBox = browser.find_element(By.CLASS_NAME, "el-checkbox__inner");
    agreeBox.click()
    btns = browser.find_elements(By.TAG_NAME, "button")
    for btn in btns:
        if btn.get_attribute("type") == "submit":
            #btn.click()
            browser.execute_script("arguments[0].click();", btn)


#获取商品信息
def getGoodsInfo():
    ts = int(round(time.time() * 1000))
    param = "activity_id=14&ts={0}&key=NiPcywkZs2eWmTIYZWHj1oTLNOggog95".format(ts)
    h1 = hashlib.md5()
    h1.update(param.encode(encoding='utf-8'))
    sign = h1.hexdigest().upper()
    getProductUrl = "https://api.nftqin.com/api/presell/activity?sign={0}&ts={1}&activity_id={2}".format(sign,ts,14)
    res = browser.get(getProductUrl)
    print("getProductUrl" + getProductUrl)

#加车下单
def purchaseGoods():
    ts = int(round(time.time() * 1000))
    signParam = "id=25492&pay_type=sand_h5&ts={0}&key=NiPcywkZs2eWmTIYZWHj1oTLNOggog95".format(ts)
    h1 = hashlib.md5()
    h1.update(signParam.encode(encoding='utf-8'))
    sign = h1.hexdigest().upper()
    commonParam = "id=25492&pay_type=sand_h5"
    purchaseUrl = "https://api.nftqin.com/api/payment/purchase?sign={0}&ts={1}&{2}".format(sign,ts,commonParam)
    res = browser.get(purchaseUrl)
    print("purchaseUrl" + purchaseUrl)

if __name__ == '__main__':
    chrome_path = "D:\program\chromedriver.exe"
    browser = webdriver.Chrome(executable_path=chrome_path)
    response = browser.get("https://www.nftqin.com/presellDetails?productId=53&activeId=42")
    print(response)
    try:
     browser.find_elements(By.LINK_TEXT, "登录")
     #toLoginPage(userName, smsCode)
    except Exception as e:
      print("已登录")
      traceback.print_exc()
    getGoodsInfo()
    #purchaseGoods()
