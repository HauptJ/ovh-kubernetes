"""OVH Image.

Usage:
  image.py --version
  image.py --getkey
  image.py --listapps
  image.py --install <ovhServerName> <sshKeyName> <hostName> <ovhTemplateName> <useDistribKernel>
  image.py --status <ovhServerName>
  image.py --templates <ovhServerName>
  image.py --reboot <ovhServerName>
  image.py --servers

Options:
  --version     Show version
  --getkey      Get new consumer key
  --listapps    Get a list of all authorized API applications
  --install     Image server
  --status      Get server imaging status
  --templates   Get a list of available image templates
  --reboot      Reboot server
  --servers     List available servers

"""

from docopt import docopt

from classes.OvhAuth import OvhAuth
from classes.OvhAuthError import OvhAuthError
from classes.OvhInstall import OvhInstall
from classes.OvhInstallError import OvhInstallError


def main(arguments):
    try:
        if arguments['--getkey']:
            ovhAuth = OvhAuth()
            ovhAuth.retrieve_consumer_key()
        elif arguments['--listapps']:
            ovhAuth = OvhAuth()
            ovhAuth.retrieve_api_apps()
        elif(arguments['--install']):
            ovhInstall = OvhInstall()
            ovhInstall.install(arguments['<ovhServerName>'], arguments['<sshKeyName>'], arguments['<hostName>'], arguments['<ovhTemplateName>'], arguments['<useDistribKernel>'])
        elif(arguments['--status']):
            ovhInstall = OvhInstall()
            ovhInstall.retrieve_install_status(arguments['<ovhServerName>'])
        elif(arguments['--reboot']):
            ovhInstall = OvhInstall()
            ovhInstall.reboot(arguments['<ovhServerName>'])
        elif(arguments['--templates']):
            ovhInstall = OvhInstall()
            ovhInstall.retrieve_install_templates(arguments['<ovhServerName>'])
        elif(arguments['--servers']):
            ovhInstall = OvhInstall()
            ovhInstall.list_servers()
        else:
            print("Invalid option paramater passed in.")

    except OvhAuthError as e:
        if e.upstreamError is not None:
            print("Auth Error: message: " + str(e.message) + " | upstream error: " + str(e.upstreamError))
        else:
            print("Auth Error: message: " + str(e.message))
    except OvhInstallError as e:
        if e.upstreamError is not None:
            print("Install Error: message: " + str(e.message) + " | upstream error: " + str(e.upstreamError))
        else:
            print("Install Error: message: " + str(e.message))

if __name__== "__main__":
    arguments = docopt(__doc__, version='OVH Image 0.2')
    main(arguments)
