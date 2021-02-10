from selenium import webdriver 
import selenium
import time
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.common.keys import Keys
import string
import random

###################################################################################################################
#############################  Only these are the values to be added  #############################################

facebook_id = ""   # facebook id
facebook_pass = "" # facebook pass
Post_content = "Hello World!"  # content of the facebook post to be made
Comment = "Comment Made"  # Comment on the random friend timeline's first post

###################################################################################################################




chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options) 
driver.get('https://www.facebook.com/') 
driver.maximize_window()
driver.implicitly_wait(5)

# enter username and password and login
driver.find_element_by_id("email").send_keys(facebook_id) 
driver.find_element_by_id("pass").send_keys(facebook_pass)
driver.find_element_by_name("login").click()
time.sleep(5)

# open profile
driver.get('https://www.facebook.com/me') 
time.sleep(5)

# get location
intro=driver.find_element_by_css_selector("div[data-pagelet='ProfileTilesFeed_0']")
elements=intro.find_elements_by_css_selector("span[class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql rrkovp55 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v knj5qynh oo9gr5id hzawbc8m']")
flag = 1
for el in elements:
    if "Lives in " in el.text:
        flag=0
        location = el.text

if flag:
    # if location not in the id get a random friends of friends
    time.sleep(3)
    driver.find_element_by_css_selector("input[placeholder='Search Facebook']").send_keys(random.choice(string.ascii_letters))
    driver.find_element_by_css_selector("input[placeholder='Search Facebook']").send_keys(Keys.RETURN)
    time.sleep(4)
    driver.refresh()
    time.sleep(4)
    driver.find_element_by_xpath("//*[contains(text(), 'People')]").click()
    driver.find_element_by_css_selector("input[aria-label='Friends of friends'][type='checkbox']").click()
else:
    driver.find_element_by_css_selector("input[placeholder='Search Facebook']").send_keys(location)
    driver.find_element_by_css_selector("input[placeholder='Search Facebook']").send_keys(Keys.RETURN)
    driver.find_element_by_xpath("//*[contains(text(), 'People')]").click()

time.sleep(4)
driver.refresh()
driver.find_element_by_css_selector("a[role='link'][tabindex='0'][class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p dkezsu63']").click()
add_friend = driver.find_element_by_css_selector("div[data-pagelet='ProfileActions']")

# add friend
# if already a friend a random friends of friends is added
while True:
    try:
        add_friend.find_element_by_xpath("//*[contains(text(), 'Add Friend')]").click()
        time.sleep(4)
        break
    except selenium.common.exceptions.NoSuchElementException:
        driver.find_element_by_css_selector("input[placeholder='Search Facebook']").send_keys(random.choice(string.ascii_letters))
        driver.find_element_by_css_selector("input[placeholder='Search Facebook']").send_keys(Keys.RETURN)
        time.sleep(4)
        driver.refresh()
        driver.find_element_by_xpath("//*[contains(text(), 'People')]").click()
        driver.find_element_by_css_selector("input[aria-label='Friends of friends'][type='checkbox']").click()
        driver.refresh()
        time.sleep(4)
        driver.find_element_by_css_selector("a[role='link'][tabindex='0'][class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p dkezsu63']").click()
        add_friend = driver.find_element_by_css_selector("div[data-pagelet='ProfileActions']")
        continue

# create a post with the post content
driver.get('https://www.facebook.com/')
post = driver.find_element_by_css_selector("div[aria-label='Create a post']")
post.find_element_by_css_selector("span[class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7']").click()
driver.find_element_by_xpath("//*[@id='mount_0_0']/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div").send_keys(Post_content)
driver.find_element_by_css_selector("div[aria-label='Post']").click()
time.sleep(4)

# comment on a random friend's timeline's first post
driver.get('https://www.facebook.com/me/friends')
driver.find_element_by_css_selector("input[placeholder='Search']").send_keys(random.choice(string.ascii_letters))
driver.find_element_by_css_selector("input[placeholder='Search']").send_keys(Keys.RETURN)
time.sleep(3)
while True:
    try:
        driver.find_element_by_xpath("//*[contains(text(), 'No results for')]").is_displayed()
        time.sleep(2)
        driver.get('https://www.facebook.com/me/friends')
        driver.find_element_by_css_selector("input[placeholder='Search']").send_keys(random.choice(string.ascii_letters))
        driver.find_element_by_css_selector("input[placeholder='Search']").send_keys(Keys.RETURN)
        time.sleep(2)
        continue
    except:
        break
time.sleep(4)
driver.find_element_by_css_selector("a[class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8'][role='link'][tabindex='0']").click()
driver.find_element_by_css_selector("div[aria-label='Write a comment']").send_keys(Comment)
driver.find_element_by_css_selector("div[aria-label='Write a comment']").send_keys(Keys.RETURN)

time.sleep(10)
driver.quit()