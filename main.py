from flask import Flask, Blueprint, render_template, url_for
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True, port=8000)