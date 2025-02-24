"""
docstring
"""

import locale
from datetime import datetime
from flask import Flask, render_template


app = Flask(__name__)
locale.setlocale(locale.LC_TIME, "")


@app.route("/")
def homepage():
    """
    docstring
    """
    the_time = datetime.now().strftime("%A, %d %b %Y %H:%M")

    # Render HTML with variable
    return render_template(
        "index.html", the_time=the_time, tema="cat", alto="600", ancho="920"
    )


@app.route("/status")
def status():
    """
    docstring
    """
    return "OK Todo"


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
