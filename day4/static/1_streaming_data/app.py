from flask import Flask, render_template, Response, make_response

import random
import json
import pandas
import numpy as np

df = pandas.DataFrame({
    "x": [11, 28, 388, 400, 420],
    "y": np.random.rand(5)
})

d = [
    dict([
             (colname, row[i])
             for i, colname in enumerate(df.columns)
             ])
    for row in df.values
    ]
app = Flask(__name__)


@app.route('/streamdata')
def event_stream():
    # make this work :)
    make_response(d.to_json())


@app.route('/stream')
def show_basic():
    x = random.randint(0, 101)
    y = random.randint(0, 101)
    print json.dumps(d)
    return render_template("index.html", data=json.dumps(d))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')