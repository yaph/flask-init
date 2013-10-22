# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('app.cfg')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error=error), 404


@app.route('/')
def start():
    return render_template('start.html', title='My awesome flask app')


@app.route('/about/')
def about():
    return render_template('about.html', title='About my awesome flask app')


@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


if __name__ == '__main__':
    if app.instance_path.startswith('#HOME#'):
        app.run(debug=True)
    else:
        app.run()