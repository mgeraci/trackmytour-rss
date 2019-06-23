from flask import Flask, render_template

import csv


app = Flask(__name__)


@app.route("/")
def index():
    with open('data.csv') as csv_file:
        parsed_csv = csv.reader(csv_file)

        data = []

        for row in parsed_csv:
            print row
            data.append({
                'map': row[0],
                'date': row[4],
            })

        # the first item in the row is the csv headers, so remove it
        data.pop(0)

        return render_template('index.xml', data=data)
