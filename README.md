This app is written in Flask. To start the app, run:

		FLASK_APP=trackmytour-rss.py FLASK_ENV=development flask run

A file called `localsettings.py` is required, and has information about the
project that should not get checked in.

		TRACKMYTOUR_URL='https://...'
