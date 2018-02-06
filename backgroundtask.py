import threading
import time


def your_function():
    print("your code")


class Execute(object):
    # set interval time
    def __init__(self, interval=10):
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        # if it is equal to false background task is not active
        thread.daemon = True
        thread.start()

    def run(self):
        try:
            while True:
                # Do something
                your_function()
                time.sleep(self.interval)
        except Exception:
            pass


teste = Execute()
