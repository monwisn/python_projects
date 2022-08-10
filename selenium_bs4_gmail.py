# using Python, Selenium, BeautifulSoup, smtplib:
# create directory screenshots,
# search for a term on Wikipedia,
# take a screenshot of the searched term,
# save the text to a txt file
# send it to an email

import smtplib
import random
import time

from bs4 import BeautifulSoup
from email.message import EmailMessage
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from urllib.request import urlopen


options = Options()
options.headless = True


def turn_on_website():
    browser.get('https://pl.wikipedia.org/wiki/Wikipedia:Strona_g%C5%82%C3%B3wna')
    browser.maximize_window()
    browser.implicitly_wait(20)


def print_screen(term):
    number = random.randrange(0, 100)
    file_name = f"screenshots/{term}_{number}.png"
    browser.save_screenshot(file_name)


def search_for_a_term(term):
    browser.get('https://pl.wikipedia.org/wiki/Wikipedia:Strona_g%C5%82%C3%B3wna')
    search_form = browser.find_element(By.NAME, "search")
    search_form.send_keys(term)
    search_form.submit()


def create_txt():
    link = browser.current_url
    f = urlopen(link)
    my_file = f.read()

    soup = BeautifulSoup(my_file, features="html.parser")

    string = ''
    elements = soup.find_all("div", class_="mw-parser-output")

    for element in elements:
        element.find("table", class_="infobox").extract()
        string += element.get_text()

    with open('new.txt', 'w', encoding='UTF-8') as new_file:
        new_file.write(string)


if __name__ == "__main__":
    term = input("Enter a search term: ")
    browser = Firefox(options=options)
    turn_on_website()

    search_for_a_term(term)
    time.sleep(5)
    create_txt()
    print_screen(term)
    results = browser.find_elements(By.CLASS_NAME, 'mw-parser-output')
    print(results[0].text)
    browser.close()


with open("new.txt", 'r', encoding='UTF-8') as filename:
    variable = filename.read()
    print(variable)


# sending email:

email_text = 'new.txt'
searching = term
msg = EmailMessage()
msg['From'] = 'your_gmail'
msg['Subject'] = f'Searching term: {searching}'
msg['To'] = 'send_gmail'
msg.set_content('Wikipedia article: ')
msg.add_attachment(open(email_text, 'r', encoding='UTF-8').read())

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com.', 465)
    server.ehlo()
    server.login('your_gmail', 'gmail_password_third-party_apps')
    server.send_message(msg)
    server.close()

except Exception as error:
    print('Something went wrong...')
    raise error
