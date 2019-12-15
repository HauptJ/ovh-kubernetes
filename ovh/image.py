#!/usr/bin/env python3

"""OVH Image.

Usage:
  image.py --version
  image.py --getkey
  image.py --listapps
  image.py --install <ovhServerName> <sshKeyName> <hostName> <ovhTemplateName> <useDistribKernel>
  image.py --status <ovhServerName>
  image.py --templates <ovhServerName>
  image.py --reboot <ovhServerName>

Options:
  --version     Show version
  --getkey      Get new consumer key
  --listapps    Get a list of all authorized API applications
  --install     Image server
  --status      Get server imaging status
  --templates   Get a list of available image templates
  --reboot      Reboot server 

"""


import ovh
import json
import sys
from docopt import docopt


def retrieve_consumer_key(ovh_client):

    ck = ovh_client.new_consumer_key_request()

    # Request full API access
    ck.add_recursive_rules(ovh.API_READ_WRITE, '/')

    # Request token
    validation = ck.request()

    print("Please visit %s to authenticate" % validation['validationUrl'])
    input("and press Enter to continue...")

    print("Welcome", ovh_client.get('/me')['firstname'])
    print("Your 'consumer key is '%s'" % validation['consumerKey'])


def retrieve_api_apps(ovh_client):

    return ovh_client.get('/me/api/application')


def retrieve_install_templates(ovh_client, ovh_server_name):

    return ovh_client.get('/dedicated/server/' + ovh_server_name + '/install/compatibleTemplates')


def retrieve_status(ovh_client, ovh_server_name):

    return ovh_client.get('/dedicated/server/' + ovh_server_name + '/install/status')


def reboot(ovh_client, ovh_server_name):
    
    return ovh_client.post('/dedicated/server/' + ovh_server_name + '/reboot')


def install(ovh_client, ovh_server_name, ssh_key_name, host_name, ovh_template_name, use_distrib_kernel=False):

    result = ovh_client.post(
    '/dedicated/server/'+ ovh_server_name + '/install/start',
    details={
        "noRaid":False,
        "sshKeyName":ssh_key_name,
        "language":"en",
        "useSpla":False,
        "diskGroupId": 1,
        "resetHwRaid":False,
        "customHostname":host_name,
        "installSqlServer":False,
        "useDistribKernel":use_distrib_kernel
    },
    templateName=ovh_template_name,
    )
    return result


def print_result(result):
    print(json.dumps(result, indent=4))


def client():
    # create a client instance using configuration in ovh.conf
    return ovh.Client()



def main(arguments):

    if arguments['--getkey']:
        retrieve_consumer_key(client())
    elif arguments['--listapps']:
        print_result(retrieve_api_apps(client()))
    elif(arguments['--install']):
        print_result(install(client(), arguments['<ovhServerName>'], arguments['<sshKeyName>'], arguments['<hostName>'], arguments['<ovhTemplateName>'], arguments['<useDistribKernel>']))
    elif(arguments['--status']):
        print_result(retrieve_status(client(), arguments['<ovhServerName>']))
    elif(arguments['--reboot']):
        print_result(reboot(client(), arguments['<ovhServerName>']))
    elif(arguments['--templates']):
        print_result(retrieve_install_templates(client(), arguments['<ovhServerName>']))
    else:
        print("Invalid option paramater passed in.")

if __name__== "__main__":
    arguments = docopt(__doc__, version='OVH Image 0.1')
    main(arguments)
