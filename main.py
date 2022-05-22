from appium import webdriver
import time


# 设置desired_capablities 字典
from selenium.webdriver.common.by import By

desired_caps = {}
# 指定移动平台操作系统
desired_caps["platformName"] = "Android"
# 指定操作系统版本
desired_caps["platformVersion"] = "8.1.0"
# 指定设备 可通过adb device查看
desired_caps["deviceName"] = "4f621d86"
# 指定需要测试的app的程序包名
desired_caps["appPackage"] = "com.box.art"
# 指定启动页面的名字
desired_caps["appActivity"] ="com.ibox.nft.app.IBoxLauncherActivity"
#desired_caps["appActivity"] =".Launcher"
# 指定每次运存测试前重新安装测试的app
desired_caps['noReset'] = False


driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
driver.implicitly_wait(5)

phonNo = 15727023402;
verifyCode = 739173;


def isElementExist(model, located):
    flag = True;
    try:
        if model == 'id':
            driver.find_element(By.ID, located)
        if model == 'xpath':
            driver.find_element(By.XPATH, located)
        if model == 'class':
            driver.find_element(By.CLASS_NAME, located)
    except:
        flag = False;
    finally:
        return flag

#浏览主页商品
def swipHomePage():
    homeBtn = driver.find_element(By.ID, "com.box.art:id/tv_navi_home")
    isFindGoods = False;
    if homeBtn:
        homeBtn.click();
        isFindGoods = findSecGoods("");
    return isFindGoods

def findSecGoods(goodsId):
    isFind = False
    size = driver.get_window_size()
    old = None;
    new = driver.page_source
    goodsName = "你到底在想什么"
    while True:
        if old == new:
            break
        else:
            if driver.page_source.find(goodsName) != -1:
                print("找到了对应商品")
                sku = driver.find_element_by_android_uiautomator('new UiSelector().textContains("畅享音乐")')
                sku.click()
                isFind = True
                break;
            else:
                driver.swipe(size['width']*0.5, size['height']*0.9,size['width']*0.5, size['height']*0.1, 200)
                time.sleep(2)
                old = new
                new = driver.page_source
    return isFind


def buyGoods():
    try:
     buyBtn = driver.find_element_by_accessibility_id("立即购买")
     #buyBtn = driver.find_element_by_android_uiautomator('new UiSelector().text("立即购买")')
     buyBtn.click()
     #确认订单页面
     if isElementExist("id", "com.box.art:id/cb_service_notice"):
        agreeCheckBox = driver.find_element(By.ID, "com.box.art:id/cb_service_notice") #同意按钮勾选
       # agreeCheckBox.__setattr__("checked", True)
        agreeCheckBox.click()
     else:
         print("未抢到")

    except:
        print("还未开始抢购，未查找到购买按钮")







def toMinePage(name):
    #driver.find_element("com.box.art:id/tv_navi_mine").click();
    #driver.find_element_by_android_uiautomator("com.box.art:id/tv_navi_mine").click();
    isLogin = False;
    if isElementExist("id", "com.box.art:id/tv_confirm"):
        confirmBtn = driver.find_element(By.ID, "com.box.art:id/tv_confirm")
        confirmBtn.click();
    if isElementExist("id","com.box.art:id/tv_navi_mine"):
        navMineBtn = driver.find_element(By.ID, "com.box.art:id/tv_navi_mine")
        navMineBtn.click();
        if isElementExist("id", "com.box.art:id/tv_wallet_address"):
           print("已登录")
           isLogin = True
        else:
           driver.find_element(By.ID, "com.box.art:id/met_phone").set_value(phonNo)
           driver.find_element(By.ID, "com.box.art:id/met_smscode").set_value(verifyCode);
           driver.find_element(By.ID, "com.box.art:id/btn_login").click();
          # time.sleep(1)
           if isElementExist("id", "com.box.art:id/tv_navi_mine"):
               navMineBtn = driver.find_element(By.ID, "com.box.art:id/tv_navi_mine")
               navMineBtn.click();
               if isElementExist("id", "com.box.art:id/tv_wallet_address"):
                   print("登陆成功");
                   isLogin = True;
               else:
                   print("登录失败")
           else:
               print("登录失败，验证码过期")
        return isLogin









# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    isLogin = toMinePage('PyCharm')
    if isLogin:
        isFindGoods = swipHomePage();
        if isFindGoods:
            #while True:
                print("开始抢购")
                buyGoods()
        else:
            print("未查找到指定商品")
    else:
        print("登录验证不通过")



