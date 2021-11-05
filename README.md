# PEEK ~ (Paul, Ethan, Elizabeth, Kora)
#### This is the main repository of our Software Engineering project as part of CS-UY 4513 section C.
![](https://app.travis-ci.com/PEEK-NYU/PEEK.svg?branch=main)

#### HEROKU:  https://dashboard.heroku.com/apps/peek-nyu/deploy/heroku-git
#### TRAVIS:  https://app.travis-ci.com/github/PEEK-NYU/PEEK

## Project Idea:
 -- a software that aids users in scheduling <br/>
 --- story: user queries software for the best time(s) to study for an exam next week... software loads user's google calendar data and returns some suggested time/duration slots compatible with the user's schedule along with event-creation links... <br/>
 -- takes imported google calendar data and exports google calender (either through calendar event creation links or direct editing <br/>
 --- main features include automatic scheduling suggestions <br/>
 
 ## CRUD Overview:
**Create**
* Users can insert, work, sleep, and break times
* Users can insert a week schedule in the database
* Week schedule
    * An already established schedule on one's calender for a particular week
    * That is, events with speficific times, durations, and on specific days
    * Week schedule is stored in database after confirmation

* Users can insert a new event with a duration time
* A suggested time and day for the new event is a calculated
* Calculation is based on entered data (inserted work, sleep, and break times, and already established schedule)

**Read**
* Users can search and retrieve week schedules on database
* Users can read calculated time suggestion for new events 

**Update**
* Users can modify existing week schedule data
* Users can add calculated suggested times for new events to week schedule data

**Delete**
* Users can hard or soft delee existing events on week schedules
* Users can hard or soft delete existing week schedule records from database

 
## Organization Founders:
#### Kora Hughes
#### Elizabeth Akindeko
#### Ethan Philpott
#### Shaoxuan Liu

## More Links:
#### Team Ref: https://docs.google.com/spreadsheets/d/1glCAWIw6jaU5CnT3hGBCVzhFlsXHqffca_ndXOUfIwY/edit#gid=0
#### Template Ref: https://github.com/gcallah/demo-repo2
#### Previous Ref: https://github.com/AlphaError/swe-demo/tree/483d66b752659eeca268a26512faefc57851544c
