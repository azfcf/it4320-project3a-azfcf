from API_Functions import api_test, is_date_in_range, get_user_input, filter_json_data, generate_chart, render_chart_in_browser


while True: 
    #get user input for stock symbol, chart type, time series function, start date, and end date
    stock_symbol, chart_type, time_series_function, start_date, end_date = get_user_input()
    
    #get the JSON data from the Alpha Vantage API based on user input
    json_data = api_test(stock_symbol, time_series_function)
    
    if json_data:
        #filter the JSON data based on the given start_date and end_date
        filtered_data = filter_json_data(json_data, start_date, end_date)
        
        if filtered_data:
            chart = generate_chart(filtered_data, chart_type, stock_symbol)
            render_chart_in_browser(chart)
            print(filtered_data)
        else:
            print("No data found within the specified date range.")
    
    #ask user if they want to view more stock data
    repeat_function = input("\nWould you like to view more stock data? (y/n)\n")
    if repeat_function == "n":
        break