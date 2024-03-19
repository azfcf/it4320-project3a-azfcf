import requests

api_key = "WSXKBS7HAVYX9L7O"

def api_test(stock_symbol, time_series_function, start_date, end_date):
    time_series_functions = {
        '1': {'function': 'TIME_SERIES_INTRADAY', 'interval': '5min'},
        '2': {'function': 'TIME_SERIES_DAILY'},
        '3': {'function': 'TIME_SERIES_WEEKLY'},
        '4': {'function': 'TIME_SERIES_MONTHLY'}
    }

    selected_function = time_series_functions.get(time_series_function)

    function_name = selected_function['function']
    url = f'https://www.alphavantage.co/query?function={function_name}&symbol={stock_symbol}&apikey={api_key}'

    if time_series_function == '1':
        url += f'&interval={selected_function.get("interval")}'

    url += f'&outputsize=full&start_date={start_date}&end_date={end_date}'

    try:
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()
        print(data)
        print(url)
    except requests.exceptions.RequestException as e:
        print("The query you selected either doesn't exist or is incorrect. Please try again.")
