import re
import sys
import ovh

from typing_extensions import Final

from classes.Client import Client
from classes.OvhAuthError import OvhAuthError
from ovh.exceptions import APIError


class OvhAuth(Client):
    CONSUMER_KEY_REGEX: Final = r'(?<=(^consumer_key=))[a-zA-Z0-9]{32}'

    def __init__(self):
        Client.__init__(self)


    def update_consumer_key(self, consumerKey, configFile='./ovh.conf'):
        try:
            with open(configFile, 'r') as inFile:
                ovhConfigTxt = inFile.read()
            
            updatedConfig = re.sub(r'(?<=(^consumer_key=))[a-zA-Z0-9]{32}', consumerKey, ovhConfigTxt, flags=re.M)

            with open(configFile, 'w') as outFile:
                outFile.write(updatedConfig)

        except IOError as e:
            raise OvhAuthError("Failed to update ovh.conf - IOError: ", e)

        except:
            raise OvhAuthError("Failed to update ovh.conf - Unknown Error", sys.exc_info()[0])

            
    def retrieve_consumer_key(self):
        try:
            ck = self._ovhClient.new_consumer_key_request()

            # Request full API access
            ck.add_recursive_rules(ovh.API_READ_WRITE, '/')

            # Request token
            validation = ck.request()

            print("Please visit %s to authenticate" % validation['validationUrl'])
            input("and press Enter to continue...")

            print("Welcome", self._ovhClient.get('/me')['firstname'])
            consumerKey = validation['consumerKey']
            print("Your 'consumer key is '%s'" % consumerKey)

            print("Updating consumer key in ovh.conf")
            self.update_consumer_key(consumerKey)
            print("Consumer key updated in ovh.conf")

        except IOError as e:
            raise OvhAuthError("Failed to retrieve consumer key - IOError: ", e)

        except APIError as e:
            raise OvhAuthError("Failed to retrieve consumer key - APIError", e)

        except:
            raise OvhAuthError("Failed to retrieve consumer key - Unknown Error", sys.exc_info()[0])


    def retrieve_api_apps(self):
        try:
            res = self._ovhClient.get('/me/api/application')
            Client.print_result(res)

        except IOError as e:
            raise OvhAuthError("Failed to retrieve a list of API Apps - IOError", e)

        except APIError as e:
            raise OvhAuthError("Failed to retrieve a list of API Apps - APIError", e)

        except:
            raise OvhAuthError("Failed to retrieve a list of API Apps - Unknown Error",  sys.exc_info()[0])