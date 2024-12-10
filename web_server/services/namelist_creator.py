from typing import TextIO


class NamelistCreator:
    def __init__(self, namelist_file_name: str):
        self.__name = namelist_file_name

    def create_namelist(self) -> TextIO:
        raise NotImplementedError
