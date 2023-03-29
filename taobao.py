# from selenium import webdriver
from selenium import webdriver
import time
import datetime


# 实现淘宝网登陆功能
def login():
    driver.get('https://www.taobao.com/')
    # 定位登陆按钮，若存在则模拟点击登陆功能
    if driver.find_element_by_xpath('//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]'):
        driver.find_element_by_xpath(
            '//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]').click()
        time.sleep(3)  # 休眠3s
        # 扫码登陆
        driver.find_element_by_xpath('//*[@id="login"]/div[1]/i').click()
        print('请在10s内完成扫码')
        time.sleep(10)
        driver.get('https://cart.taobao.com/cart.htm')  # 会话保持，进入购物车
    time.sleep(3)  # 休眠3s

    # 记录当前时间
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print('login:success', now)

 # 实现下单功能


def buy(times):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        # 时间比对
        if now >= times:
            while True:
                # 定位全选按钮
                if driver.find_element_by_xpath('//*[@id="J_SelectAll1"]'):
                    try:
                        # 点击全选按钮
                        driver.find_element_by_xpath(
                            '//*[@id="J_SelectAll1"]').click()
                        # 全选点击完后跳出当前循环
                        break
                    except:
                        print('全选失败')
            time.sleep(0.2)
            while True:
                # 定位结算按钮
                # if driver.find_element_by_xpath('//*[@id="J_Go"]/span'):
                if driver.find_element_by_link_text('结 算'):
                    try:
                        # 点击结算按钮
                        driver.find_element_by_xpath(
                            '//*[@id="J_Go"]/span').click()
                        print('结算成功')
                        # 结算按钮点击完成后跳出循环
                        break
                    except:
                        print('结算失败')
            time.sleep(0.5)
            while True:
                try:
                    # 点击提交订单
                    driver.find_element_by_xpath(
                        '//*[@id="submitOrderPC_1"]/div/a[2]').click()
                    # driver.find_element_by_link_text('提交订单').click()
                    temp_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                    print('订单抢购成功,抢购时间为: ', temp_now)
                    break
                except:
                    print('订单提交失败')
                    break
            break


# 测试入口
if __name__ == '__main__':
    driver = webdriver.Chrome()
    times = input('请输入抢购时间,格式为2022-04-19 17:00:00.000000: ')
    login()
    buy(times)
