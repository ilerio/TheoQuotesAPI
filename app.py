#!flask/bin/python
from flask import Flask, jsonify, render_template
from theoquotes import get_quotes_tq, get_authors_tq
from words import get_words_tq
import random

app = Flask(__name__)
quotes = get_quotes_tq()
authors = get_authors_tq()
words = get_words_tq()

@app.route('/')
def index():
    return render_template('index.html');

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
Returns all quotes from a given author
"""
@app.route('/quotes_from/<string:author>')
def get_quotes_from_author(author):
    res = []
    for quote in quotes:
        if quote['author'] == author:
            res.append(quote)
    return jsonify(res)

"""
Returns a random quote
"""
@app.route('/random_quote')
def get_random_quote():
    x = random.randrange(0, (len(quotes)-1))
    return jsonify(quotes[x])

"""
Returns a random word
"""
@app.route('/random_word')
def get_random_word():
    x = random.randrange(0, (len(quotes)-1))
    return jsonify(words[x])

if __name__ == '__main__':
    app.run(debug=False)
