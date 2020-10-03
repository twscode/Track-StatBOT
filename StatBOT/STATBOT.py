import time
import selenium
import warnings



warnings.filterwarnings("ignore")
print("Thank you for using Teddy Wimberly's")
print(" ____  _        _   ____   ___ _____ ")
print("/ ___|| |_ __ _| |_| __ ) / _ \_   _|")
print("\___ \| __/ _` | __|  _ \| | | || |  ")
print(" ___) | || (_| | |_| |_) | |_| || |  ")
print("|____/ \__\__,_|\__|____/ \___/ |_| ")
print("READ ME: In about 15 seconds, StatBOT will automatically open four tabs that display some of my accomplishments during my track career. After the video on tab 3 is over, and tab four opens, you are free to navigate the tabs as you wish!👍")
time.sleep(15) # delay for 15 seconds

PATH = "C:\Program Files (x86)\chromedriver.exe"
from selenium import webdriver
driver = webdriver.Chrome
driver = webdriver.Chrome(PATH)
driver.get ("https://www.athletic.net/TrackAndField/Athlete.aspx?AID=12560862")
print(driver.title)
driver.execute_script("window.scrollTo(400, 500)")
time.sleep(3)
driver.execute_script("window.open();")
driver.switch_to_window(driver.window_handles[1])
driver.get ("https://www.facebook.com/1481292358830213/posts/watch-teddy-wimberly-of-mount-st-joseph-upset-5-other-guys-who-have-gone-sub-11-/2101436750149101/")
time.sleep(3)
driver.execute_script("window.open();")
driver.switch_to_window(driver.window_handles[2])
driver.get ("https://www.youtube.com/watch?v=CeYWKokR9us&feature=youtu.be")
print(driver.title)
time.sleep(41)
driver.execute_script("window.open();")
driver.switch_to_window(driver.window_handles[3])
driver.get ("https://miaasports.net/2020-all-miaa-indoor-track/")
driver.execute_script("window.scrollTo(2200, 2200)")
print(driver.title)




# ____  _                               _     _       
#/ ___|| |_ ___  _ __ __ _  __ _  ___  | |__ (_)_ __  
#\___ \| __/ _ \| '__/ _` |/ _` |/ _ \ | '_ \| | '_ \ 
# ___) | || (_) | | | (_| | (_| |  __/ | |_) | | | | |
#|____/ \__\___/|_|  \__,_|\__, |\___| |_.__/|_|_| |_|
#                          |___/                      
#image = Image.open('medals.jpg')
#image.show()
#play_link = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[4]/button')
#play_link.click()
# click radio button
#play_link = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[4]/button')
#play_link.click()
#//*[@id="cmg-app-content"]/div[1]/div[1]/div/div/div[2]/div/div/div
#/html/body/div[1]/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div/div/div
#/html/body/div[1]/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div
#/html/body/div[1]/div[1]/div[2]/div[1]/div[3]/div/div[1]/div/div[1]/img
#/html/body/div[4]/div/button
#/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[4]/button

