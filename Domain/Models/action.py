class Action(object):
    source = ""
    destination = ""
    action = ""

    # The class "constructor" - It's actually an initializer 
    def __init__(self, source, destination, action):
        self.destination = destination
        self.source = source
        self.action = action 