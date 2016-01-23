from __future__ import absolute_import

from bottle import post, response, route, TEMPLATE_PATH, view

TEMPLATE_PATH.append('/home/ringingi/ringinginross/application/views')
 
@route('/')
@view('index')
def index():
    return {}

#
@post('/lookup')
def lookup():
    # lookup name in db, return either error or signup uuid


    # guest not found
    response.status = 401
    return {'message': 'guest not found'}


@post('/rsvp')
def rsvp():

    return {'message': 'OK'}

# @route('/hello/<name>')
# def hello(name='World'):
#     return template('<b>Hello {{name}}</b>!', name=name)

# @route('/assets/<filepath:path>')
# def serve_assets(filepath):
#     return static_file(filepath, root='/home/ringingi/ringinginross/application/views/assets/')
#
# @route('/images/<filepath:path>')
# def server_images(filepath):
#     return filepath
#     # return static_file(filepath, root='/home/ringingi/ringinginross/application/views/images/')
