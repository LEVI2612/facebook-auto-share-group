#this is my first super mini project fresh year man 
#created in 15/05/2023
#make sure u download chromedriver you can find it in : https://chromedriver.chromium.org/downloads find the same version of your chrome extension 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 
import time

#replace the group that u want to share to 

groups = ['MobileLegends','215858421926082','417986378746621','1275517625932600','1299027166832650','2058923737698685'] #group you can find it by enter the group example : https://facebook.com/groups/********** copy the ******* and replace it in code 

post = 'https://www.facebook.com/photo?fbid=546824187637397&set=a.352316400421511' #this is the post link u want to post in the group 
#make it dimissed notification

options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome("/Users/lychhievtong/Documents/chromedriver_mac_arm64/chromedriver", options=options)

while True:
#get user input facebook email and password 
    username = input ("Input your email : ")
    password = input("Input your password : ")


#open facebook and login to your acc
    driver.get('https://facebook.com/')
    driver.find_element(By.ID,'email').send_keys(username)
    driver.find_element(By.ID, 'pass').send_keys(password)
    driver.find_element(By.NAME , 'login').click()
    time.sleep(2)

    if 'login' in driver.current_url: 
        print("Invalid email or password. Please try again.")
    else:
        print('Successful Login')
        break
        

#posting in groups 
for i in range (len(groups)) : 
    link = 'https://facebook.com/groups/'+groups[i]
    driver.get(link)
    time.sleep(3)
    group_p = driver.find_element(By.XPATH ,"//div[@class='x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xmjcpbm x107yiy2 xv8uw2v x1tfwpuw x2g32xy x78zum5 x1q0g3np x1iyjqo2 x1nhvcw1 x1n2onr6 xt7dq6l x1ba4aug x1y1aw1k xn6708d xwib8y2 x1ye3gou']")
    group_p.click()
    time.sleep(3)
    group_p.find_element(By.XPATH , "//div[@class='_1mf _1mj']").send_keys(post)
    time.sleep(3)
    stt = group_p.find_element(By.XPATH, "//div[@class='_1mf _1mj']")
    stt.send_keys(Keys.COMMAND+'a')
    stt.send_keys(Keys.DELETE)
    time.sleep(1)
    group_p.find_element(By.XPATH ,"//div[@aria-label='Post']//div[@class='x1n2onr6 x1ja2u2z x78zum5 x2lah0s xl56j7k x6s0dn4 xozqiw3 x1q0g3np xi112ho x17zwfj4 x585lrc x1403ito x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xn6708d x1ye3gou xtvsq51 x1r1pt67']").click()
    time.sleep(5)
    print('post sucessfully !! ')
    
#after it done all your group post it'll close your chrome driver 

#u can set up the time either to make it faster !!!
