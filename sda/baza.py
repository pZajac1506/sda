# -*- coding: UTF-8 -*-
import uuid


class ObiektBazy:
    def __init__(self, _id=None):
        if _id is not None:
            self.__id = _id
        else:
            self.__id = uuid.uuid4().hex

    @property
    def id(self):
        return self.__id


class Baza:
    def __init__(self):
        self.studenci = {}
        self.tematy = {}
        self.grupy = {}
        self.dzienniki = {}


# TODO trudne! zaimplementować bazę która zapisuje dane w pliku
# Zrobić to tak, żeby nie zmieniać reszty kodu
class BazaWPliku:
    pass
