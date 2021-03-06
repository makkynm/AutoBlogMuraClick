#!/usr/bin/env python
# coding: utf-8

# In[15]:


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
driver_path = "./chromedriver" #webdriverのパス
driver = webdriver.Chrome(executable_path=driver_path)
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(10) # 秒 暗示的待機 
driver.get("https://degitalization.hatenablog.jp/entry/2020/08/02/193536") #ブログのURL 読み込み

element = wait.until(EC.visibility_of_all_elements_located)
element = driver.find_element_by_link_text("にほんブログ村")#リンクテキスト名が"日本ブログ村"の要素を取得
element.click()
time.sleep(1) 

#広告を消す
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform() #ESCキーで広告をブロック
element = wait.until(EC.visibility_of_all_elements_located)
time.sleep(5)

element = driver.find_element_by_link_text("デジタル推進課") #リンクテキスト名が"デジタル推進課"の要素を取得
driver.execute_script("arguments[0].scrollIntoView();", element) #スクロール
time.sleep(2)
element.click()

time.sleep(2) 
driver.quit() #Close Screen

