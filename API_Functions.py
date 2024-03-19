import requests

def api_test():
    url = 'https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)
