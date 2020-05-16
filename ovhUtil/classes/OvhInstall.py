import sys

from classes.Client import Client
from classes.OvhInstallError import OvhInstallError
from ovh.exceptions import APIError


class OvhInstall(Client):

    def __init__(self):
        Client.__init__(self)

    def install(self, ovh_server_name, ssh_key_name, host_name, ovh_template_name, use_distrib_kernel=False):

        try:
            res = self._ovhClient.post(
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
            Client.print_result(res)

        except IOError as e:
            raise OvhInstallError("Failed to image server - IOError", e)

        except APIError as e:
            raise OvhInstallError("Failed to image server - APIError", e)

        except:
            raise OvhInstallError("Failed to image server - Unknown error", sys.exc_info()[0])


    def retrieve_install_templates(self, ovh_server_name):

        try:
            res = self._ovhClient.get('/dedicated/server/' + ovh_server_name + '/install/compatibleTemplates')
            Client.print_result(res)

        except IOError as e:
            raise OvhInstallError("Failed to retrieve list of server installation templates - IOError", e)

        except APIError as e:
            raise OvhInstallError("Failed to retrieve list of server installation templates - APIError", e)

        except:
            raise OvhInstallError("Failed to retrieve list of server installation templates - unknown error", sys.exc_info()[0])


    def retrieve_install_status(self, ovh_server_name):

        try:
            res = self._ovhClient.get('/dedicated/server/' + ovh_server_name + '/install/status')
            Client.print_result(res)

        except IOError as e:
            raise OvhInstallError("Failed to retrieve server installation status - IOError", e)

        except APIError as e:
            raise OvhInstallError("Failed to retrieve server installation status - APIError", e)

        except:
            raise OvhInstallError("Failed to retrieve server installation status - unknown error", sys.exc_info()[0])


    def reboot(self, ovh_server_name):

        try:
            res = self._ovhClient.post('/dedicated/server/' + ovh_server_name + '/reboot')
            Client.print_result(res)

        except IOError as e:
            raise OvhInstallError("Failed to reboot server - IOError", e)

        except APIError as e:
            raise OvhInstallError("Failed to reboot server - APIError", e)

        except:
            raise OvhInstallError("Failed to reboot server - unknown error", sys.exc_info()[0])


    def list_servers(self):

        try:
            res = self._ovhClient.get('/dedicated/server')
            Client.print_result(res)

        except IOError as e:
            raise OvhInstallError("Failed to get a list of servers - IOError", e)

        except APIError as e:
            raise OvhInstallError("Failed to get a list of servers - APIError", e)

        except:
            raise OvhInstallError("Failed to get a list of servers - unknown error", sys.exc_info()[0])