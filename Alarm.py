import os
import random
import webbrowser
from time import strftime, localtime, sleep
import urllib.request
import lxml.html


# Writes youtube video urls to YT.txt
def write_vids():
    
    connection = urllib.request.urlopen('https://www.youtube.com/music')
    dom = lxml.html.fromstring(connection.read())
    if os.path.exists('YT.txt'):
        
        os.remove('YT.txt')
    f = open('YT.txt', 'x')
    for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
    
        if '/watch?v=' in link:
            
            f.write('https://youtube.com/' + link + "\n")
    f.close()


# Waits for time to approach alarm time
def alarm_function(alarm_time):

    system_time = strftime("%H:%M", localtime())
    
    time_to_sleep = (int(alarm_time[:2]) % int(system_time[:2]) * 3600) + 
    sleep( int(alarm_time[:2]) * 3600 + int(strftime('%M') )

    # Activates alarm
    if strftime("%H:%M", localtime()) == alarm_time:
        print("The time is now " + system_time + "\nTime to wake up!")

    # Plays video from YT.txt file
    f_lines = open('YT.txt', 'r').read().splitlines()
    current_line = random.choice(f_lines)
    webbrowser.open_new_tab(current_line)
    exit()


def main():
    
    alarm_time = input("What time do you want to wake up?\nExample: 06:30\n>   ")
    alarm_function(alarm_time)  


if __name__ == '__main__':
          
    main()


