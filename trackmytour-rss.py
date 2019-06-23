from flask import Flask, render_template

import csv


app = Flask(__name__)


'''
The items in each row of the trackmytour csv are:
0: 'Map',
1: 'ID',
2: 'Waypoint Type',
3: 'Weather',
4: 'Local Time',
5: 'GMT Time',
6: 'Time Zone',
7: 'Latitude',
8: 'Longitude',
9: 'Comment',
10: 'URL',
11: 'Image1',
12: 'Image2',
13: 'Image3',
14: 'Image4',
15: 'Image5',
16: 'Image6'
'''

@app.route("/")
def index():
    with open('data.csv') as csv_file:
        parsed_csv = csv.reader(csv_file)

        data = []

        for row in parsed_csv:
            data.append({
                'url': row[10],
                'title': '{}: {}'.format(row[4], row[2]),
                'comment': row[9],
                'date': row[4],
                'image': row[11],
            })

        # the first item in the row is the csv headers, so remove it
        data.pop(0)

        return render_template('index.xml', data=data)
