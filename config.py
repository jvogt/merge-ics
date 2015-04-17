#############################
# Variables:                #
#############################

# Folder, where the existing *.ics files are. The trailing slash is neccessary. This directory (and its files) must be readable for the user which runs this script
CALDIR = '/var/www/izzl.org/caltest/work/cals/'

# Name (and path) where the merged ics-file should be written. This directory and file must be writeable for the user which runs this script
ICS_OUT = '/var/www/izzl.org/caltest/work/cal.ics'

# Name of this tool
MY_NAME = 'Merged Calendar for Jeff Vogt'

# Our domain (This and MY_NAME will be printed into the new ics, as 'generator' ;) )
MY_DOMAIN = 'izzl.org'

# a short, one word name for this tool, used in errormessages as identifier
MY_SHORTNAME = 'merge_ics.py'

# The Timezone for the new file. This is here, becaus Mozilla Sunbird 0.5 want it ;). It's the general Timezone of the file. Normaly, an entry has it one timezone.
OUR_TIMEZONE = 'US/Pacific'

# Name of the new calendar
CALENDARNAME = 'Merged Calendar for Jeff Vogt'

# do we need logging?
DEBUG = True

# if DEBUG=True, where to log the data? (note: logfile (if it already exists) or directory must be writable by the user which runs this script)
DEBUGFILE = '/var/www/izzl.org/caltest/work/merge_ics.log'
