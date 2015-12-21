#!/usr/bin/env python
#This is intended to be used on a Raspberry Pi with the PiGlow hat: https://shop.pimoroni.com/products/piglow
#Code found on Adafruit.com @ https://learn.adafruit.com/raspberry-pi-e-mail-notifier-using-leds/overview
#Prerequisite for PyGlow library is the SMBUS library: sudo apt-get install python-smbus
#Requires PyGlow library: git clone https://github.com/benleb/PyGlow.git
#Requires IMAPClient library: https://pypi.python.org/pypi/IMAPClient

#import PyGlow
import time
import IMAPClient

DEBUG = True # Set DEBUG to False if you want nothing logged to the console.

HOSTNAME = 'imap.gmail.com'
USERNAME = 'whiskeythedev' # Your GMAIL username - leave out the @gmail.com portion.
PASSWORD = 'c$1v1cW@s2' # Your GMAIL password - This is plain text. If someone can see this file, they can see your password.
MAILBOX = 'Inbox' # Which mailbox the job checks. By default leave it to Inbox, unless you want it to check another folder.

NEWMAIL_OFFSET = 0   # Count in Inbox. If you leave unread in your inbox a lot, set this value to above 0.
MAIL_CHECK_FREQ = 60 # This value is in seconds

# PyGlow Global Variables:
#b = 128
#s = 1000
#pyglow = PyGlow(brightness=int(b), speed=int(s), pulse=True, pulse_dir=BOTH) #pulse_dir=BOTH might have to be pulse_dir="BOTH"... if errors are thrown.

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
        print "Right now I would be turning on the RED LEDs and pulsing them"
        #pyglow.color(6)
    else:
        print "Right now I am shutting off all LEDs"
        #pyglow.all(0) #shuts off all LEDs

    time.sleep(MAIL_CHECK_FREQ)

if __name__ == '__main__':
    try:
        print 'Press Ctrl-C to quit.'
        while True:
            loop()
    finally:
        print "Hey!"
        #pyglow.all(0) #Kills all LEDs if you Ctrl-C the program.
