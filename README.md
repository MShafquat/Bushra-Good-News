# Bushra: Good News

Source code for [Bushra](https://bushra.com.bd) backend, which scrapes and checks for negativity in online news portals.
The backend is built using Django, and Django Rest Framework. It scrapes news from The Daily Star, and checks their
sentiment using `vaderSentiment` package. MongoDB Atlas is used for the database.

To run the code, install all the requirements in `requirements.txt` file in a python virtual environment,
and create a `.env` file stating the followings:

```
SECRET_KEY=<add a secret key>
DEBUG=True/False
DB_USER=<mongodb database user>
DB_PWD=<mongodb database password>
```