import os, datetime, glob, time
from shutil import copyfile
import Domain.localizations as loc
from Domain.Models.action import Action
from Domain.Models.directive import Directive
import os.path

now = datetime.datetime.now()

# massive functions
def check_files(directive): # copy source to destination 
    if(directive.backup_mode == "copy" or directive.backup_mode == "cut"):
        for action in one_side_check(directive):
            log("{0} \t ; \t {1} \t ; \t {2}".format(action.action, action.source, action.destination), "{0}{1}".format(loc.log_dir, "actions.log"))

    #result = []
    #if(action == "restore") #swap
    #    tmp = destination
     #   destination = source
     #   source = tmp
      #  action = "copy"
 #filename, file_extension = os.path.splitext(file) #get file name and extension
   
# arriva direttiva ritorna lista action
def one_side_check(directive):
    file_list = []
    os.chdir("{0}".format(directive.source))
    for file in glob.glob("*"):    # foreach file in source path

        source_file = "{0}{1}".format(directive.source, file)
        destination_file = "{0}{1}".format(directive.destination, file)
        filename, file_extension = os.path.splitext(file) #get file name and extension

        if file_extension in directive.extension_mappings :
            directive.destination_file = "{0}{1}".format(directive.extension_mappings[file_extension], file)

        if not os.path.isdir(source_file):
            tuple = Action(source_file, destination_file, directive.backup_mode)
            if exists(destination_file):  
                if not are_the_same(source_file, destination_file):          
                    file_list.append(tuple)
            else:
                file_list.append(tuple)
        else:
            new_directive = Directive(directive.extension, source_file, destination_file, directive.backup_mode, directive.options, directive.environment, directive.sub_directives, directive.extension_mappings)
            for dir in directive.sub_directives :
                if dir.source == source_file :
                    new_directive = dir
            file_list.extend(one_side_check(new_directive))
    return file_list

def exists(file):
    return os.path.isfile(file)

def are_the_same(source, destination):
    has_same_last_modified_date = (os.path.getmtime(source) == os.path.getmtime(destination))   # check last modified date
    has_same_size = (os.stat(source).st_size == os.stat(destination).st_size)                   # check size
    return (has_same_last_modified_date and has_same_size)

# primitive functions

def copy(source, destination):
    copyfile(source, destination)   
    log("copy {0} to {1}".format(source, destination), loc.log_dir, "{0}{1}".format(loc.log_dir, "actions.log"))

def delete(source):
    os.remove(source)
    log("delete {0}".format(source), "{0}{1}".format(loc.log_dir, "actions.log"))
   
def cut(source, destination):
    copy(source, destination)
    delete(source)

def log(text, path, time = False):
    with open(path, 'ab+') as f:
        if time:
            f.write("{0}:{1} {2}\n".format(now.hour, now.minute, text))
        else :
            f.write("{0}\n".format(text))

#                text = "{0}\t;\t{1}\t;\t{2}".format(action, source_file, destination_file)
                #"{0}{1}{2}.log".format(directory, now.year, now.month, now.day),    
#                log(source_file, destination_file)

def print_log():
    with open("{0}{1}{2}{3}.log".format(loc.log_dir, now.year, now.month, now.day), 'r') as f:
        print f.read()