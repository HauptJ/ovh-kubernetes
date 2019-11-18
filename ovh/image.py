#!/usr/bin/env python3

import ovh
import json
import sys
import getopt


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

def printResult(result):
    print(json.dumps(result, indent=4))


def client():
    # create a client instance using configuration in ovh.conf
    ovhClient = ovh.Client()
    return ovhClient


def main(argv):
    option = ''
    ovhServerName = ''
    sshKeyName = ''
    sshKeyName = ''
    hostName = ''
    ovhTemplateName = ''
    useDistribKernel = ''

    try:
        opts, args = getopt.getopt(argv,"hi:o",["option="])
    

    # Function return output

    ovhClient = client()
    if(option == "reinstall"):
        result = reimage(ovhClient, ovhServerName, sshKeyName, hostName, ovhTemplateName, useDistribKernel)
        printResult(result)
    else:
        print("Invalid option paramater passed in.")
    

if __name__== "__main__":
    main(sys.argv[1:])
