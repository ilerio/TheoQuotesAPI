#!flask/bin/python
from flask import Flask, jsonify
import random, urllib, sys
from theoquotes import get_quotes_tq, get_authors_tq

app = Flask(__name__)
quotes = get_quotes_tq()
authors = get_authors_tq()

@app.route('/')
def index():
    return "Hello, World!"

"""
Returns all quotes
"""
@app.route('/quotes')
def get_quotes():
    return jsonify(quotes)

"""
Returns a list of authors.
"""
@app.route('/authors')
def get_authors():
    return jsonify(authors)

"""
Return all quotes from a given author
"""
@app.route('/quotes_from/<string:author>')
def get_quotes_from_author(author):
    res = []
    for quote in quotes:
        if quote['name'] == author:
            res.append(quote)
    return jsonify(res)

"""
Return a random quote
"""
@app.route('/random')
def get_random_quote():
    x = random.randrange(0, (len(quotes)-1))
    return jsonify(quotes[x])

if __name__ == '__main__':
    app.run(debug=False)
