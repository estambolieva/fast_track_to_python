from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import json
import urllib2

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)
app = Flask(__name__)

def getExchangeRates():
    rates = []
    response = urllib2.urlopen('http://api.fixer.io/latest')
    data = response.read()
    rdata = json.loads(data, parse_float=float)

    rates.append(rdata['rates']['AUD'])
    rates.append(rdata['rates']['GBP'])
    rates.append(rdata['rates']['JPY'])
    rates.append(rdata['rates']['USD'])
    rates.append(rdata['rates']['BGN'])
    rates.append(rdata['rates']['BRL'])
    rates.append(rdata['rates']['CAD'])
    rates.append(rdata['rates']['RUB'])
    rates.append(rdata['rates']['NZD'])
    rates.append(rdata['rates']['HKD'])
    return rates


@app.route("/")
def index():
    rates = getExchangeRates()
    return render_template('rates.html', **locals())


@app.route("/hello")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5080)