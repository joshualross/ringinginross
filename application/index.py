from __future__ import absolute_import

from bottle import error, post, request, response, route, TEMPLATE_PATH, view

from application import BASE_DIR
from application.lib.logging import Logger
from application.service import RSVPService

TEMPLATE_PATH.append(BASE_DIR + '/views')


@route('/')
@view('index')
def index():
    return {}


@post('/lookup')
def lookup():
    """Lookup user name to ensure they are on the guest list."""
    first_name = request.forms.get('first_name')
    last_name = request.forms.get('last_name')
    if not first_name or not last_name:
        Logger.warn('Invalid parameters')
        response.status = 400
        return {'message': 'invalid parameters'}

    # lookup name in db, return either error or signup uuid
    guest_uuid = RSVPService.search_by_name(request.forms.get('first_name'), request.forms.get('last_name'))
    # guest not found
    if not guest_uuid:
        Logger.warn('Guest not found in registry')
        response.status = 401
        return {'message': 'guest not found'}

    guest = RSVPService.fetch(guest_uuid)
    return {'guest': guest.dump()}


@post('/rsvp')
def rsvp():
    return {'message': 'OK'}


@error(404)
def error404():
    return {}
