import platform
import Domain.localizations as loc
import Utils.file_manager as fm 

def generate_scripts(directives):
    for directive in directives :
        fm.check_files(directive)
        

def apply_config(directives):
    filtered_directives = []
    for directive in directives:
        if(directive.backup_mode == "environment"):
            check_os(directive.options)
        if(directive.environment == loc.environment):
            if(directive.backup_mode == "log_path"):
                loc.log_dir = directive.options
            elif(directive.backup_mode == "base_path"):
                loc.source_dir = directive.source 
                loc.destination_dir = directive.destination
            else:
                directive.source = "{0}{1}".format(loc.source_dir, directive.source)
                directive.destination = "{0}{1}/{2}".format(loc.destination_dir, loc.environment, directive.destination)
                filtered_directives.append(directive)
    return filtered_directives

def check_os(option):
    if option == "auto":
        loc.environment = platform.system()
        if loc.environment == 'Linux':
            loc.environment = platform.dist()[0]
    else:
        loc.environment = option
    print_message("Current OS: {0}\n".format(loc.environment))

def print_message(message):
    print("\n\n------------------------------------------------------------------------------")
    print("\n\t {0} \n".format(message))
    print("------------------------------------------------------------------------------\n\n")