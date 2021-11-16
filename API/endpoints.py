"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from http import HTTPStatus
from flask import Flask
from flask_restx import Resource, Api
import werkzeug.exceptions as wz

import db.db as db

app = Flask(__name__)
api = Api(app)

WORKING_MSG = "I'm working!"
WORKING_VAL = "\\(^-^)/"


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
        Returns a list of all chat events.
        """
        events = db.get_events()
        if events is None:
            raise (wz.NotFound("Chat event db not found."))
        else:
            return events


@api.route('/create_event/<eventname>')
class CreateEvent(Resource):
    """
    This class supports adding a chat event.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    @api.response(HTTPStatus.NOT_ACCEPTABLE, 'A duplicate key')
    def create(self, eventname):
        """
        This method adds a event to the event db.
        """
        ret = db.add_event(eventname)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound("Chat event db not found."))
        elif ret == db.DUPLICATE:
            raise (wz.NotAcceptable("Chat event name already exists."))


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
    This class supports adding a user to the chat event.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    @api.response(HTTPStatus.NOT_ACCEPTABLE, 'A duplicate key')
    def create(self, username):
        """
        This method adds a user to the user database.
        """
        ret = db.add_user(username)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound("User db not found."))
        elif ret == db.DUPLICATE:
            raise (wz.NotAcceptable("User name already exists."))
        return f"{username} added."
