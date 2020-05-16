import json

import ovh


class Client:

    def __init__(self):
        self._ovhClient = ovh.Client()

    def get_ovhClient(self):
        return self._ovhClient

    @staticmethod
    def print_result(result):
        print(json.dumps(result, indent=4))