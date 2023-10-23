#!/usr/bin/python3
"""starts web app"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/states_list')
def states():
    """display html of states"""
    path = '7-states_list.html'
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda name: state.name)
    return render_template

@app.teardown_appcontext
def app_teardown(arg=None):
    '''clean up'''
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
