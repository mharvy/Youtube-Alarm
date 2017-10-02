# Import libraries for alarm
import os
import random
import webbrowser
from time import strftime, localtime, sleep

# Import libraries for parsing youtube
import urllib.request
import lxml.html


# If YT file doesn't exist, create one
if not(os.path.exists('YT.txt')):
    flags = os.O_RDWR|os.O_CREAT
    f = open('YT.txt', 'x')
    f.close()


# Fill YT file with new youtube links
connection = urllib.request.urlopen('https://www.youtube.com/music')
dom = lxml.html.fromstring(connection.read())


# Writes youtube video urls to YT.txt
if os.path.exists('YT.txt'):
    os.remove('YT.txt')
f = open('YT.txt', 'x')

for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
    if '/watch?v=' in link:
        f.write('https://youtube.com/' + link + "\n")

f.close()


# Prompts user for alarm time
print('When do you want to wake up?\nExample: 06:30')
alarm_time = input("> ")


# Variable for system time
system_time = strftime("%H:%M", localtime())


# Waits for time to approach alarm time
while system_time != alarm_time:
    system_time = strftime("%H:%M", localtime())
    print("The time is now " + system_time)
    sleep(60 - int(strftime("%S")))
    system_time = strftime("%H:%M", localtime())


# Activates alarm
if strftime("%H:%M", localtime()) == alarm_time:
    print("The time is now " + system_time + "\nTime to wake up!")

    # Plays video from YT.txt file
    f_lines = open('YT.txt', 'r').read().splitlines()
    current_line = random.choice(f_lines)
    webbrowser.open_new_tab(current_line)
    exit()







