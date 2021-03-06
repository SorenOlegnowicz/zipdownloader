import os
import subprocess as sub
from sys import argv

# unpacks command line arguments
try:
    lesson_number = argv[1]
    directory = argv[2]
except:
    lesson_number = argv[1]
    directory = '.'


# Downloads Udacity zip files
def download_zips(lessons, directory):
    counter = 1
    try:
        while counter <= lessons:
            url = "https://s3.amazonaws.com/udacity-hosted-downloads/lesson{}.zip".format(counter)
            outfile = "{}/zip{}".format(directory, counter)
            sub.call(["curl", url, "-o", outfile])
            print(".....curling..zip....file....{}.......".format(counter))
            counter += 1
        print('..........Java Lessons Downloaded.......')
    except:
        print("......ERROR......Try...Again....")

# Script
os.makedirs(directory, exist_ok=True)
download_zips(int(lesson_number), directory)
