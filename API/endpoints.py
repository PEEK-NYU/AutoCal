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


@api.route('/create_event/<eventname>') 
class CreateEvent(Resource):
    """
    This class supports adding an event.
    """
    #Paul: seems like duration is not a mandatory parameter, different from README
    #Paul: should probably name this function CreateEmptyEvent
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    @api.response(HTTPStatus.NOT_ACCEPTABLE, 'A duplicate key')
    def post(self, eventname):
        """
        This method adds an event
        """
        ret = db.add_event({"name": eventname})
        if ret == db.NOT_FOUND:
            raise (wz.NotFound("Event db not found."))
        elif ret == db.DUPLICATE:
            raise (wz.NotAcceptable("Event name already exists."))
        return f"{eventname} added."


@api.route('/events/delete/<eventname>')
class DeleteEvent(Resource):
    """
    This class enables deleting a chat room.
    While 'Forbidden` is a possible return value, we have not yet implemented
    a user privileges section, so it isn't used yet.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    @api.response(HTTPStatus.FORBIDDEN,
                  'Only the owner of a event can delete it.')
    def post(self, eventname):
        """
        This method deletes a room from the room db.
        """
        ret = db.del_event(eventname)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound(f"Event {eventname} not found."))
        else:
            return f"{eventname} deleted."


@api.route('/list_users')
class ListUsers(Resource):
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


@api.route('/users/delete/<username>')
class DeleteUser(Resource):
    """
    This class enables deleting a chat user.
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
            raise (wz.NotFound(f"Chat participant {username} not found."))
        else:
            return f"{username} deleted."


'''
UNFINISHED PROTOTYPES, PLEASE DON'T UNCOMMENT THE FOLLOWING

@api.route('/create_event/<eventname>')
class CreateEventWithDuration(Resource):
    """
    This class supports adding an event with a specific duration.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    @api.response(HTTPStatus.NOT_ACCEPTABLE, 'A duplicate key')
    def post(self, eventname, eventduration):
        """
        This method adds an event with a specific duration
        """
        ret = db.add_event({"name": eventname, "duration": eventduration})
        if ret == db.NOT_FOUND:
            raise (wz.NotFound("Event db not found."))
        elif ret == db.DUPLICATE:
            raise (wz.NotAcceptable("Event name already exists."))
        return f"{eventname} added."

@api.route('/events/update_event/<eventname>')
class SetEventDuration(Resource):
    """
    This class supports setting the duration of an event.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def post(self, eventname, eventduration):
        """
        This method sets the duration of an event.
        """
        ret = db.set_event_fields({"name": eventname, "duration": eventduration})
        if ret == db.NOT_FOUND:
            raise (wz.NotFound("Event db not found."))
        return f"{eventname} duration successfully set."
        
@api.route('/events/update_event/<eventname>')
class SetEventTime(Resource):
    """
    This class supports setting the time of an event.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def post(self, eventname, starttime, endtime):
        """
        This method sets the time of an event.
        """
        ret = db.set_event_fields({"name": eventname, "start_time": starttime, "end_time": endtime, "unscheduled": False})
        if ret == db.NOT_FOUND:
            raise (wz.NotFound("Event db not found."))
        return f"{eventname} time successfully set."
        
@api.route('/events/update_event/<eventname>')
class SetEventLocation(Resource):
    """
    This class supports setting the location of an event.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def post(self, eventname, eventlocation):
        """
        This method sets the location of an event.
        """
        ret = db.set_event_fields({"name": eventname, "location": eventlocation})
        if ret == db.NOT_FOUND:
            raise (wz.NotFound("Event db not found."))
        return f"{eventname} location successfully set."
    
@api.route('/users/update_password/<username>')
class SetUserPassword(Resource):
    """
    This class supports setting the password of a user.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def post(self, username, password):
        """
        This method sets the password of a user.
        """
        ret = db.set_event_fields({"name": username, "password": password})
        if ret == db.NOT_FOUND:
            raise (wz.NotFound("User db not found."))
        return f"{username} password successfully set."
    
@api.route('/users/update_email/<username>')
class SetUserEmail(Resource):
    """
    This class supports setting the email of a user.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def post(self, username, email):
        """
        This method sets the email of a user.
        """
        ret = db.set_event_fields({"name": username, "email": email})
        if ret == db.NOT_FOUND:
            raise (wz.NotFound("User db not found."))
        return f"{username} email successfully set."
'''