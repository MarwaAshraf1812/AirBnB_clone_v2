#!/usr/bin/python3
"""
Start Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close(exc):
    """Clean-up and close the session after each request"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Return state list from storage"""
    return render_template("7-states_list.html", states=storage.all(State))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
