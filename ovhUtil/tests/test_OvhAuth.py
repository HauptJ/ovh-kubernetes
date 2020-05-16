import unittest

from typing_extensions import Final

from classes.OvhAuth import OvhAuth
from classes.OvhAuthError import OvhAuthError


class Test_OvhAuth(unittest.TestCase):
    TEST_CK_REGEX_STRING: Final = "consumer_key=byb7NafakeN73atestIA0Jk6Kt3stXSAA"
    TEST_CK_STRING: Final = "ayyb7NafakeN73atestIA0Jk6Kt3stXSA"
    TEST_CK_STRING1: Final = "byb7NafakeN73atestIA0Jk6Kt3stXSA"

    def __init__(self, *args, **kwargs):
        super(Test_OvhAuth, self).__init__(*args, **kwargs)


    def test_RegexPattern(self):
        try:
            self.assertRegex(Test_OvhAuth.TEST_CK_REGEX_STRING, OvhAuth.CONSUMER_KEY_REGEX)
        except IOError as e:
            self.fail(e)


    def test_get_ovhClient(self):
        try:
            auth = OvhAuth()
            self.assertIsNotNone(auth.get_ovhClient())
            del auth

        except IOError as e:
            self.fail(e)

        except OvhAuthError as e:
            self.fail(e)

    
    def test_update_consumer_key(self):
        try:
            auth = OvhAuth()
            auth.update_consumer_key(Test_OvhAuth.TEST_CK_STRING, 'ovh.test')
            with open('ovh.test', 'r') as inFile:
                ovhConfigTxt = inFile.read()

            self.assertIn(Test_OvhAuth.TEST_CK_STRING, ovhConfigTxt)
            auth.update_consumer_key(Test_OvhAuth.TEST_CK_STRING1, 'ovh.test')

        except IOError as e:
            self.fail(e)

        except OvhAuthError as e:
            self.fail(e)