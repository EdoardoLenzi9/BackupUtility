import os, datetime
from shutil import copyfile
import localizations as loc
import os.path

now = datetime.datetime.now()

def checkFile(path):
    return path.is_file()

def cut(source, destination):
    copy(source, destination)
    os.remove(source)
    log("delete {0}".format(source))

def copy(source, destination):
    copyfile(source, destination)   
    log("copy {0} to {1}".format(source, destination))
   
def log(text):
    with open("{0}{1}{2}.log".format(loc.log_dir, now.year, now.month, now.day),'ab') as f:
        f.write("{0}:{1} {2}\n".format(now.hour, now.minute, text))

def print_log():
    with open("{0}{1}{2}{3}.log".format(loc.log_dir, now.year, now.month, now.day), 'r') as f:
        print f.read()