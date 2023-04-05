from flask import Flask, render_template
import json
import requests
from flask_bootstrap import Bootstrap
import os
from dotenv import load_dotenv

load_dotenv()
bootstrap = Bootstrap()
app = Flask(__name__)
bootstrap.init_app(app)


@app.route('/')
def random_quote():
    '''
    A function that requests for random quotes.

    Args:
        category & count
    '''

    url = "https://famous-quotes4.p.rapidapi.com/random"

    querystring = {"category":"all","count":"12"}

    headers = {
        "X-RapidAPI-Key":  os.environ.get('API_KEY'),
        "X-RapidAPI-Host": "famous-quotes4.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data =response.text
    dict = json.loads(data)

    cat_url = "https://famous-quotes4.p.rapidapi.com/"
    

    cat_response = requests.request("GET", cat_url, headers=headers)
    data2 =cat_response.text
    dict2 = json.loads(data2)
    return render_template('home.html', quotes = dict, items = dict2)

@app.route("/categories")
def list_categories():
    '''
    A function that requests for all quotes categories.

    Args:
        all & count
    '''

    url = "https://famous-quotes4.p.rapidapi.com/random"

    querystring = {"category":"all","count":"12"}

    headers = {
        "X-RapidAPI-Key":  os.environ.get('API_KEY'),
        "X-RapidAPI-Host": "famous-quotes4.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data =response.text
    dict = json.loads(data)

    cat_url = "https://famous-quotes4.p.rapidapi.com/"
    

    cat_response = requests.request("GET", cat_url, headers=headers)
    data2 =cat_response.text
    dict2 = json.loads(data2)
    return render_template('home.html', quotes = dict, items = dict2)


@app.route('/categories/<query>')
def select_categories(query):
    '''
    A function that sends requests for the quote categories.

    Args:
        category
    '''


    url = "https://famous-quotes4.p.rapidapi.com/random"

    querystring = {"category":"{}".format(query),"count":"12"}

    headers = {
        "X-RapidAPI-Key":  os.environ.get('API_KEY'),
        "X-RapidAPI-Host": "famous-quotes4.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data =response.text
    dict = json.loads(data)

    cat_url = "https://famous-quotes4.p.rapidapi.com/"
    

    cat_response = requests.request("GET", cat_url, headers=headers)
    data2 =cat_response.text
    dict2 = json.loads(data2)
    return render_template('home.html', quotes = dict, items = dict2)


if __name__ == '__main__':
    app.run(debug=True)