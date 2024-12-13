from io import StringIO
from types import MappingProxyType



class NamelistContentCreator:
    def __init__(self, namelist_title: str):
        self.__title = namelist_title

    def create_namelist(self, namelist_data: MappingProxyType):
        raise NotImplementedError
