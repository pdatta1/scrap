from flask import Flask, flash, request, render_template, url_for, session, redirect, Blueprint
from flask_login import login_required, current_user
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

main = Blueprint('main', __name__)


@main.route('/')
def index():
    sndmap = Map(identifier="sndmap", lat=37.4419, lng=-122.1419,markers=[
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
             'lat': 37.4419,
             'lng': -122.1419,
             'infobox': "<b>Hello World</b>"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
             'lat': 37.4300,
             'lng': -122.1400,
             'infobox': "<b>Hello World from other place</b>"
          }
        ])

    return render_template('index.html',  sndmap=sndmap)


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', username=current_user.username)


@main.route('/aboutus')
def aboutus():
    return 'About US'
