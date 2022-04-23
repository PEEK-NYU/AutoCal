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


"""
