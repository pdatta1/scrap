from flask_login import UserMixin

from src.__init__ import scrap_database


class User(UserMixin, scrap_database.Model):

    id = scrap_database.Column(scrap_database.Integer, primary_key=True)
    username = scrap_database.Column(scrap_database.String(100))
    password = scrap_database.Column(scrap_database.String(100))
    email_address = scrap_database.Column(scrap_database.String(100), unique=True)



