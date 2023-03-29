# from selenium import webdriver
from selenium import webdriver
import time
import datetime
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# 实现淘宝网登陆功能
def login():
    driver.get('http://www.cjzzc.com/')
    # 定位登陆按钮，若存在则模拟点击登陆功能 button button-rounded button-royal
    if driver.find_element_by_class_name('button button-rounded button-royal'):
        driver.find_element_by_class_name(
            'button button-rounded button-royal').click()
        time.sleep(3)  # 休眠3s

        print('请在10s内完成扫码')
        
    time.sleep(3)  # 休眠3s

    # 记录当前时间
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print('login:success', now)

 # 实现下单功能





# 测试入口
if __name__ == '__main__':
    # driver = webdriver.Chrome()
    # # times = input('请输入抢购时间,格式为2022-04-19 17:00:00.000000: ')
    # login()


    driver = webdriver.Chrome()
    # driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get("https://www.md5.com.cn")
    # wait = WebDriverWait(driver, 20)
    driver.implicitly_wait(30)
    driver.find_element_by_class_name('el-icon-circle-close').click()
    # wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "el-icon-circle-close"))).click()
    # wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "el-icon-circle-close"))).send_keys('user name here')
 
