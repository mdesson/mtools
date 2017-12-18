# Script makes a back up of selected files in list every 15 minutes
# The script retains a total of 8 backups
# Each time it creates a new backup, it removes the oldest one
# This is meant to be done as a cron job or used with Windows Task Scheduler

from shutil import copy, rmtree
from datetime import datetime
from os import listdir, makedirs

targets = ["C:/FULL/PATH/HERE/FILE.txt"]

destination = "C:/PATH/TO/ARCHIVE"


def dirname():
    now = datetime.now()
    timestamp = "{}.{}.{}-{}.{}".format(now.year, now.month, now.day, now.hour, now.minute)
    return "{}/{}/".format(destination, timestamp)


def rm_old_dir():
    dirs = {}
    destination_list = listdir(destination)
    for i in destination_list:
        try:
            datetime_object = datetime.strptime(i.split("/")[-1], '%Y.%m.%d-%H.%M')
            dirs[datetime_object] = i

        except ValueError:
            print("ValueError: {} could not be converted into datetime object".format(i))

        except:
            print("Unknown error occurred while creating list of dicts holding datetime_object:directory.")
            print("Currently iterating on {}".format(i))
            print("Iterating over these dirs: {}".format(listdir(destination)))
            print("List of successfully created dir:datetime dicts: {}".format(dirs))

    if len(dirs) >= 8:
        oldest_dir = datetime.now()
        for key in dirs.items():
            if key[0] < oldest_dir:
                oldest_dir = key[0]

    if dirs != {}:
        rmtree("{}/{}".format(destination, dirs[oldest_dir]))


def backup(targetlist):
    destination_directory = dirname()
    makedirs(destination_directory)
    for file in targetlist:
        copy(file, destination_directory)


if __name__ == "__main__":
    rm_old_dir()
    backup(targets)
