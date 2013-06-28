# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error=error), 404


@app.route('/')
def start():
    return render_template('start.html', title='My awesome flask app')


@app.route('/about/')
def about():
    return render_template('about.html', title='About my awesome flask app')


if __name__ == '__main__':
    if app.instance_path.startswith('#HOME#'):
        app.run(debug=True)
    else:
        app.run()