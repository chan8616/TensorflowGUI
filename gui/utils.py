
class Redirection(object):
    def __init__(self, log_area):
        self.out = log_area

    def write(self, string):
        self.out.WriteText(string)

    def flush(self):
        pass

