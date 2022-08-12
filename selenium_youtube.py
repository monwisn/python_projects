# Using Python and Selenium you can:
# turn on browser and YouTube,
# search for a song,
# turn on/off subtitles,
# pause/turn off a song whenever you want
# close the browser

import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def turn_on_yt():
    browser.get('https://www.youtube.com')
    browser.maximize_window()
    browser.implicitly_wait(15)

    # accept cookies policy
    cookies = browser.find_element(By.CSS_SELECTOR,
                                   "[aria-label='Accept the use of cookies and other data for the purposes described']")
    cookies.click()


def search_clip(name):
    search_form = browser.find_element(By.NAME, "search_query")
    search_form.send_keys(name)
    search_form.submit()


def turn_on_first_clip():
    for i in range(4):
        time.sleep(4)
        try:
            result = browser.find_elements(By.ID, 'video-title')
            print(result)
            result[0].click()
            break

        except Exception as e:
            print(e)


def info_banner():
    banner = browser.find_element(By.CSS_SELECTOR, "[aria-label='No thanks']")
    banner.click()  # close yt info banner


def subtitles():
    turn_on_off = browser.find_elements(By.CLASS_NAME, "ytp-subtitles-button")[0]
    turn_on_off.click()  # turn on/off subtitles


def switch_to_fullscreen():
    for i in range(10):
        time.sleep(1)
        try:
            fullscreen = browser.find_elements(By.CLASS_NAME, 'ytp-fullscreen-button')[0]
            fullscreen.click()  # same button to minimize screen
            break

        except Exception as e:
            print(e)


# def write_down_time():
#     for x in range(20):
#         time.sleep(1)
#         try:
#             c_time = browser.find_elements(By.CLASS_NAME, "ytp-time-current")[0]
#             time.sleep(12)
#             print(c_time.text)
#             c_time[0].click()
#             time.sleep(5)
#             browser.close()
#         except Exception as e:
#             print(e)


def pause():
    time.sleep(15)
    player = browser.find_elements(By.CLASS_NAME, 'ytp-play-button')[0]
    player.click()



if __name__ == "__main__":
    browser = webdriver.Firefox()
    turn_on_yt()
    time.sleep(3)
    search_clip('imagine dragons sharks')
    turn_on_first_clip()
    time.sleep(35)  # wait for the ads to end
    info_banner()
    switch_to_fullscreen()
    # subtitles()
    time.sleep(10)
    pause()
    subtitles()
    time.sleep(2)
    switch_to_fullscreen()  # minimize screen
    time.sleep(2)
    print('done')
    browser.close()
    time.sleep(2)
    quit()
