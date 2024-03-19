
import requests

def api_test():
    url = 'https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)

def get_user_input():
    
    while True:
        stock_symbol = input("\nEnter the stock symbol you are looking for: ")
        if stock_symbol.strip():  # Check if the input is not empty
            break
        print("Invalid input. Please try again.")

    while True:
        print("\nChart types \n ----------- \n 1. Bar \n 2. Line\n")
        chart_type = input("Enter the chart type (1, 2): ")
        if chart_type in ('1', '2'):  # Check if the input is either '1' or '2'
            break
        print("Invalid input. Please try again.")

    while True:
        print("\nSelect the time series of the chart you want to generate \n ------------------------------------- \n 1. Intraday \n 2. Daily\n 3. Weekly \n 4. Monthly")
        time_series_function = input("Enter the time series option (1, 2, 3, 4): ")
        if time_series_function.strip() in ('1', '2', '3', '4'):  # Check if the input is one of the valid options
            break
        print("Invalid input. Please try again.")  

    while True:
        start_date = input("Enter the start date (YYYY-MM-DD): ")
        if len(start_date.strip()) == 10:  # Check if the input has the correct length
            break
        print("Invalid input. Please try again.")

    while True:
        end_date = input("Enter the end date (YYYY-MM-DD): ")
        if len(end_date.strip()) == 10:  # Check if the input has the correct length
            break
        print("Invalid input. Please try again.")
    return stock_symbol, chart_type, time_series_function, start_date, end_date

def main(): 
    while True:
        get_user_input()
        repeat_function = input("\nWould you like to view more stock data? (y/n)\n")
        if repeat_function == "n":
            break
    #api_test()  

if __name__=="__main__": 
    main() 