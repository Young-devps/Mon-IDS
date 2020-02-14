from datetime import datetime

class CurrentTime(object):
    def index(self):
        return str(datetime.now())