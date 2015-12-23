from cafe.engine.http.client import AutoMarshallingHTTPClient
from cloudcafe.brm.models import requests, responses

class BrmClient(AutoMarshallingHTTPClient):
    '''
    This is the client class which aids in accessing
    Create Customer api.Each function in this
    class creates a request to an api and recieves
    the response.
    '''

    def __init__(self):
        pass

    def create_customer(self, requestslib_kwargs=None):
        pass