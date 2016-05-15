import os, time
from bs4 import BeautifulSoup
from selenium import webdriver
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

cwd = os.getcwd() + '/'
driver = webdriver.Chrome(cwd + 'chromedriver') # 啟動 chromedriver
driver.get('http://elearning.ling.sinica.edu.tw/CReading.html');
time.sleep(1) # 等待
search_box = driver.find_element_by_name('wordToSearch') # 取得搜尋框
search_box.send_keys('春天') # 在搜尋框內輸入關鍵字
search_box.submit() # 令 chrome driver 按下 submit
time.sleep(1)

driver.switch_to_window(driver.window_handles[1])
#print (driver)
#driver.save_screenshot('C:\spider\demo.png')確認有轉換到新的頁面
driver.find_element_by_xpath("//input[@type='submit' and @value='近義詞 Near Synonyms']").click()
time.sleep(1)

driver.switch_to_window(driver.window_handles[2])
#print (driver.title)
#driver.save_screenshot('C:\spider\demo2.png')

soup = BeautifulSoup(driver.page_source, "html.parser")
f = open('keywords.txt', 'w', encoding = 'UTF-8')
for br_tag in soup.find_all('br'):
    soup_striing = str(br_tag.next)
    f.write(soup_striing)
#    print (br_tag.next)
f.close()
driver.quit() # 關閉 chromedriver

