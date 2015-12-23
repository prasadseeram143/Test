from cafe.engine.models.base import AutoMarshallingModel


class BaseBRM(AutoMarshallingModel):
    '''
    This is the base class for Create Customer API.
    It provides functions to serialize requests
    and deserialize responses.
    '''

    def _obj_to_flist(self):
        return self._obj_to_string()

    @classmethod
    def _string_to_obj(cls, data):
        pass