import requests


def currency_convertor():

    currency_in = input('Please input the currency code you want to exchange \n')
    currency = requests.get('http://www.floatrates.com/daily/' + f'{currency_in}' + '.json')

    cache = {}

#EUR/USD automatically added to cache

    if currency_in.lower() == 'usd':
        cache['eur'] = currency.json()['eur']
    elif currency_in.lower() == 'eur':
        cache['usd'] = currency.json()['usd']
    else:
        cache['usd'] = currency.json()['usd']
        cache['eur'] = currency.json()['eur']

    while True:

        currency_out = input('Please input the currency code you want to receive \n')
        if currency_out == "":
            break
        amount = float(input('Please input the amount of currency you have \n'))

        if currency_out.lower() in cache:
            print('Checking the cache...')
            print('Oh! It is in the cache')
            print(f"You received {round((((cache[currency_out.lower()]['rate']) * amount)),2)} {currency_out.upper()}.")
        else:
            print('Checking the cache...')
            print('Sorry, but it is not in the cache!')
            print(f"You received {round((((currency.json()[currency_out]['rate']) * amount)),2)} {currency_out.upper()}.")
            cache[currency_out.lower()] = currency.json()[currency_out]


currency_convertor()

