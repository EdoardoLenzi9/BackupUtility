class Directive(object):
    extension = ""
    source = ""
    destination = ""
    backup_mode = ""
    options = []
    environment = ""
    sub_directives = []
    extension_mappings = dict()

    # The class "constructor" - It's actually an initializer 
    def __init__(self, extension, source, destination, backup_mode, options, environment, sub_directives, extension_mappings):
        self.destination = destination
        self.extension = extension
        self.source = source
        self.backup_mode = backup_mode
        self.options = options
        self.environment = environment
        self.sub_directives = sub_directives
        self.extension_mappings = extension_mappings
