import csv
from Domain.Models.directive import Directive

def parse_config(path):
    directive_list = []
    with open(path) as file:
        rows = file.readlines() 
        for row in rows:
            if(row[0] != '#'):                  # comments
                row = row.strip()               # take out leading and ending spaces
                row = row.replace(" ", "")      # delete inner spaces
                directives = [x.strip() for x in row.split(';')]
                try:           
                    current_directive = Directive(directives[0], directives[1], directives[2], directives[3], directives[4], directives[5], [], {})
                    flag = True
                    for directive in directive_list : #TODO anche per sottodirettive
                        if current_directive.source == directive.source :
                            if current_directive.extension == "*" and directive.extension != "*" :
                                current_directive.extension_mappings[directive.extension] = directive.destination
                                directive_list.remove(directive)
                            elif current_directive.extension != "*" and directive.extension == "*" :
                                directive.extension_mappings[current_directive.extension] = current_directive.destination
                                flag = False
                        elif current_directive.source in directive.source and current_directive.source != "": 
                            current_directive.sub_directives.append(directive)
                            directive_list.remove(directive)
                        elif directive.source in current_directive.source and directive.source != "":
                            directive.sub_directives.append(current_directive)
                            flag = False
                    if flag :
                        directive_list.append(current_directive)
                    print(directives)
                except :
                    print('An error occur reading .config file line: \n {0} \n'.format(row))
    return directive_list