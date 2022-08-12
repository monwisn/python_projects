import os
import re
import json
import time

from bs4 import BeautifulSoup
from pathlib import Path

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Before running this script need to add the code that will allow you to disable the 'marionette' mode for Firefox
# (navigator.webdriver = false)

# It worked for older versions of Firefox:
# firefox_capabilities = DesiredCapabilities.FIREFOX
# firefox_capabilities['marionette'] = False
# browser = Firefox(options=opts, capabilities=firefox_capabilities)


opts = Options()
browser = Firefox(options=opts)


def turn_on_browser():
    browser.get('https://www.skyscanner.pl/')
    browser.maximize_window()
    browser.implicitly_wait(10)

    # accept cookies policy
    accept_cookies = browser.find_element(By.ID, 'acceptCookieButton')
    accept_cookies.click()
    browser.implicitly_wait(10)


def departure_city(city):
    search_form = browser.find_element(By.ID, "fsc-origin-search")
    search_form.click()
    search_form.send_keys(city)


def destination_city(city):
    search_form = browser.find_element(By.ID, "fsc-destination-search")
    search_form.send_keys(city)


def direct_flights():
    checkbox = browser.find_element(By.CSS_SELECTOR, "[aria-label='Tylko loty bezpośrednie']")
    checkbox.click()  # select only direct flights


def select_dates():
    departure_date = browser.find_element(By.ID, 'depart-fsc-datepicker-button')
    departure_date.click()

    depart_month = browser.find_element(By.ID, 'depart-calendar__bpk_calendar_nav_select')
    Select(depart_month).select_by_visible_text('Listopad 2022')

    depart_day = browser.find_element(By.CSS_SELECTOR, "[aria-label='czwartek, 17 listopada 2022']")
    depart_day.click()

    return_date = browser.find_element(By.ID, 'return-fsc-datepicker-button')
    return_date.click()

    return_month = browser.find_element(By.ID, 'return-calendar__bpk_calendar_nav_select')
    Select(return_month).select_by_visible_text('Listopad 2022')

    return_day = browser.find_element(By.CSS_SELECTOR, "[aria-label='wtorek, 22 listopada 2022']")
    return_day.click()


def adults():
    number_of_passengers = browser.find_element(By.ID,
                                                'CabinClassTravellersSelector_fsc-class-travellers-trigger__OTYyM')
    number_of_passengers.click()

    increase_the_quantity = browser.find_element(By.XPATH, '//*[@title="Zwiększ liczbę osób dorosłych"]')
    increase_the_quantity.click()  # 2 adults


def search():
    confirm = browser.find_element(By.CLASS_NAME, 'BpkLink_bpk-link__MzIwM')
    confirm.click()

    find_a_flight = browser.find_element(By.CSS_SELECTOR, "[aria-label='Szukaj']")
    find_a_flight.click()


def find_prices(city):
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')

    elements = soup.find_all("div", class_="FlightsTicket_container__NWJkY")
    departure_time = soup.find_all("div", class_="LegInfo_routePartialDepart__NzEwY")
    arrival_time = soup.find_all('div', class_='LegInfo_routePartialArrive__Y2U1N')

    departure = list()
    arrival = list()

    for i in range(6):
        r1 = re.findall(r'\d\d:\d\d', departure_time[i].text)
        r2 = re.findall(r'\d\d:\d\d', arrival_time[i].text)
        departure.append(r1)
        arrival.append(r2)

    new = list()
    dictionary = dict()

    for i in range(0, 5, 2):
        new.append(f'''
        departure: {departure[i]} -> {arrival[i]} {city}
        return: {city} {departure[i + 1]} - > {arrival[i + 1]}
        ''')

    price = list()

    for i in range(3):
        string = ''
        for j in elements[i].text:
            if j.isalpha() == False and j != ' ':
                string += j
        price.append(string)

        print(f'OFFER{i + 1}:\nprice: ' + elements[i].text + new[i])

        dictionary[f'OFFER{i + 1}'] = {
            'price': int(price[i]),
            'information': new[i]
        }

    if not os.path.exists("prices.json"):
        with open('prices.json', 'w') as file1:
            json.dump(dictionary, file1)
    else:
        with open("prices2.json", "w") as file2:
            json.dump(dictionary, file2)


def compare_json(path):
    data = list()
    elements = path.rglob('*.json')

    for element in elements:
        f = open(element.name)
        data.append(json.load(f))

    # for key in data[0]['OFFER1']['price']:
    #     print(key)
    offers_list = list()

    for i in range(len(data)):
        offer1 = data[i]['OFFER1']['price']
        offer2 = data[i]['OFFER2']['price']
        offer3 = data[i]['OFFER3']['price']

        offers_list.extend((offer1, offer2, offer3))

    print(f'The best price offer is: {min(offers_list)}')


if __name__ == '__main__':
    path = Path()
    turn_on_browser()
    departure_city('Warszawa')
    destination_city('Mediolan')
    direct_flights()
    select_dates()
    adults()
    search()
    time.sleep(25)
    find_prices('Mediolan')
    compare_json(path)
