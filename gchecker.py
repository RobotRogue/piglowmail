#!/usr/bin/env python
#This is intended to be used on a Raspberry Pi with the PiGlow hat
#Code found on Adafruit.com @ https://learn.adafruit.com/raspberry-pi-e-mail-notifier-using-leds/overview
#Thank you for checking out my code! https://github.com/RobotRogue

import time
import PyGlow
import IMAPClient

DEBUG = True # Set DEBUG to False if you want nothing logged to the console.

HOSTNAME = 'imap.gmail.com'
USERNAME = raw_input('Enter your username: ') # Your GMAIL username - leave out the @gmail.com portion.
PASSWORD = raw_input('Enter your password: ') # Your GMAIL password - This is plain text. If someone can see this file, they can see your password.
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
        #pyglow.color(6)
        print("This is where your PiGlow would start to blink.")
    else:
        #pyglow.all(0) #shuts off all LEDs
        print("Your PiGlow should not be blinking right now.")

    time.sleep(MAIL_CHECK_FREQ)

if __name__ == '__main__':
    try:
        print 'Press Ctrl-C to quit.'
        while True:
            loop()
    finally:
        #pyglow.all(0) #Kills all LEDs if you Ctrl-C the program.
        print("Here we'd shut off all LEDs.")


# Notes:
# Create a function that will prompt user to input username, and prompt to input password
# Then have it store those as variables to pass to the check mail loop

# May also just be able to write the whole thing in such a way where when the python file is executed,
# user will have to pass in Username and Password as arguments (or parameters) at the top level.
