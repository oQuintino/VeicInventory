from io import StringIO
from types import MappingProxyType
from typing import LiteralString



class NamelistContentCreator:
    def __init__(self, namelist_title: LiteralString):
        self.__title = namelist_title

    def create_namelist(self, namelist_data: MappingProxyType):
        raise NotImplementedError
