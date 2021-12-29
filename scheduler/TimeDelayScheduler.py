import time


class TimeDelayScheduler:
    delay: int
    consequence_limit: int
    consequence_count = 0
    _stop_now = False

    def __init__(self, checker_with_consequence, delay=30, consequence_limit=2):
        self.checker_with_consequence = checker_with_consequence
        self.delay = delay
        self.consequence_limit = consequence_limit

    def run(self):
        while not self._stop_now:
            check_result, consequence_result = self.checker_with_consequence.do_check()
            if consequence_result:
                self.consequence_count += 1
            else:
                self.consequence_count = 0
            self.pause()
            if self.consequence_count == self.consequence_limit:
                self._stop_now = True
                print(f'Consequence limit of {self.consequence_limit} reached.  Stopping.')

    def pause(self):
        time.sleep(self.delay)
