# THE BELOW section is the notifier

#Original creators code found here: http://null-byte.wonderhowto.com/how-to/make-gmail-notifier-python-0132845/
#import sys, feedparser, PyGlow, parser2, time
import sys
import feedparser
import time
import parser2


def checker():
    x=1
    parser2.mail(0)
    time.sleep(10)

while True:
    checker()

#re-run above program to infinity, every ten seconds.
#Change the "time.sleep(seconds to wait) variable if you want a longer/shorter check interval.


#Assign variables with values. Fill in your username and password
SERVER="mail.google.com"
USERNAME="YOUR.GMAIL.ADDRESS@gmail.com"
PASSWORD="YOUR PASSWORD"
PROTO="https://"
PATH="/gmail/feed/atom"
newEmail=""


#parses your account data and sends it to gmail
def mail(checker):
    email = int(feedparser.parse(
        PROTO + USERNAME + ":" + PASSWORD + "@" + SERVER + PATH
    )["feed"]["fullcount"])


#checks for mail
    if email > 0:
        newEmail = 1
    else:
        newEmail = 0


#plays sound if email present
    if newEmail==1:
         print("I'm beeping right now, I swear.")
         print("You have " + email + " emails!")
         #pyglow.color(6)
         print("Lights should totally be blinking right now too")
    else:
         pyglow.all(0) #shuts off all LEDs


#Runs after the above code, tells user how to exit program, and shuts down LEDs after close.
if __name__ == '__main__':
    try:
        print 'Press Ctrl-C to quit.'
        while True:
            loop()
    finally:
        print("Things and stuff.")
        #pyglow.all(0) #Kills all LEDs if you Ctrl-C the program.
