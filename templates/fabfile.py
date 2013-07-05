# -*- coding: utf-8 -*-
from fabric.api import env, local, cd, run

LOCAL_FLASK_PATH = '.'
LOCAL_PUBLIC_PATH = 'public_html/'
LOCAL_STATIC_PATH = 'static/'
LIVE_FLASK_PATH = '#PROD_PROJECT_FLASK#'
LIVE_PUBLIC_PATH = '#PROD_PROJECT_WWW#'
LIVE_STATIC_PATH = '#PROD_PROJECT_WWW#/static/'
RSYNC_EXCLUDE = '--exclude-from="rsync-exclude.txt"'
env.use_ssh_config = True


def assets():
    local('rm -rf static/gen/')
    local('scripts/assets.py')
    local('rm -rf static/.webassets-cache/')


def git():
    local('git add . && git commit -a')
    local('git push')


def dev():
    env.hosts = ['localhost']
    env.cwd = LOCAL_FLASK_PATH


def live():
    env.hosts = ['#PROD_SERVER#']
    env.cwd = LIVE_FLASK_PATH


def rsync(dir_src, dir_dst, exclude=''):
    local('rsync %s -aruvz %s hm:%s' % (exclude, dir_src, dir_dst))


def pip():
    with cd(env.cwd):
        run('workon #PROJECT_NAME#' and 'pip install -r requirements.txt')


def up():
    assets()
    rsync(LOCAL_FLASK_PATH, LIVE_FLASK_PATH, RSYNC_EXCLUDE)
    rsync(LOCAL_PUBLIC_PATH, LIVE_PUBLIC_PATH)
    rsync(LOCAL_STATIC_PATH, LIVE_STATIC_PATH)