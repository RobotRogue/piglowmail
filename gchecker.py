#!/usr/bin/env python

#Original code found on Adafruit.com @ https://learn.adafruit.com/raspberry-pi-e-mail-notifier-using-leds/overview
#Feel free to hard-code your username and password instead of using raw_input
#Thank you for checking out my code! https://github.com/RobotRogue

import time
from PyGlow import PyGlow
from imapclient import IMAPClient
import getpass #Info on getpass here: https://docs.python.org/2/library/getpass.html

DEBUG = True # Set DEBUG to False if you want nothing logged to the console.

HOSTNAME = 'imap.gmail.com'
USERNAME = raw_input('Enter your username: ') # Your GMAIL username - leave out the @gmail.com portion.
PASSWORD = getpass.getpass('Enter your password: ') # Your GMAIL password - This is plain text. If someone can see this file, they can see your password.
MAILBOX = 'Inbox' # Which mailbox the job checks. By default leave it to Inbox, unless you want it to check another folder.

NEWMAIL_OFFSET = 0   # Count in Inbox. If you leave unread in your inbox a lot, set this value to above 0.
MAIL_CHECK_FREQ = 60 # This value is in seconds

# PyGlow Global Variables:
b = 128
s = 1000
pyglow = PyGlow(brightness=int(b), speed=int(s), pulse=True) #pulse_dir=BOTH might have to be pulse_dir="BOTH"... if errors are thrown.

def pulseRed():
    #while True:
    for x in range(0,59): #better way to loop?
        pyglow.color(6)

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
        pulseRed()
        print('This is where your PiGlow would start to pulse red.')
    else:
        pyglow.all(0) #shuts off all LEDs
        print('Your PiGlow should not be blinking right now.')

    #time.sleep(MAIL_CHECK_FREQ)
    #is time.sleep still needed since I used a for loop in the pulseRed function?

if __name__ == '__main__':
    try:
        print 'Press Ctrl-C to quit.'
        while True:
            loop()
    finally:
        pyglow.all(0) #Kills all LEDs if you Ctrl-C the program.
        print('Here we shut off all LEDs.')


# Notes:
# Changed on 12/22/15 -- changed While loop to a For loop.
# Changed on 12/22/15 -- commented out time.sleep(MAIL_CHECK_FREQ) because I am using a For loop in the pulseRed function.
# The thought on the above changes is that the For loop will pulse the PiGlow 60 times @ 1000ms/pulse, which would make that 60 seconds.
# The earlier incarnation has "MAIL_CHECK_FREQ" set to 60 seconds... so by removing that time.sleep, and replacing it with the For loop...
# That should effectively do the same thing. Reason for doing this is because I used a While loop in the pulseRed function which locked
# The whole damn thing into an infinite loop, so the program only checked mail once and never again.
# Needs testing -- if it passes, I'll clean up the code.
