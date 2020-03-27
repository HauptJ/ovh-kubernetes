from classes.Error import Error

def __init__(self, message, upstreamError=None):
    self.message = message
    self.upstreamError = upstreamError