#!/usr/bin/python3
"""Start a flask web app
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_HBNB():
    """Return string when route queried
       using curl
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
