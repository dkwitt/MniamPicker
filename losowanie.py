import random
def wyswietl_kivi(boolean):
    if not type(boolean) is bool:
        raise TypeError("Kivi bamboozled")

    if boolean:
        return  """ (^) 
    /(   )"""
    else:
        return """ (-) 
    /(   )"""

def losuj_pytania(baza_pytan, baza_zadanych_pytan):
    if (len(baza_pytan) <= 0 and len(baza_zadanych_pytan) <= 0 ) or (type(baza_pytan) is not list or type(baza_zadanych_pytan) is not list):
        raise ValueError(":c nie wolno")
    if baza_pytan == []:
        baza_pytan = baza_zadanych_pytan
        baza_zadanych_pytan = []
    wylosowany_indeks=(random.randint(0,len(baza_pytan)))
    pytanie_do_przeniesienia = baza_pytan.pop(wylosowany_indeks)
    baza_zadanych_pytan.append(pytanie_do_przeniesienia)
    return pytanie_do_przeniesienia````````