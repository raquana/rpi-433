import requests
import random


class TwoHundredResponseChecker:

    _ips: []
    _success = 200

    def __init__(self, ips):
        self._ips = ips

    def check(self):
        return self.check_response()

    def check_response(self):
        random.shuffle(self._ips)
        for ip in self._ips:
            try:
                print(f'Checking {ip}')
                response = requests.get('https://' + ip, timeout=2.000)
                if response.status_code == self._success:
                    return True
            except:
                print(f'Failed checking {ip}')

        return False
