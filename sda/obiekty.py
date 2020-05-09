import uuid
from collections import defaultdict

from sda.baza import ObiektBazy


class Temat(ObiektBazy):
    def __init__(self, nazwa, opis, _id=None):
        super().__init__(_id)
        self.nazwa = nazwa
        self.opis = opis

    def __repr__(self):
        return f'"{self.nazwa} - {self.opis}"'


class Student(ObiektBazy):
    def __init__(self, imie, nazwisko, wiek, _id=None):
        super().__init__(_id)
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    #def __str__(self):
    #    return f'{self.imie} {self.nazwisko} ({self.wiek})'

    def __repr__(self):
        return f'"{self.imie} {self.nazwisko} ({self.wiek})"'


class Grupa(ObiektBazy):
    def __init__(self, nazwa, opis, _id=None):
        super().__init__(_id)
        self.nazwa = nazwa
        self.opis = opis
        self.studenci = []
        self.dziennik_id = ''

    def __repr__(self):
        return f'"{self.nazwa} - {self.opis}"'


# TODO dodac oceny
class Dziennik(ObiektBazy):
    def __init__(self):
        super().__init__()
        self.obecnosci = defaultdict(dict)
        # self.obecnosc[temat_id][student_id] = 0 albo 1
