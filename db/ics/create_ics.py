#!env python3

from icalendar import Calendar, Event, vCalAddress, vText
import pytz
from datetime import datetime
import os
from pathlib import Path

# Creating icalendar/event
event = Event()
event.add('summary', 'Python meeting about calendaring on Autocal')
event.add('dtstart', datetime(2021, 1, 12, 8, 0, 0, tzinfo=pytz.utc))
event.add('dtend', datetime(2021, 1, 12, 10, 0, 0, tzinfo=pytz.utc))
event.add('dtstamp', datetime(2021, 1, 12, 0, 10, 0, tzinfo=pytz.utc))

# Adding Organizer
organizer = vCalAddress('MAILTO:kitkatakora@kawaiiland.com')
organizer.params['cn'] = vText('Organizer')
organizer.params['role'] = vText('Kitten')
event['organizer'] = organizer

# Adding attendee
attendee = vCalAddress('MAILTO:paulfullmoon@wolves.com')
attendee.params['cn'] = vText('Wolverine')
attendee.params['ROLE'] = vText('REQ-PARTICIPANT')
event.add('attendee', attendee, encode=0)

 Adding location
event['location'] = vText('Zoom Link:https://zoom.com/123456')

# Adding events to calendar
cal = Calendar()
cal.add_component(event)

directory = str(Path(__file__).parent.parent) + "/"
# print(directory)
f = open(os.path.join(directory, 'testing.ics'), 'wb')
f.write(cal.to_ical())
f.close()

# vim: ft=python

"""
What we have here:

BEGIN:VCALENDAR
BEGIN:VEVENT
SUMMARY:Python meeting about calendaring on Autocal
DTSTART;VALUE=DATE-TIME:20220423T080000Z
DTEND;VALUE=DATE-TIME:20220423T100000Z
DTSTAMP;VALUE=DATE-TIME:20220423T001000Z
ATTENDEE;CN="Wolverine";ROLE=REQ-PARTICIPANT:MAILTO:paulfullmoon@wolves.com
LOCATION:Zoom Link:https://zoom.com/123456
ORGANIZER;CN=Organizer;ROLE=Kitten:MAILTO:kitkatakora@kawaiiland.com
END:VEVENT
END:VCALENDAR


Other Tests to check out:

# Give the week headers, each 3 letters long
print(calendar.weekheader(3))
print() # these empty prints are just for spacing. they print a blank space

# Give the integer value of what the first weekday is (Monday is 0, TUesday is 1, etc...)
print(calendar.firstweekday())
print()

# Print out the specified month
print(calendar.month(2019, 3))
print()

# Get the specified month in array form (if you don't understand the distinction, it's okay.)
print(calendar.monthcalendar(2019, 3))
print()

# Print out the specified year
print(calendar.calendar(2019))
print()

# Find out what day of the week (Mon is 0, Tue is 1, Wed is 2, etc...) the specified day is
day_of_the_week = calendar.weekday(3000, 3, 8)

# Tell us if the specified year is a leap year
is_leap = calendar.isleap(2020)
print(is_leap)
print()

# Specify how many leap days there are in the specified range of years (exclusive)
how_many_leap_days = calendar.leapdays(2000,3000)
print(how_many_leap_days)


TODO: check below, change above?
from ics import Calendar, Event
c = Calendar()
e = Event()
e.name = "My cool event"
e.begin = '2014-01-01 00:00:00'
c.events.add(e)
c.events
# [<Event 'My cool event' begin:2014-01-01 00:00:00 end:2014-01-01 00:00:01>]
with open('my.ics', 'w') as my_file:
    my_file.writelines(c)
# and it's done !

"""
