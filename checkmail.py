#!/usr/bin/env python
#Code found on Adafruit.com @ https://learn.adafruit.com/raspberry-pi-e-mail-notifier-using-leds/overview
#Requires PyGlow library: https://github.com/benleb/PyGlow
#Requires IMAPClient library (not sure if separate install required)

from imapclient import IMAPClient
from PyGlow import PyGlow
import time

DEBUG = True # Set DEBUG to False if you want nothing logged to the console.

HOSTNAME = 'imap.gmail.com'
USERNAME = 'your username here' # Your GMAIL username - leave out the @gmail.com portion.
PASSWORD = 'your password here' # Your GMAIL password - This is plain text. If someone can see this file, they can see your password.
MAILBOX = 'Inbox' # Which mailbox the job checks. By default leave it to Inbox, unless you want it to check another folder.

NEWMAIL_OFFSET = 0   # Count in Inbox. If you leave unread in your inbox a lot, set this value to above 0.
MAIL_CHECK_FREQ = 60 # This value is in seconds

# PyGlow Global Variables:
b = 128
s = 1000
pyglow = PyGlow(brightness=int(b), speed=int(s), pulse=True, pulse_dir=BOTH) #pulse_dir=BOTH might have to be pulse_dir="BOTH"... if errors are thrown.

def loop():
    server = IMAPClient(HOSTNAME, use_uid=True, ssl=True)
    server.login(USERNAME, PASSWORD)

    if DEBUG:
        print('Logging in as ' + USERNAME)
        select_info = server.select_folder(MAILBOX)
        print('%d messages in INBOX' % select_info['EXISTS'])

    folder_status = server.folder_status(MAILBOX, 'UNSEEN')
    newmails = int(folder_status['UNSEEN'])

    if DEBUG:
        print "You have", newmails, "new emails!"

    if newmails > NEWMAIL_OFFSET:
        pyglow.color(6)
    else:
        pyglow.all(0) #shuts off all LEDs

    time.sleep(MAIL_CHECK_FREQ)

if __name__ == '__main__':
    try:
        print 'Press Ctrl-C to quit.'
        while True:
            loop()
    finally:
        pyglow.all(0) #Kills all LEDs if you Ctrl-C the program.


#The PyGlow() object can accept four optional parameters:

# brightness=None - sets default brightness level (value: number from 0 and 255)
# speed=None - sets default pulsing speed in milliseconds (value: number > 0)
# pulse=None - enables pulsing by default (value: True or False)
# pulse_dir=None - sets default pulsation direction (value: UP, DOWN, BOTH)

#In order to be able to use PyGlow module, the PyGlow() class must be imported:
#from PyGlow import PyGlow

#Then it's possible to instantiate the PyGlow() object:
#pyglow = PyGlow()
