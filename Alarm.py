import os
import random
import webbrowser
import time
import datetime
import urllib.request
import lxml.html


# Writes youtube video urls to YT.txt
def write_videos():

    connection = urllib.request.urlopen('https://www.youtube.com/music')
    dom = lxml.html.fromstring(connection.read())

    if os.path.exists('YT.txt'):

        os.remove('YT.txt')
    f = open('YT.txt', 'x')

    for link in dom.xpath('//a/@href'):  # select the url in href for all a tags(links)

        if '/watch?v=' in link:

            f.write('https://youtube.com/' + link + "\n")

    f.close()


# Waits for time to approach alarm time, then plays YT video
def alarm_function(alarm_time):

    real_alarm_time = int(alarm_time[:2]) * 3600 + int(alarm_time[3:]) * 60
    today = datetime.date.today()
    seconds_since_midnight = time.time() - time.mktime(today.timetuple())

    if real_alarm_time < time.time():  # Activates alarm after certain amount of time

        time.sleep(real_alarm_time - seconds_since_midnight)

    elif real_alarm_time > time.time():

        time.sleep(real_alarm_time - seconds_since_midnight)


# Plays video from YT.txt file
def play_video():

    f_lines = open('YT.txt', 'r').read().splitlines()
    current_line = random.choice(f_lines)
    webbrowser.open_new_tab(current_line)
    exit()


# Writes new yt file, waits until alarm_time, then plays random video
def yt_alarm(alarm_time):

    write_videos()
    alarm_function(alarm_time)
    play_video()


def main():

    alarm_time = input("What time do you want to wake up?\nExample: 06:30\n>   ")
    yt_alarm(alarm_time)


if __name__ == '__main__':

    main()
