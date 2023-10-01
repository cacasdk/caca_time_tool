import time


class CacaTimeTool:
    def __init__(self, path):
        self.path = path
        self.debug = False

    @property
    def old_time(self):
        with open(self.path, "r") as r:
            return r.read()

    @property
    def new_time(self):
        return time.time()

    def compare(self, h):
        the_time = self.new_time - self.old_time
        if not self.debug:
            return the_time >= h * 3600
        else:
            return True
