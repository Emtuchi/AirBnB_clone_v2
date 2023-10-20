#!/usr/bin/python3
"""Start a flask web app
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes = False)
def hello_HBNB():
    """Return string when route queried
       using curl
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
