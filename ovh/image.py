#!/usr/bin/env python3

"""OVH Image.

Usage:
  image.py --version
  image.py 

Options:
  --version     Show version

"""


import ovh
import json
import sys
from docopt import docopt

def reimage(ovhClient, ovhServerName, sshKeyName, hostName, ovhTemplateName, useDistribKernel=False):

    result = ovhClient.post(
    '/dedicated/server/'+ ovhServerName + '/install/start',
    details={
        "noRaid":False,
        "sshKeyName":sshKeyName,
        "language":"en",
        "useSpla":False,
        "diskGroupId": 1,
        "resetHwRaid":False,
        "customHostname":hostName,
        "installSqlServer":False,
        "useDistribKernel":useDistribKernel
    },
    templateName=ovhTemplateName,
    )
    return result


def getConsumerKey(ovhClient):

    ck = ovhClient.new_conumer_key_request()

    # Request full API access
    ck.add_recursive_rules(ovh.API_READ_WRITE, '/')

    # Request token
    validation = ck.request()

    print("Please visit %s to authenticate" % validation['validationUrl'])
    input("and press Enter to continue...")

    print("Welcome", ovhClient.get('/me')['firstname'])
    print("Your 'consumer key is '%s'" % validation['consumerKey'])



def printResult(result):
    print(json.dumps(result, indent=4))


def client():
    # create a client instance using configuration in ovh.conf
    ovhClient = ovh.Client()
    return ovhClient


def main(arguments):
    option = ''
    ovhServerName = ''
    sshKeyName = ''
    sshKeyName = ''
    hostName = ''
    ovhTemplateName = ''
    useDistribKernel = ''
    

    # Function return output

    ovhClient = client()
    if(option == "reinstall"):
        result = reimage(ovhClient, ovhServerName, sshKeyName, hostName, ovhTemplateName, useDistribKernel)
        printResult(result)
    else:
        print("Invalid option paramater passed in.")
    

if __name__== "__main__":
    arguments = docopt(__doc__, version='OVH Image 0.1')
    main(arguments)
