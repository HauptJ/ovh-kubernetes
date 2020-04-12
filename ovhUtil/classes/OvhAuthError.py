from classes.Error import Error

class OvhAuthError(Error):

    def __init__(self, message, upstreamError=None):
        self.message = message
        self.upstreamError = upstreamError