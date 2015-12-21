# PiGlowMail
<p><b>NOTE: Right now my master repo is a total mess, this is all very much a WIP. I plan to consolidate the whole thing into a single file when I'm done. For now, don't bother downloading this repo.</b></p>

<p>Use your <b><a href="https://shop.pimoroni.com/products/piglow" target="_blank">PiGlow hat</a></b> to notify you that you have new mail!</p>
<p>This code will check your inbox for new mail, and if it finds a new message, it will cause the red LEDs on your PiGlow hat to pulse Red, until all new emails have been read.</p>
<p>I used most of the code from Adafruit.com @ https://learn.adafruit.com/raspberry-pi-e-mail-notifier-using-leds/overview</p>

<p>Requires some libraries to work</p>
<ul>
<li>IMAPClient library: For the checking for new mail -  https://pypi.python.org/pypi/IMAPClient</li>
<li>PyGlow library: For providing pulse capability - https://github.com/benleb/PyGlow</li>
<li>If you use 2-factor auth for gmail: https://support.google.com/mail/answer/1173270?hl=en</li>
</ul>
