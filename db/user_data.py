"""
This file will manage interactions with the user and their data

Sample of User Architecture for Refrence:
{
  "user_id_1": {
    "username": "Fake User",
    "password": "123"
  }
}
"""

import os

import db.db_connect as dbc

import random
import string

DEMO_HOME = os.environ["DEMO_HOME"]
GET_USERS = "users"
USERS = "_user_id"
UNAME = "username"
PW = "password"

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
    return dict(dbc.fetch_all(GET_USERS))

def get_user(uid):
    """
    A function to get a user given its user id
    """
    curr_users = get_all_users()
    return curr_users[uid]

def find_user(keyword):
    """
    A function to return a list of users with a username keyword
    """
    curr_users = get_all_users()
    user_list = {}
    for key, value in curr_users.items():
        if keyword in value[UNAME]:
            user_list[key] = value
    return user_list

def generate_uid():
    """
    A function that generates a random _user_id key
    """
    curr_users = get_all_users()
    # https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits/2257449
    new_uid = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    if new_uid in curr_users.keys():
        return generate_uid()  # recursively make sure no repeat uid's
    return new_uid

def add_user(username, password):
    """
    Add a user to the database using username & password
    """
    new_user = {}
    new_uid = generate_uid()
    new_user[new_uid] = {UNAME: username, PW: password}
    dbc.insert_doc(USERS, new_user)

def del_user(uid):
    curr_users = get_all_users()
    del curr_users[uid]  # use curr_users.pop(uid) for silent
