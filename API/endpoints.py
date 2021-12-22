"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from http import HTTPStatus
from flask import Flask
from flask_restx import Resource, Api
import werkzeug.exceptions as wz
import db.data as db

app = Flask(__name__)
api = Api(app)

WORKING_MSG = "I'm working!"
WORKING_VAL = "\(^-^)/"

# Done
@api.route('/endpoints')
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

# Done
@api.route('/test')
class AppTest(Resource):
    """
    The purpose of the HelloWorld class is to have a simple test to see if the
    app is working at all.
    """
    def get(self):
        """
        A trivial endpoint to see if the server is running.
        It just answers with "hello world."
        """
        return {WORKING_MSG: WORKING_VAL}

# Done
@api.route('/list_events')
class ListEvents(Resource):
    """
    This endpoint returns a list of all events.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self):
        """
        Returns a list of all events.
        """
        events = db.get_events()
        if events is None:
            raise (wz.NotFound("Event db not found."))
        else:
            return events


# Done
@api.route('/create_event/<username>/<eventname>') 
class CreateEvent(Resource):
    """
    This class supports adding an event.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    @api.response(HTTPStatus.NOT_ACCEPTABLE, 'A duplicate key')
    def post(self, username, eventname):
        """
        This method adds an event
        """
        ret = db.add_event(eventname, "370 Jay", 1640146943, 1640147053, "This is a test event", username, [username])
        #TODO Fix not found
        if ret == db.NOT_FOUND:
            raise (wz.NotFound("Event db not found."))
        return f"{eventname} added. id: {ret['id']}"

# Done
@api.route('/events/delete/<event_id>')
class DeleteEvent(Resource):
    """
    This class enables deleting an event.
    While 'Forbidden` is a possible return value, we have not yet implemented
    a user privileges section, so it isn't used yet.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    @api.response(HTTPStatus.FORBIDDEN,
                  'Only the owner of a event can delete it.')
    def post(self, event_id):
        """
        This method deletes a event from the event db.
        """
        ret = db.del_event(event_id)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound(f"Event {event_id} not found."))
        else:
            return f"{event_id} deleted."


# Done
@api.route('/get_users')
class GetUsers(Resource):
    """
    This endpoint returns a list of all users.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self):
        """
        Returns a list of all users.
        """
        users = db.get_users()
        if users is None:
            raise (wz.NotFound("User db not found."))
        else:
            return users

# Done
@api.route('/create_user/<username>')
class CreateUser(Resource):
    """
    This class supports adding a user to the app
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    @api.response(HTTPStatus.NOT_ACCEPTABLE, 'A duplicate key')
    def post(self, username):
        """
        This method adds a user to the app
        """
        ret = db.add_user(username)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound("User db not found."))
        elif ret == db.DUPLICATE:
            raise (wz.NotAcceptable("User name already exists."))
        return f"{username} added."

# Done
@api.route('/users/delete/<username>')
class DeleteUser(Resource):
    """
    This class enables deleting a user
    While 'Forbidden` is a possible return value, we have not yet implemented
    a user privileges section, so it isn't used yet.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    @api.response(HTTPStatus.FORBIDDEN, 'A user can only delete themselves.')
    def post(self, username):
        """
        This method deletes a user from the user db.
        """
        ret = db.del_user(username)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound(f"Username {username} not found."))
        else:
            return f"{username} deleted."

@api.route('/list_breaks')
class ListBreaks(Resource):
    """
    This endpoint returns a list of all breaks.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self):
        """
        Returns a list of all breaks.
        """
        events = db.get_breaks()
        if events is None:
            raise (wz.NotFound("Event db not found."))
        else:
            return events

# Done
@api.route('/create_break/<username>/<breakname>') 
class CreateBreak(Resource):
    """
    This class supports adding a break.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    @api.response(HTTPStatus.NOT_ACCEPTABLE, 'A duplicate key')
    def post(self, username, breakname):
        """
        This method adds a break
        """
        ret = db.add_break(breakname, 1640146943, 1640147053, username)
        #TODO Fix not found
        if ret == db.NOT_FOUND:
            raise (wz.NotFound("Event db not found."))
        return f"{breakname} added. id: {ret['id']}"


@api.route('/breaks/delete/<eventname>')
class DeleteBreak (Resource):
    """
    This class enables deleting a break.
    While 'Forbidden` is a possible return value, we have not yet implemented
    a user privileges section, so it isn't used yet.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    @api.response(HTTPStatus.FORBIDDEN,
                  'Only the owner of a event can delete it.')
    def post(self, eventname):
        """
        This method deletes a break from the break db.
        """
        ret = db.del_break(eventname)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound(f"Break {eventname} not found."))
        else:
            return f"{eventname} deleted."