import time


class FourThreeThreeMhzSocketOffOn:
    socket: None
    delay: int

    def __init__(self, socket, delay):
        self.socket = socket
        self.delay = delay

    def execute(self):
        print('Consequence Executing...')
        return self.socket_off_on_with_delay()

    def socket_off_on_with_delay(self):
        self.socket_off()
        self.pause()
        self.socket_on()
        return True

    def socket_on(self):
        print('Socket: ON')

    def socket_off(self):
        print('Socket: OFF')

    def pause(self):
        print(f"Socket Delay: Waiting {self.delay} seconds")
        time.sleep(self.delay)
