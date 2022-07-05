# Using the input() function ask the user for the currency that would like to exchange
# and then the amount of currency to be exchanged.
# Display the value at the rate taken from an external API.

import requests

response = requests.get('http://api.nbp.pl/api/exchangerates/tables/A')
request = response.json()
currency = input('Which currency do you want to exchange: [USD/EUR/CHF]: ')
quantity = int(input('How much currency do you want to exchange '))

for rate in request[0]['rates']:
    if currency == rate['code']:
        result = quantity * float(rate['mid'])
        print(f'As a result, you will receive {round(result, 2)} PLN.')

        break

