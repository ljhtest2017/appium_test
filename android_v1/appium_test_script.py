#!/usr/bin/python
# -*- coding: UTF-8 -*-
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

print('====测试开始====')
# appium 模拟器或真机 脚本
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.lemon.lemonban'
desired_caps['appActivity'] = 'com.lemon.lemonban.activity.WelcomeActivity'

# 连接appium server, 并发送它设备信息
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


# 等待元素可见
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((MobileBy.ID, "com.lemon.lemonban:id/navigation_tiku")))
# app元素定位
# 定位多个元素
eles = driver.find_element_by_class_name("android.widget.TextView")
print("多个元素：", eles)
# id元素定位
driver.find_element_by_id("com.lemon.lemonban:id/navigation_tiku").click()
# # content-desc属性来定位
# driver.find_element_by_accessibility_id("题库")
# #uiautomator 定位表达式中，要用双引号。java当中单引号和双引号不一样。
# driver.find_element_by_android_uiautomator('new UiSelector().textContain(\"公开课\")')
# # xpath定位
# driver.find_element_by_xpath('//android.widget.TextView[@test=\"公开课\"]')
# driver.quit()


# 启动app  activity
driver.activate_app()
# 安装app  install
driver.install_app()
# 卸载APP  remove
driver.remove_app()
# 拉取文件pull
driver.pull_file()
# 推送文件push
driver.push_file()
# 锁屏 lock
driver.lock()
# 解屏 unlock
driver.unlock()
# 滑动屏幕 swipe
driver.swipe()
# 获取设备的大小，也就是x和y
size = driver.get_window_size()

#向左滑
driver.swipe(size['width']*0.9, size['height']*0.5, size['width']*0.1, size['height']*0.5)

# aapt dmmp badging apk应用名

# appium inspect 定位元素

# TouchAction类
# 将一系列的动作放在一个链条中，然后将该链条传递给服务器。服务器接受该链条后，解析各个动作，逐个执行。
# 短按press  长按 longPress 点击tap 移动到move_to 等待wait 释放 release 执行perform 取消 cancel


































