"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from http import HTTPStatus
from flask import Flask
from flask_cors import CORS
from flask_restx import Resource, Api
import werkzeug.exceptions as wz

import db.user_data as udata
import db.event_data as edata
# import db.connect_data as cdata

import db.ics.create_ics as cal

app = Flask(__name__)
CORS(app)
api = Api(app)

test_key = 'hello'
test_value = 'world'


@api.route('/admin/hello')
class HelloWorld(Resource):
    """
    The purpose of the HelloWorld class is to have a simple test to see if the
    app is working at all.
    """
    def get(self):
        """
        A trivial endpoint to see if the server is running.
        It just answers with "{hello: world}."
        """
        return {test_key: test_value}


@api.route('/admin/endpoints')
class Endpoints(Resource):
    """
    This class will serve as live, fetchable documentation of what endpoints
    are available in the system.
    """
    @api.response(HTTPStatus.OK, 'Success')
    def get(self):
        """
        The `get()` method will return a list of available endpoints.
        """
        endpoints = sorted(rule.rule for rule in api.app.url_map.iter_rules())
        return {"Available endpoints": endpoints}


@api.route('/admin/events/get')
class ListAllEvents(Resource):
    """
    *Admin* This endpoint returns a list of all events.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self):
        """
        Returns a list of all events.
        """
        events = edata.get_all_events()
        if events is None:
            raise (wz.NotFound("Event db not found."))
        else:
            return events


@api.route('/events/get/<uid>')
class ListEvents(Resource):
    """
    This endpoint returns a list of all events associated with a given user ID.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self, uid):
        """
        Returns a list of all events associated with a given user ID..
        """
        events = edata.get_user_events(uid)
        if events is None:
            raise (wz.NotFound("Event db not found."))
        else:
            return events


@api.route('/events/get/<eid>')
class GetEvent(Resource):
    """
    This endpoint returns an event given an event ID.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self, eid):
        """
        Returns an event given an event ID.
        """
        event = edata.get_event(eid)
        if edata.event_exists(eid) == edata.NOT_FOUND:
            raise (wz.NotFound("Event not found."))
        else:
            return event  # {"TEST": event} TODO: fix


@api.route('/events/create/<uid>/<eventname>/'
           '<start_time>/<end_time>/<description>')
class CreateEvent(Resource):
    """
    This class supports creating an event
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    @api.response(HTTPStatus.NOT_ACCEPTABLE, 'A duplicate key')
    def post(self, uid, eventname, start_time, end_time, description):
        """
        This method adds an event to the event db.
        """
        ret = edata.create_event(uid, eventname, start_time,
                                 end_time, "", description)
        if ret == udata.NOT_FOUND:
            raise (wz.NotFound("Event db not found."))
        else:
            return ret


@api.route('/events/delete/<eid>/<uid>')
class DeleteEvent(Resource):
    """
    This class enables deleting an event
    While 'Forbidden` is a possible return value, we have not yet implemented
    a user privileges section, so it isn't used yet.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    @api.response(HTTPStatus.FORBIDDEN,
                  'Only the owner of a event can delete it.')
    def post(self, eid, uid):
        """
        This method deletes an event from the event db.
        """
        ret = edata.del_event(eid, uid)
        if ret == udata.NOT_FOUND:
            raise (wz.NotFound(f"Event {eid} not found."))
        else:
            return f"{eid} deleted."


@api.route('/admin/users/get')
class ListAllUsers(Resource):
    """
    This endpoint returns a list of all users.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self):
        """
        Returns a list of all users.
        """
        users = udata.get_all_users()
        if users is None:
            raise (wz.NotFound("User db not found."))
        else:
            return users


@api.route('/users/get/<uid>')
class GetUser(Resource):
    """
    This endpoint returns all information related to a user id.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self, uid):
        """
        Returns all information related to a user id.
        """
        user = udata.get_user(uid)
        if udata.user_exists(uid) == udata.NOT_FOUND:
            raise (wz.NotFound("User not found."))
        else:
            return user


@api.route('/users/login/<username>/<password>')
class Login(Resource):
    """
    This endpoint returns a user id given a user's login information
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self, username, password):
        """
        Returns a uid given a username and password
        """
        user = udata.log_in(username, password)
        if user == udata.NOT_FOUND:
            raise (wz.NotFound("User not found."))
        else:
            return user


@api.route('/users/create/<username>/<password>/<email>')
class CreateUser(Resource):
    """
    This class supports adding a user to the user database.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_ACCEPTABLE, 'Bad Inputs')
    def post(self, username, password, email=""):
        """
        This method adds a user to the user database.
        email must contain an @ symbol
        """
        ret = udata.add_user(username, password, email)
        if ret == udata.NOT_FOUND:
            raise (wz.NotAcceptable("Not suitable email: add @"))
        return ret


@api.route('/users/delete/<uid>')
class DeleteUser(Resource):
    """
    This class enables deleting a user.
    While 'Forbidden` is a possible return value, we have not yet implemented
    a user privileges section, so it isn't used yet.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    @api.response(HTTPStatus.FORBIDDEN, 'A user can only delete themselves.')
    def post(self, uid):
        """
        This method deletes a user from the user db.
        """
        ret = udata.del_user(uid)
        if ret == udata.NOT_FOUND:
            raise (wz.NotFound(f"User {uid} not found."))
        else:
            return f"{uid} deleted."


@api.route('/users/calendar/<uid>/<ics_data>')
class AddCalendar(Resource):
    """
    This class enables deleting a user.
    While 'Forbidden` is a possible return value, we have not yet implemented
    a user privileges section, so it isn't used yet.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    @api.response(HTTPStatus.FORBIDDEN, 'A user can only delete themselves.')
    def post(self, uid, ics_data):
        """
        This method deletes a user from the user db.
        """
        ret = cal.add_calendar(uid, ics_data)
        if ret == udata.NOT_FOUND:
            raise (wz.NotFound(f"User {uid} not found."))
        else:
            return f"{uid} deleted."
