from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time as t



chrome_options = Options()
chrome_options.add_argument("--no-sandbox")

webdriver_service = Service("chromedriver/chromedriver") ## path to where you saved chromedriver binary
browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

song_list = []
url='https://open.spotify.com/playlist/4z5whwZPQuMotubMwwlsLB?si=VxXgMLUORcO-ym6OwB420A&nd=1'
browser.get(url)

try:
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))).click()
    print("accepted cookies")
except Exception as e:
    print('no cookie button')


bottom_sentinel = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='bottom-sentinel']")))

for x in range(5):
    songs = WebDriverWait(browser, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@data-testid='tracklist-row']")))
    for song in songs:
        print(song.text)
        song_list.append(song.text)
    t.sleep(2)
    bottom_sentinel.location_once_scrolled_into_view
    browser.implicitly_wait(15)
print(list(set(song_list)))
print('Total songs:', len(list(set(song_list))))