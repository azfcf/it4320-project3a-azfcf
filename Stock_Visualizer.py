from API_Functions import api_call
import csv

from Graphing_functions import filter_json_data, generate_chart, render_chart_in_browser, parse_date_string
import datetime

from flask import Flask, render_template, request, url_for, flash, redirect, abort


# make a Flask application object called app
app = Flask(__name__)
app.config["DEBUG"] = True

#flash  the secret key to secure sessions
app.config['SECRET_KEY'] = 'your secret key'
    
# if os.path.exists('chart.svg'):
#     os.remove('chart.svg')

@app.route('/', methods=('GET', 'POST'))
def index():
    chart = None
    today = datetime.date.today().strftime("%Y-%m-%d")

    symbols = []

    with open('stocks.csv', mode = 'r') as file:
        stocksFile = csv.reader(file)
        next(stocksFile)
        for lines in stocksFile:
            symbols.append({"symbol": lines[0], "name":lines[1]})

    if request.method == 'POST':
        symbol = request.form['symbol']
        chart_type = request.form['charttype']
        timeseries = request.form['timeseries']
        start_date = parse_date_string(request.form['startdate'])
        end_date = parse_date_string(request.form['enddate'])

        if start_date > end_date:
            flash("Start date cannot be later than the end date.")
        else:
            json_data = api_call(symbol, timeseries, start_date)

            if json_data:
                #filter the JSON data based on the given start_date and end_date
                filtered_data = filter_json_data(json_data, start_date, end_date)
                
                if filtered_data:
                    chart = generate_chart(filtered_data, chart_type, symbol, start_date, end_date)
                else:
                    flash("No data found within the specified date range.")
            else:
                flash("No data found for specified input.")

    return render_template('index.html', symbols=symbols, today=today, chart=chart)


app.run(host="0.0.0.0")