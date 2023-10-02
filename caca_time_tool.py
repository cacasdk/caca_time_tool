import time


class CacaTimeTool:
    def __init__(self, path):
        self.path = path
        self.debug = False

    def init(self):
        with open(self.path, "w") as w:
            w.write()
            w.close()

    @property
    def old_time(self):
        with open(self.path, "r") as r:
            output = r.read()
            r.close()
            return output

    @property
    def new_time(self):
        return time.time()

    def compare(self, h):
        the_time = float(self.new_time) - float(self.old_time)
        if not self.debug:
            if the_time >= h * 3600:
                with open(self.path, "w") as w:
                    w.write(str(time.time()))
                    w.close()
                return True
            else:
                return False
        else:
            print("Warning:The DEBUG mode is on!")
            return True
