# flask-init

A Bash script to create a Flask app skeleton for FastCGI depyloment.

## Requirements

You need a decent operating system, e. g. a flavor of Linux, that comes with or
lets you install Bash, Python and all the other packages listed below.
It most certainly will be a pain to get this working under Windows, maybe not so
much under OS X.

* git
* curl
* virtualenvwrapper
* rsync
* fabric
* the others I forgot to mention

## Installation

Clone the repo

    git clone https://github.com/yaph/flask-init.git

Create a symlink to the flask-init command, e. g.:

    ln -s `pwd`/flask-init/flask-init $HOME/bin

## Create the project's development environment

    flask-init

You will be prompted for some settings mainly used for production deployment.
Downloading and installing packages will take a few moments.

When finished change into the newly created project directory enter
`workon project_name` and run a dev server with `python app.py`

Now start writing your app.