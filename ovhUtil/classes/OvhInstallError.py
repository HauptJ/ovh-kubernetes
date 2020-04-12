from classes.Error import Error

class OvhInstallError(Error):

    def __init__(self, message, upstreamError=None):
        self.message = message
        self.upstreamError = upstreamError