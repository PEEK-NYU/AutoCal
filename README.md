# PEEK ~ (Paul, Ethan, Elizabeth, Kora)
#### This is the main repository of our Software Engineering project as part of CS-UY 4513 section C.
![](https://app.travis-ci.com/PEEK-NYU/PEEK.svg?branch=main)

#### HEROKU:  https://peek-nyu.herokuapp.com/
#### TRAVIS:  https://app.travis-ci.com/github/PEEK-NYU/PEEK

## Project Idea:
* A website that aids users in scheduling events. Website pulls data from Google Calendar and suggests the best time for an event.
* Story: User queries software for the best time(s) to study for an exam next week => Website loads user's google calendar data and returns some suggested time slots compatible with the user's schedule => User selects one and the server automatically adds event to Google Calendar using Google's Calendar API. Users can also add breaks for when they want no events added for that time period.
* Over time, the system learns the user's prefered time slot for various events.
* Users can log in with their Google account for ease of use 
 
## Requirements:
**Database** 
(note: for simplicity, all ints are positive where 0 represents an uninitialized value.)

User
* username (string)  //unique database key
* password (string)
* google_key (string)
* profile_pic_url (string)

Event
* event_id (string) // unique database key
* eventname (string)
* location (string)
* start_time (int)
* end_time (int)
* owner (username: string)
* break (bool)

**Create**
1. Users can create an account with a password, and username (must be unique).
2. Users can create a break during which no events will be scheduled. The user would specify a given time period for the break and name the break.
3. Users can import events from their Google Calendar. These events passed in from Google Calendar have a name, start_time, end_time, and location.
4. Users can add an event with an eventname (required), start_time (required), end_time (required), and location (optional) passed by the user.

**Read**
1. Users can get multiple scheduled events.
2. Users can get a specific event given an event ID.
3. Users can get a list of suggested times for a given time duration.
4. Users can get their user info.
5. Users can get a break.
6. Users can get all breaks.
7. Users can get both scheduled breaks and scheduled events.
8. Get a list of users

**Update**
1. Users can change an event's properties.
2. Users can add a suggested time or a custom time to an existing event.
3. Users can change their password.
4. Users can update their account to add/modify their linked Google Calendar account.
5. Users can update the breaks.

**Delete**
1. Users can delete a given event.
2. Users can delete a given break.
3. Users can delete their account.

## Design:

**Create**
1. `/create_user` Fulfills requirement 1 of Create. Users can create an account by passing a password (required), profile_pic_url (optional) and username (required). Users will have all of the above data sent, stored in the database. Returns a success message + username if it works.
2. `/create_break` Fulfills requirement 2 of Create. Users can create a break time event during which no events will be scheduled. A username (required for owner field), eventname (required), start_time (required), and end_time (required) passed by the user. Events will have all of the above data sent in, stored in the database. Returns a success message + eventname if it works.
3. `/import_events/<eventname>` Fulfills requirement 3 of Create. Users can import events from their Google Calendar. The user sends a request with start_time (required) and end_time (required) and their username(required). The API server uses the user's Google API key stored in the database to get the events from Google Calendar and add to the user calendar. These events passed in from Google Calendar have an eventname(required (required), end_time (required), owner (required) and location (optional). Returns a success message and the imported events if it works.
4. `/create_event/<eventname>` Fulfills requirement 4 of Create. Users can add an event. These events have a username(required for owner field), eventname (required), start_time (optional), end_time (optional), and location (optional) passed by the user. Users will have all of the above data sent in, stored in the database.

**Read**
1. `/get_events/<username>`. Fulfills requirement 1 of Read. Users can get all scheduled events. The users must pass in a username (required). It returns a list of the event_id (required), eventname (required), start_time (required), end_time (required), and location (optional) for the events.
2. `/get_event/<event_id>` Fulfills requirement 2 of Read. Users can get a specific event. Users pass in an event_id (required). The result will have a eventname (required), start_time (optional), end_time (optional),and location (optional).
3. `/get_times/<username>` Fulfills requirement 3 of Read. Users can get a list of suggested times given a duration. Users pass in a username (required) and duration(required). The result is an list of start_time (required) and end_time(required). These times can later be used with update_event to use the chosen suggested time.
4. `/get_user/<username>` Fulfills requirement 4 of Read. Users can get their user info. Users pass in their username (required). Returns a username (required), and rofile_pic_url (optional). Does not return a password for security reasons.
5. `/get_break/<event_id>` Fulfills requirement 5 of Read. Users can get a specific break. Users pass in an event_id (required). The result will have a eventname (required), start_time (optional), and end_time (optional).
6. `/get_breaks/<username>` Fulfills requirement 6 of Read. Users can get all breaks. The users must pass in a username (required). The result will have an list of breaks with each having event_id (required), eventname (required), start_time (optional), and end_time (optional).
7. `/get_calendar/<username>`  Fulfills requirement 7 of Read. Users can get all breaks and events. The users must pass in a username (required). The result will have an list of events/breaks with each having event_id (required), eventname (required), location (optional), start_time (optional), end_time (optional), and break (required)
8. `/get_users/` Fulfills requirement 8 of Read. Get a list of usernames (required) back.

**Update**

1. `/update_event/<event_id>` Fulfills requirement 1 and 2 of Update.  Users can change an event's properties. The event is specified with event_id (required). User can specify an eventname (optional), start_time (optional), end_time (optional), and location (optional) to change.
2. `/update_password/<username>` Fulfills requirement 3 of Update. Users can change their password. Users pass in their existing_password (required) and new_password (required) and a username (required). Returns a message if successfully changed. Returns a success message + username if it works.
6. `/update_google/<username>` Fulfills requirement 5 of Update. Users can add or update their linked Google Calendar account. Users pass in the google_key (required) and a username (required). Returns a message if successfully changed. Returns a success message + username if it works.
7. `/update_break/<event_id>` Fulfills requirement 6 of Update. Users can update their break times. The break is specified with event_id (required). User can specify an eventname (optional), start_time (optional), end_time (optional), and location (optional) to change.

**Delete**
1. `/delete_event/<event_id>` Fulfills requirement 1 of Delete. Users can delete a given event using an event_id. Users pass in an event_id (required). Returns a success message + event_id if it works.
2. `/delete_break/<event_id>` Fulfills requirement 2 of Delete. Users can delete a given break using an event_id. Users pass in a event_id (required). Returns a success message + event_id if it works.
3. `/delete_user/<username>` Fulfills requirement 2 and 3 of Delete. Users can delete a given user using a user ID. Users pass in a username (required). Returns a success message + username if it works.

**Important: all items passed into REST not in the URL are in the body of the request**
 
## Organization Founders:
#### Kora Hughes
#### Elizabeth Akindeko
#### Ethan Philpott
#### Shaoxuan Liu

## More Links:
#### Team Ref: https://docs.google.com/spreadsheets/d/1glCAWIw6jaU5CnT3hGBCVzhFlsXHqffca_ndXOUfIwY/edit#gid=0
#### Template Ref: https://github.com/gcallah/demo-repo2
#### Previous Ref: https://github.com/AlphaError/swe-demo/tree/483d66b752659eeca268a26512faefc57851544c
