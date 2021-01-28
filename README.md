# Bushra: Good News

Source code for [Bushra](https://bushra.com.bd) backend, which scrapes and checks for negativity in online news portals.
The backend is built using Django, and Django Rest Framework. It scrapes news from The Daily Star, and checks their
sentiment using `vaderSentiment` package. MongoDB Atlas is used for the production database, and SQLite3 for testing.

To run the code, install all the requirements in `requirements.txt` file in a python virtual environment, and create
a `.env` file stating the followings:

```
SECRET_KEY=<add a secret key>
DEBUG=True/False
DB_USER=<mongodb database user>
DB_PWD=<mongodb database password>
```

The `scrape` command need to run in order to collect news from newspapers (currently only The Daily Star) and save to
the database. The command can be run using `python manage.py scrape`.