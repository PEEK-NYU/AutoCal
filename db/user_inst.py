"""
test file to simulate how a user's instance will interact with the system...
"""
import user_data as udata

def login_attempt():
    username = "example_uname"
    password = "example_pw"
    # TODO: attach to react frontend to fill-out this method
    return username, password


def session_runtime(): # should return state
    # init
    session_in_progress = False
    curr_user = None

    # runtime
    session_in_progress = True
    query = ""
    while session_in_progress:
        # Note: print statements are temp: put in frontend, not console
        if query == "logging":
            user_data = login_attempt()
            ret = udata.log_in(user_data[0], user_data[1])
            if ret == udata.NOT_FOUND:
                print("Incorrect username and password combination..." +
                      " please try again")
            else:
                print("User", user_data[0], "successfully logged in")
                curr_user = ret
        elif query == "update":
            print(curr_user)
            return curr_user
        elif query == "quit":
            session_in_progress = False
        else:  # shows current session info for testing
            print("Session in progress... " + str(curr_user), '\r')
