#!/usr/bin/python
#
#      merge_ics.py:        This script will get all .ics files (iCalendar files, as
#                           specified in the RFC 2445 specification), read it and
#                           aggregate all events to a new .ics file. If one of the
#                           sourcefiles is not readable (or is not RFC 2445 compatible),
#                           it will be ignored.
# 
#      Original Author:     Thomas Deutsch <thomas@tuxpeople.org>
#      Current Maintainer:  Jeff Vogt (http://github.com/jvogt)
#
#      Version:             2.0(2015-04-17)
#       
#      License:             GPL v2
#       
#                           This program is free software; you can redistribute it and/or modify
#                           it under the terms of the GNU General Public License as published by
#                           the Free Software Foundation; either version 2 of the License, or
#                           (at your option) any later version.
#       
#                           This program is distributed in the hope that it will be useful, but
#                           WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
#                           or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
#                           for more details.
#       
#                           You should have received a copy of the GNU General Public License along
#                           with this program; if not, write to the Free Software Foundation, Inc.,
#                           51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA 
#       
#      Usage:               This script is made to be started by hand or via the php wrapper.
#                           It needs no parameters or options, but you should configure
#                           the variables in the config file before you run it ;)

from config import *
#############################
# Script:                   #
#############################

# We need some stuff
import glob, sys, datetime
from time import *

DEBUGMSG = 'Log started\n'

lt = localtime()
DEBUGMSG = DEBUGMSG + strftime("Tag/Monat/Jahr: %d/%m/%Y", lt) + '\n'
DEBUGMSG = DEBUGMSG + strftime("Stunde:Minute:Sekunde: %H:%M:%S", lt) + '\n'

DEBUGMSG = DEBUGMSG + 'import of glob and sys done\n'

# We need the iCalendar package from http://codespeak.net/icalendar/
import icalendar
from icalendar import Calendar, Event, Timezone
DEBUGMSG = DEBUGMSG + 'inport of icalendar done\n'

# Open the new calendarfile and adding the information about this script to it
newcal = Calendar()
newcal.add('prodid', '-//' + MY_NAME + '//' + MY_DOMAIN + '//')
newcal.add('version', '2.0')
newcal.add('x-wr-calname', CALENDARNAME)
DEBUGMSG = DEBUGMSG + 'new calendar started\n'

# we need to add a timezone, because some clients want it (e.g. sunbird 0.5)
tzc = icalendar.Timezone()
tzc.add('tzid', 'America/Los_Angeles')
tzc.add('x-lic-location', 'America/Los_Angeles')

tzd = icalendar.TimezoneDaylight()
tzd.add('tzname', 'PDT')
tzd.add('dtstart', datetime.datetime(1970, 3, 29, 2, 0, 0))
tzd.add('rrule', {'freq': 'yearly', 'bymonth': 3, 'byday': '2su'})
tzd.add('TZOFFSETFROM', datetime.timedelta(hours=-8))
tzd.add('TZOFFSETTO', datetime.timedelta(hours=-7))

tzs = icalendar.TimezoneStandard()
tzs.add('tzname', 'PST')
tzs.add('dtstart', datetime.datetime(1970, 10, 25, 3, 0, 0))
tzs.add('rrule', {'freq': 'yearly', 'bymonth': 11, 'byday': '1su'})
tzs.add('TZOFFSETFROM', datetime.timedelta(hours=-7))
tzs.add('TZOFFSETTO', datetime.timedelta(hours=-8))


tzd2 = icalendar.TimezoneDaylight()
tzd2.add('tzname', 'MDT')
tzd2.add('dtstart', datetime.datetime(1970, 3, 29, 2, 0, 0))
tzd2.add('rrule', {'freq': 'yearly', 'bymonth': 3, 'byday': '2su'})
tzd2.add('TZOFFSETFROM', datetime.timedelta(hours=-7))
tzd2.add('TZOFFSETTO', datetime.timedelta(hours=-6))

