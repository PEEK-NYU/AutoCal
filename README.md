# PEEK ~ (Paul, Ethan, Elizabeth, Kora)
#### This is the main repository of our Software Engineering project as part of CS-UY 4513 section C.
![](https://app.travis-ci.com/PEEK-NYU/PEEK.svg?branch=main)

#### HEROKU:  https://dashboard.heroku.com/apps/peek-nyu/deploy/heroku-git
#### TRAVIS:  https://app.travis-ci.com/github/PEEK-NYU/PEEK

## Project Idea:
* A website that aids users in scheduling events. Website pulls data from Google Calendar and suggests the best time for an event.
* Story: User queries software for the best time(s) to study for an exam next week => Software loads user's google calendar data and returns some suggested time/duration slots compatible with the user's schedule => Server automatically adds event to Google Calendar using Google's Calendar API. Users can also add breaks for when they want no events added for that time period
 
 ## Design

**Database** 

User
* email (string)
* name (string)
* password (string)
* google_key (string)
* user_id (string)
* array of events (if we are using nosql that is, if we use sql we don't need this)

Event
* event_id (string)
* name (string)
* location (string)
* start_time (int)
* end_time (int)
* duration (int)
* unscheduled (bool)
* user_id (string)

Break
* break_id (string)
* name (string)
* start_time (int)
* end_time (int)
* duration (int)

**Create**
1. Users can create an account with an email, password, and name.
2. Users can create a break during which no events will be scheduled. The user would specify a given time period for the break and name the break.
3. Users can import events from their Google Calendar. These events passed in from Google Calendar have a name, start_time, end_time, duration and location.
4. Users can add an event with a name (required), start_time (optional), end_time (optional), duration (required) and location (optional) passed by the user. Events without a start_time AND end_time are considered unscheduled events and will be displayed in a separate section on the side of the website.

**Read**
1. Users can get multiple scheduled events from a given time frame.
2. Users can get all unscheduled events.
3. Users can get a specific event given an event ID.
4. Users can get a list of suggested times for a given time duration.
5. Users can get their user info.
6. Users can get a break.
7. Users can get all breaks from a given time frame.
8. Users can get both scheduled breaks and scheduled events from a given time frame.

**Update**
1. Users can change an event's properties.
2. Users can add a suggested time or a custom time to an existing unscheduled event.
3. Users can change their password.
4. Users can change their email.
5. Users can change their name.
6. Users can update their account to add/modify their linked Google Calendar account.
7. Users can update the breaks.

**Delete**
1. Users can delete a given event.
2. Users can delete a given break.
3. Users can delete their account.

## CRUD

**Create**
1. `/create_user` Fulfills requirement 1 of Create. Users can create an account by passing a email (required), password (required), and name (required). Returns a success message + user_id if it works.
2. `/create_break` Fulfills requirement 2 of Create. Users can create a break time during which no events will be scheduled. The break time will have a name (required), start_time (required), end_time (required), and duration (required) passed by the user. Returns a success message + break_id if it works.
3. `/import_events` Fulfills requirement 3 of Create. Users can import events from their Google Calendar. The user sends a request with start_time (required) and end_time (required). The API server uses the user's Google API key stored in the database to get the events from Google Calendar and add to the user calendar. These events passed in from Google Calendar have a name, start_time, end_time, duration and location. Returns a success message and the imported events if it works.
4. `/create_event` Fulfills requirement 4 of Create. Users can add an event. These events have a name (required), start_time (optional), end_time (optional), duration (required) and location (optional) passed by the user. Events without a start_time AND end_time are considered unscheduled events and will be displayed in a separate section on the side of the website. Returns a success message + event_id if it works.

**Read**
1. `/get_events/<user_ID>`. Fulfills requirement 1 of Read. Users can get multiple scheduled events from a given time frame. The users must pass in a user_ID (required), start_time (required) and end_time (required). It returns a list of the event_id (required), name (required), start_time (required), end_time (required), duration (required), and location (optional) for the events.
2. `/get_unscheduled/<user_ID>` Fulfills requirement 2 of Read. Users can get all unscheduled events. Users pass in a user_ID (required). It returns an event_id (required), name (required), duration (required), and location (optional). No start_time or end_time is returned because all unscheduled events have none scheduled yet.
3. `/get_event/<event_ID>` Fulfills requirement 3 of Read. Users can get a specific event (scheduled or unscheduled). Users pass in an event_ID (required). The result will have a  event_id (required), name (required), start_time (optional), end_time (optional), duration (required), location (optional) and if it is unscheduled or not (required).
4. `/get_times/<user_ID>` Fulfills requirement 4 of Read. Users can get a list of suggested times for a given time duration. Users pass in duration (required) and a user_ID (required). The result is an array of start_time (required) and end_time(required). These times can later be used with update_event to use the chosen suggested time.
5. `/get_user/<user_ID>` Fulfills requirement 5 of Read. Users can get their user info. Users pass in their user_ID (required). Returns a user_id (required), email (required) and name (required). Does not return a password for security reasons.
6. `/get_break/<break_ID>` Fulfills requirement 6 of Read. Users can get a specific break. Users pass in an break_ID (required). The result will have a break_ID (required), name (required), start_time (optional), end_time (optional), and duration (required).
7. `/get_breaks/<user_ID>` Fulfills requirement 7 of Read. Users can get breaks from a timeframe. The users must pass in a start_time (required) and end_time (required) and a user_ID (required). The result will have an array of breaks with each having break_ID (required), name (required), start_time (optional), end_time (optional), and duration (required).
8. `/get_calendar/<user_ID>`  Fulfills requirement 8 of Read. Users can get breaks and events from a timeframe. The users must pass in a start_time (required) and end_time (required) and a user_ID (required). The result will have an array of breaks with each having break_ID (required), name (required), start_time (optional), end_time (optional), and duration (required). It also returns a list of the event_id (required), name (required), start_time (required), end_time (required), duration (required), and location (optional) for the events.

**Update**

1. `/update_event/<event_ID>` Fulfills requirement 1 and 2 of Update.  Users can change an event's properties. The event is specified with event_ID (required). User can specify a name (optional), start_time (optional), end_time (optional), duration (optional) and location (optional) to change. Note if you change duration and have a specified end_time and start_time you also must change those times. Returns a success message + event_ID if it works.
2. `/update_password/<user_ID>` Fulfills requirement 3 of Update. Users can change their password. Users pass in their existing_password (required) and new_password (required) and a user_ID (required). Returns a message if successfully changed. Returns a success message + user_ID if it works.
3. `/update_email/<user_ID>` Fulfills requirement 4 of Update. Users can change their email. Users pass in their new_email (required) and a user_ID (required). Returns a message if successfully changed. Returns a success message + user_ID if it works.
5. `/update_name/<user_ID>` Fulfills requirement 5 of Update. Users can change their name. Users pass in their new_name (required) and a user_ID (required). Returns a message if successfully changed. Returns a success message + user_ID if it works.
6. `/update_google/<user_ID>` Fulfills requirement 6 of Update. Users can add or update their linked Google Calendar account. Users pass in the google_key (required) and a user_ID (required). Returns a message if successfully changed. Returns a success message + user_ID if it works.
7. `/update_break/<break_ID>` Fulfills requirement 7 of Update. Users can update their break times. Users pass in a break_ID (required), start_time (optional), end_time (optional) to change the event. Returns a success message + user_ID if it works.

**Delete**
1. `/delete_event/<event_ID>` Fulfills requirement 1 of Delete. Users can delete a given event using an event ID. Users pass in an event_ID (required). Returns a success message + event_ID if it works.
2. `/delete_break/<break_ID>` Fulfills requirement 2 of Delete. Users can delete a given break using a break ID. Users pass in a break_ID (required). Returns a success message + break_ID if it works.
3. `/delete_user/<user_ID>` Fulfills requirement 3 of Delete. Users can delete a given user using a user ID. Users pass in a user_ID (required). Returns a success message + user_ID if it works.

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
