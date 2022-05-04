# """
# Create_ics.py tests
# """
# import db.ics.create_ics as ci
#
#
# organizer = input("Enter organizer name: ")
# title = input("Enter event title: ")
# desc = input("Enter event description: ")
# start = input("Enter start time (20010101 00:00:00): ")
# end = input("Enter end time (20010101 00:00:00): ")
# attendees = input("Enter Attendees ('John' or 'mike, lola, etc' or 'none'): ")
# location = input("Enter Location: ")
#
# test_event = ci.create_event(organizer, title, start, end, desc, attendees, location)
#
# test_cal = ci.add_to_cal(test_event, 'test_calendar.ics')
#
# print("********      updated calendar file     ********\n")
# print(test_cal)
# print("\n")