tzs2 = icalendar.TimezoneStandard()
tzs2.add('tzname', 'MST')
tzs2.add('dtstart', datetime.datetime(1970, 10, 25, 3, 0, 0))
tzs2.add('rrule', {'freq': 'yearly', 'bymonth': 11, 'byday': '1su'})
tzs2.add('TZOFFSETFROM', datetime.timedelta(hours=-6))
tzs2.add('TZOFFSETTO', datetime.timedelta(hours=-7))



tzd3 = icalendar.TimezoneDaylight()
tzd3.add('tzname', 'CDT')
tzd3.add('dtstart', datetime.datetime(1970, 3, 29, 2, 0, 0))
tzd3.add('rrule', {'freq': 'yearly', 'bymonth': 3, 'byday': '2su'})
tzd3.add('TZOFFSETFROM', datetime.timedelta(hours=-6))
tzd3.add('TZOFFSETTO', datetime.timedelta(hours=-5))

tzs3 = icalendar.TimezoneStandard()
tzs3.add('tzname', 'CST')
tzs3.add('dtstart', datetime.datetime(1970, 10, 25, 3, 0, 0))
tzs3.add('rrule', {'freq': 'yearly', 'bymonth': 11, 'byday': '1su'})
tzs3.add('TZOFFSETFROM', datetime.timedelta(hours=-5))
tzs3.add('TZOFFSETTO', datetime.timedelta(hours=-6))


tzd4 = icalendar.TimezoneDaylight()
tzd4.add('tzname', 'EDT')
tzd4.add('dtstart', datetime.datetime(1970, 3, 29, 2, 0, 0))
tzd4.add('rrule', {'freq': 'yearly', 'bymonth': 3, 'byday': '2su'})
tzd4.add('TZOFFSETFROM', datetime.timedelta(hours=-5))
tzd4.add('TZOFFSETTO', datetime.timedelta(hours=-4))

tzs4 = icalendar.TimezoneStandard()
tzs4.add('tzname', 'EST')
tzs4.add('dtstart', datetime.datetime(1970, 10, 25, 3, 0, 0))
tzs4.add('rrule', {'freq': 'yearly', 'bymonth': 11, 'byday': '1su'})
tzs4.add('TZOFFSETFROM', datetime.timedelta(hours=-4))
tzs4.add('TZOFFSETTO', datetime.timedelta(hours=-5))

newcal.add_component(tzc)
newcal.add_component(tzd)
newcal.add_component(tzs)
newcal.add_component(tzd2)
newcal.add_component(tzs2)
newcal.add_component(tzd3)
newcal.add_component(tzs3)
newcal.add_component(tzd4)
newcal.add_component(tzs4)

# Looping through the existing calendarfiles
for s in glob.glob(CALDIR + '*.ics'):
   try:
      # open the file and read it
      calfile = open(s,'rb')
      cal = Calendar.from_ical(calfile.read())
      # every part of the file...
      for component in cal.subcomponents:
         if component.name == 'VEVENT':
	    # ...which name is VEVENT will be added to the new file
            newcal.add_component(component)
      # close the existing file
      DEBUGMSG = DEBUGMSG + 'done with file ' + s +'\n'
      calfile.close()
   except:
      # if the file was not readable, we need a errormessage ;)
      print MY_SHORTNAME + ": Error: reading file:", sys.exc_info()[1]
      print s

# After the loop, we have all of our data and can write the file now
try:
   f = open(ICS_OUT, 'wb')
   f.write(newcal.to_ical())
   f.close()
   DEBUGMSG = DEBUGMSG + 'new calendar written\n'
except:
   print MY_SHORTNAME + ": Error: ", sys.exc_info()[1]

if DEBUG == True:
   try:
      l = open(DEBUGFILE, 'wb')
      l.write(DEBUGMSG)
      l.close()
   except:
      print MY_SHORTNAME + ": Error, unable to write log: ", sys.exc_info()[1]
# all done...
