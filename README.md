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
* Users can insert a day's schedule in the database
* Day schedule
    * An already established schedule on one's calender for a particular day
    * That is, events with speficific times, durations
    * Day schedule is stored in database after confirmation

* Users can insert a new event with a duration time
* Suggested times for the new event are calculated
* Calculation is based on entered data (inserted work, sleep, and break times, and already established schedule)
    * Calculated suggested times are not saved on database unless user confirms

**Read**
* Users can search and retrieve day schedules on database
* Users can read calculated time suggestions for new events 

**Update**
* Users can modify existing day schedule data
* Users can add calculated suggested times for new events to day schedule data

**Delete**
* Users can hard or soft delete existing events on day schedules
* Users can hard or soft delete existing day schedule records from database

 
## Organization Founders:
#### Kora Hughes
#### Elizabeth Akindeko
#### Ethan Philpott
#### Shaoxuan Liu

## More Links:
#### Team Ref: https://docs.google.com/spreadsheets/d/1glCAWIw6jaU5CnT3hGBCVzhFlsXHqffca_ndXOUfIwY/edit#gid=0
#### Template Ref: https://github.com/gcallah/demo-repo2
#### Previous Ref: https://github.com/AlphaError/swe-demo/tree/483d66b752659eeca268a26512faefc57851544c
