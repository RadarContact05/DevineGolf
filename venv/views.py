from flask import Blueprint, redirect, url_for
from flask import render_template

views = Blueprint(__name__, "")


@views.route("/")
def home():
    return render_template("index.html")

@views.route("/produkter")
def produkter():
    return render_template("produkter.html")

@views.route("/om_oss")
def om_oss():
    return render_template("om oss.html")

@views.route("/nyheter")
def nyheter():
    return render_template("nyheter.html")

@views.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")

