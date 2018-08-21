from selenium import webdriver

option = webdriver.ChromeOptions()
#设置请求头
#option.add_argument('--user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data')
#option.add_argument('user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"')
#设置代理
#option.add_argument('--proxy-server=http://171.37.135.94:8123')
browser = webdriver.Chrome(chrome_options=option)
try:
    browser.get('https://www.dianping.com/login')
    #iframe中的元素无法获取到，需要替换到iframe
    browser.switch_to.frame(browser.find_element_by_tag_name("iframe"))
    accountbutton = browser.find_element_by_css_selector('div.bottom-area span.bottom-password-login')
    accountbutton.click()
    iphonebutton  = browser.find_element_by_id('tab-account')
    iphonebutton.click()
    uinput = browser.find_element_by_id('account-textbox')
    #uinput.send_keys('手机号')
    uinput.send_keys('手机号')
    pinput = browser.find_element_by_id('password-textbox')
    pinput.send_keys('密码')
    button = browser.find_element_by_id('login-button-account')
    button.click()
    # print(browser.page_source)
    # print(browser.current_url)
    # print(browser.get_cookies())
    browser.get('http://www.dianping.com/shop/8910851')
    commenttag = browser.find_element_by_css_selector('div.clearfix.hotel-rooms-head > ul > li:nth-child(4)')
    commenttag.click()
    browser.implicitly_wait(10)
    morecomment = browser.find_element_by_css_selector('#comment > div > div.comment > div.more-comment > a > span:nth-child(1)')
    morecomment.click()
    browser.get('http://www.dianping.com/shop/8910851/review_all?queryType=sortType&&queryVal=latest')
    # sortbutton = browser.find_element_by_class_name('current-sort')
    # sortbutton.click()
    # sort1 = browser.find_element_by_css_selector('div.sort-selection-list >a.latest-sort')
    # sort1.click()
    print('cookies='+str(browser.get_cookies()))
    cookies = ''
    for cookie in browser.get_cookies():
        print('name='+cookie["name"])
        print('value='+cookie["value"])
        # cookies[cookie["name"]] = cookie["value"]
        temp='{}={};'.format(cookie["name"],cookie["value"])
        cookies +=temp
    print('cookies='+cookies)
finally:
    browser.close()
