# -*- coding: UTF-8 -*-
from sda.obiekty import Student, Grupa, Dziennik, Temat


class Dyrektor:
    def __init__(self, baza):
        self._baza = baza

    def student_dodaj(self, imie, nazwisko, wiek, _id=None):
        s = Student(imie, nazwisko, wiek, _id)
        self._baza.studenci[s.id] = s

    def student_listuj(self):
        studenci = self._baza.studenci.values()
        return studenci

    # TODO zaimplementowac usuwanie studenta
    def student_usun(self, student_id):
        raise NotImplementedError()

    # TODO zaimplementowac wyszukanie grup w których jest student
    def student_grupy(self, student_id):
        '''Zwraca liste grup do ktorych nalezy student'''
        raise NotImplementedError()

    def temat_dodaj(self, nazwa, opis, _id=None):
        t = Temat(nazwa, opis, _id)
        self._baza.tematy[t.id] = t

    def temat_listuj(self):
        tematy = self._baza.tematy.values()
        return tematy

    # TODO zaimplementowac usuwanie tematu
    def temat_usun(self, temat_id):
        raise NotImplementedError()

    # TODO zaimplementowac wyszukanie grup w których jest student
    def temat_grupy(self, student_id):
        '''Zwraca liste grup w ktorych omawiany jest temat'''
        raise NotImplementedError()

    def grupa_dodaj(self, nazwa, opis, _id=None):
        grupa = Grupa(nazwa, opis, _id)
        dziennik = Dziennik()
        self._baza.dzienniki[dziennik.id] = dziennik
        grupa.dziennik_id = dziennik.id
        self._baza.grupy[grupa.id] = grupa

    def grupa_listuj(self):
        grupy = self._baza.grupy.values()
        return grupy

    def grupa_dodaj_student(self, grupa_id, student_id):
        grupa = self._baza.grupy[grupa_id]
        grupa.studenci.append(student_id)

    def grupa_dodaj_temat(self, grupa_id, temat_id):
        grupa = self._baza.grupy[grupa_id]
        dziennik = self._baza.dzienniki[grupa.dziennik_id]
        dziennik.tematy.append(temat_id)

    def grupa_studenci(self, grupa_id):
        grupa = self._baza.grupy[grupa_id]
        studenci = []
        for student_id in grupa.studenci:
            student = self._baza.studenci[student_id]
            studenci.append(student)
        return studenci

    def grupa_dziennik(self, grupa_id):
        grupa = self._baza.grupy[grupa_id]
        dziennik = self._baza.dzienniki[grupa.dziennik_id]
        return dziennik

    def grupa_dodaj_obecnosc(self, grupa_id, temat_id, student_id, obecnosc):
        grupa = self._baza.grupy[grupa_id]
        dziennik = self._baza.dzienniki[grupa.dziennik_id]
        dziennik.obecnosci[temat_id][student_id] = obecnosc

    # TODO podawaj w procentach
    def grupa_frekwencja_student(self, grupa_id, student_id):
        obecnosci = 0
        tematy = 0
        grupa = self._baza.grupy[grupa_id]
        dziennik = self._baza.dzienniki[grupa.dziennik_id]
        for temat_id in dziennik.obecnosci.keys():
            tematy += 1
            if dziennik.obecnosci[temat_id][student_id]:
                obecnosci += 1
        return obecnosci / tematy

    # zaimplementować pokazanie frekwencji dla kazdego studena z grupy
    def grupa_frekwencja(self, grupa_id):
        raise NotImplementedError()
