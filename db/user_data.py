"""
This file will manage interactions with the user and their data

Sample of User Architecture for Refrence:
{
  "_id": {
    "username": "Fake User",
    "password": "123",
    "email": "fakemail@nyu.edu"
  }
}
"""

import os

import db.db_connect as dbc
import db.event_data.py as edata

import random
import string

DEMO_HOME = os.environ["DEMO_HOME"]
GET_USERS = "user_data"  # Currently the only Collection in AutoCalDB (Autocal's database)
USERS = "_id"
UNAME = "username"
PW = "password"
EM = "emails"

# def of return vars: global ref in other _data.py files
OK = 0
NOT_FOUND = 1
DUPLICATE = 2

client = dbc.get_client()
if client is None:
    print("Failed to connect to MongoDB.")
    exit(1)


def get_all_users():  # Note: name change
    """
    A function to return a hashmap of all users.
    """
    # TODO: double-check
    return dbc.fetch_all_as_dict(GET_USERS, USERS)


def get_user(uid):
    """
    A function to get all a user's info given its user id
    """
    curr_users = get_all_users()
    return curr_users[uid]


def find_user(keyword):
    """
    A function to return a list of users with a username keyword
    """
    curr_users = get_all_users()
    user_list = {}
    for uid, user_info in curr_users.items():
        if keyword in user_info[UNAME]:
            user_list[uid] = user_info
    return user_list


def generate_uid():
    """
    A function that generates a random _user_id key
    https://stackoverflow.com/questions/2257441/
    random-string-generation-with-upper-case-letters-and-digits/2257449
    """
    # TODO: replace with more reliable method
    curr_users = get_all_users()
    new_uid = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=10))
    if new_uid in curr_users.keys():
        return generate_uid()  # recursively make sure no repeat uid's
    return new_uid


def add_user(username, password):
    """
    Add a user to the database using username & password
    """
    # TODO: add functionality to update a user's info/pw
    new_user = {}
    new_uid = generate_uid()
    new_user[new_uid] = {UNAME: username, PW: password}
    dbc.insert_doc(GET_USERS, new_user)
    return OK


def log_in(username, password):
    """
    Returns uid given a user's username and password
    """
    curr_users = get_all_users()
    for uid, info in curr_users.items():
        if info[UNAME] == username and info[PW] == password:
            return uid
    return NOT_FOUND


def user_exists(uid):
    """
    A function that checks if a user exists
    """
    curr_users = get_all_users()
    if uid in curr_users.keys():
        return OK
    return NOT_FOUND


def del_user(uid):
    """ deletes a user and all related events """
    # curr_users = get_all_users()
    if user_exists(uid) is NOT_FOUND:
        return NOT_FOUND
    dbc.del_one(GET_USERS, filters={USERS: uid})
    edata.del_event_by_user(uid)
    return OK


def get_emails():
    """
    A function to return a list of all emails.
    """
    return dbc.fetch_all(GET_USERS, EM)
    # Note: USER_DATA previously refrenced


def email_exists(email):
    """
    returns True if email exists
    """
    rec = dbc.fetch_one(GET_USERS, filters={EM: email})
    print(f"{rec=}")
    if rec is not None:
        return OK
    return NOT_FOUND
