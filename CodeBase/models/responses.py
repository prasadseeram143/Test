from cloudcafe.object_rocket.models.base import BaseBRM


class CreateCustomer(BaseBRM):
    '''
    This is the response class for Create Customer api.
    The response body's content part is converted from string
    format to an object.
    '''

    def __init__(self):
    	pass

    @classmethod
    def _string_to_obj(cls, data):
        pass


class