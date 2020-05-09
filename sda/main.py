import fileinput

from sda.baza import Baza
from sda.dyrektor import Dyrektor


# TODO uzyć modulu tabulate do wyswietlania danych
def obsluz(dyrektor, linia):
    if len(linia) == 0:
        return
    komenda = linia[0]
    if komenda == 'student-dodaj':
        imie = linia[1]
        nazwisko = linia[2]
        wiek = linia[3]
        _id = linia[4]
        dyrektor.student_dodaj(imie, nazwisko, wiek, _id)
    elif komenda == 'student-listuj':
        print(dyrektor.student_listuj())
    elif komenda == 'student-usun':
        student_id = linia[1]
        dyrektor.student_usun(student_id)
    elif komenda == 'student-grupy':
        student_id = linia[1]
        print(dyrektor.student_grupy(student_id))
    if komenda == 'temat-dodaj':
        nazwa = linia[1]
        opis = linia[2]
        _id = linia[3]
        dyrektor.temat_dodaj(nazwa, opis, _id)
    elif komenda == 'temat-listuj':
        print(dyrektor.temat_listuj())
    elif komenda == 'temat-usun':
        temat_id = linia[1]
        dyrektor.temat_usun(temat_id)
    elif komenda == 'temat-grupy':
        temat_id = linia[1]
        print(dyrektor.temat_grupy(temat_id))
    elif komenda == 'grupa-dodaj':
        nazwa = linia[1]
        opis = linia[2]
        _id = linia[3]
        dyrektor.grupa_dodaj(nazwa, opis, _id)
    elif komenda == 'grupa-listuj':
        print(dyrektor.grupa_listuj())
    elif komenda == 'grupa-dodaj-student':
        grupa_id = linia[1]
        student_id = linia[2]
        dyrektor.grupa_dodaj_student(grupa_id, student_id)
    elif komenda == 'grupa-dodaj-temat':
        grupa_id = linia[1]
        temat_id = linia[2]
        dyrektor.grupa_dodaj_student(grupa_id, temat_id)
    elif komenda == 'grupa-dodaj-obecnosc':
        grupa_id = linia[1]
        temat_id = linia[2]
        student_id = linia[3]
        obecnosc = int(linia[4])
        dyrektor.grupa_dodaj_obecnosc(grupa_id, temat_id, student_id, obecnosc)
    elif komenda == 'grupa-dziennik':
        grupa_id = linia[1]
        print(dyrektor.grupa_dziennik(grupa_id))
    elif komenda == 'grupa-frekwencja':
        grupa_id = linia[1]
        print(dyrektor.grupa_frekwencja(grupa_id))
    elif komenda == 'grupa-frekwencja-student':
        grupa_id = linia[1]
        student_id = linia[2]
        print(dyrektor.grupa_frekwencja_student(grupa_id, student_id))
    else:
        print("nieznana komenda")


def run():
    baza = Baza()
    dyrektor = Dyrektor(baza)
    try:
        for linia in fileinput.input():
            linia = linia.strip().split()
            obsluz(dyrektor, linia)
    except KeyboardInterrupt:
        return
    except Exception as e:
        print("error: ", e)


if __name__ == '__main__':
    run()
