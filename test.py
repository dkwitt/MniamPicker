import pytest
from losowanie import *
import random


# def test_losuj_pytania_pusta_baza_pytan():
#     with pytest.raises(ValueError):
#         baza_pytan = []
#         losuj_pytania(baza_pytan, [":3 hihi źle"])
def test_losuj_pytania_losuje_pytanie():
    lista_pytan = ["a"]
    lista_zadanych_pytan = []
    assert losuj_pytania(lista_pytan, lista_zadanych_pytan) == "a"
def test_losuj_pytania_zamienia_pusta_z_pelna():
    baza_pytan = []
    baza_zadanych_pytan = ["jednopytanie", "drugiepytanie"]
    losuj_pytania(baza_pytan, baza_zadanych_pytan)
    assert len(baza_pytan) == 1 and 1 == len(baza_zadanych_pytan)

def test_losuj_pytania_zamienia_jedno_pytanie():
    baza_pytan = []
    baza_zadanych_pytan = ["jednopytanie"]
    losuj_pytania(baza_pytan, baza_zadanych_pytan)
    assert len(baza_pytan) == 0 and len(baza_zadanych_pytan) == 1


def test_losuj_pytania_losuje_jedno_z_dwoch():
    baza_pytan = []
    baza_zadanych_pytan = ["jednopytanie", "drugiepytanie"]
    assert losuj_pytania(baza_pytan, baza_zadanych_pytan) in ["jednopytanie", "drugiepytanie"]
def test_losuj_pytania_przepisuje_zadane_pytania():
    baza_pytan = ["z"]
    baza_zadanych_pytan = []
    pytanie = baza_pytan[0]
    assert len(baza_pytan) == 1 and len(baza_pytan)>len(baza_zadanych_pytan)
    assert losuj_pytania(baza_pytan, baza_zadanych_pytan) == pytanie
    assert pytanie in baza_zadanych_pytan and pytanie not in baza_pytan

        # assert wylosuje tę rzecz z bay pytan
        # ta rzecz nie znajduje sie w bazie [pytan ale nznajdujee sie w bazie zadanych pytanb

def test_losuj_pytania_wszystkie_cykl():
    pass

def test_losuj_pytania_puste_obie_bazy():
    with pytest.raises(ValueError):
        baza_pytan = []
        losuj_pytania(baza_pytan, [])

def test_losuj_pytania_baza_pytan_string():
    with pytest.raises(ValueError):
        baza_pytan = "jakisnapis"
        losuj_pytania(baza_pytan, [":3 hihi źle"])

def test_wyswietl_bleniedponperaEN_Edane():
    with pytest.raises(TypeError):
        wyswietl_kivi("string")
def test_wyswietl_true():
    assert wyswietl_kivi(True) ==  """ (^) 
    /(   )"""
def test_wyswietl_false():
    assert wyswietl_kivi(False) ==  """ (-) 
    /(   )"""

#
# def test_kivi():
#     assert func(2)==3
# def test_kivi2():
#     assert func("s")==3

