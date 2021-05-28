import sqlite3
import json
DB_DIR = 'C:\\Users\\Dominika\\Mniam\\MniamPicker\\testdb5.sqlite'

class Obiad:
    nazwa = None
    id = None
    podkladka = None
    mieso = None
    dodatki = []
    def __init__(self, id, nazwa, podkladka, mieso):
        self.id = id
        self.nazwa = nazwa
        self.podkladka = podkladka
        self.mieso = mieso
    def update_self_dodatki(self):
        self.dodatki = get_relation_obiad(self.id)



class Mieso:
    nazwa = None
    id = None
    def __init__(self, id, nazwa):
        self.id = id
        self.nazwa = nazwa
class Podkladka:
    nazwa = None
    id = None
    def __init__(self, id, nazwa):
        self.id = id
        self.nazwa = nazwa
class Dodatki:
    nazwa = None
    id = None
    def __init__(self, id, nazwa):
        self.id = id
        self.nazwa = nazwa

class DodatkiObiadRelation:
    fk_obiad = None
    fk_dodatki = None
    def __init__(self, fk_dodatki, fk_obiad):
        self.fk_dodatki =fk_dodatki
        self.fk_obiad = fk_obiad


# 1. STWORZENIE BAZY I POŁĄCZENIE JEJ
# 2. NAPISANIE FUNKCJI CREATE/ADD? OBIAD/PODL/DOD
# 3. FUNKCJA READ
# 4. FUNKCJA UPDATE
# 5. FUNKCJA DELETE

def start():

    connection = sqlite3.connect(DB_DIR)

    cursor = connection.cursor()
    query = """
        	    CREATE TABLE IF NOT EXISTS podkladka(
        	    	id_podkladka INTEGER PRIMARY KEY, 
        	    	nazwa VARCHAR(50)
        	    )
        	"""

    cursor.execute(query)
    connection.commit()
    query = """
            	    CREATE TABLE IF NOT EXISTS mieso(
            	    	id_mieso INTEGER PRIMARY KEY, 
            	    	nazwa VARCHAR(50)
            	    )
            	"""

    cursor.execute(query)
    connection.commit()
    query = """
            	    CREATE TABLE IF NOT EXISTS dodatki(
            	    	id_dodatki INTEGER PRIMARY KEY, 
            	    	nazwa VARCHAR(50)
            	    )
            	"""

    cursor.execute(query)
    connection.commit()

    query = """
    	    CREATE TABLE IF NOT EXISTS obiad(
    	    	id_obiad INTEGER PRIMARY KEY REFERENCES dodatkiobiadrelation (fk_obiad) ON DELETE CASCADE,
    	    	nazwa VARCHAR(50),
    	    	id_podkladka INTEGER NOT NULL,
    	    	id_mieso INTEGER NOT NULL,
    	    	FOREIGN KEY(id_podkladka) REFERENCES podkladka (id_podkladka),
    	    	FOREIGN KEY(id_mieso) REFERENCES mieso (id_mieso)
    	    )
    	"""

    cursor.execute(query)

    connection.commit()
    query = """
                    	    CREATE TABLE IF NOT EXISTS dodatkiobiadrelation(
                    	    	fk_dodatki REFERENCES dodatki(id_dodatki) ON DELETE CASCADE,
                    	    	fk_obiad REFERENCES obiad(id_obiad) ON DELETE CASCADE
                    	    )
                    	"""

    cursor.execute(query)
    connection.commit()
    connection.close()




def add_obiad(podkladka, mieso, nazwa):
    conn = sqlite3.connect(DB_DIR)

    cursor = conn.cursor()
    if validate_sql_safe(nazwa):

        query = """
            INSERT INTO obiad(nazwa, id_podkladka, id_mieso )
                        VALUES ( ?,?,?)
        """

        cursor.execute(query, (nazwa, podkladka, mieso))
        conn.commit()
        new_obiad_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return new_obiad_id
    else:
        print("Niepoprawna nazwa obiadu")
        conn.close()
        return -1

def add_podkladka(podkladka):
    conn = sqlite3.connect(DB_DIR)

    cursor = conn.cursor()

    query = """
	    INSERT INTO podkladka(nazwa)
	    	        VALUES ( ? )
	"""

    cursor.execute(query, (podkladka,))

    conn.commit()
    conn.close()

def add_mieso(mieso):
    conn = sqlite3.connect(DB_DIR)

    cursor = conn.cursor()

    query = """
	    INSERT INTO mieso(nazwa)
	    	        VALUES ( ? )
	"""

    cursor.execute(query, (mieso,))

    conn.commit()
    conn.close()

def add_dodatki(dodatki):
    conn = sqlite3.connect(DB_DIR)

    cursor = conn.cursor()

    query = """
	    INSERT INTO dodatki(nazwa)
	    	        VALUES ( ?)
	"""

    cursor.execute(query, (dodatki,))

    conn.commit()
    conn.close()

def update_obiad(podkladka, mieso, dodatki):
    conn = sqlite3.connect(DB_DIR)

    cursor = conn.cursor()

    query = """
	    UPDATE obiad
	    SET podkladka = ?, mieso = ?, dodatki =?
	"""

    cursor.execute(query, (podkladka, mieso, dodatki))

    conn.commit()
    conn.close()


def delete_obiad(id):
    conn = sqlite3.connect(DB_DIR)

    cursor = conn.cursor()

    query = f"""
        DELETE
        FROM dodatkiobiadrelation
        WHERE fk_obiad = {id}"""

    cursor.execute(query)
    conn.commit()

    conn = sqlite3.connect(DB_DIR)

    cursor = conn.cursor()
    query = f"""
        DELETE
        FROM obiad
        WHERE id_obiad = {id}"""
    cursor.execute(query)
    conn.commit()
    conn.close()

def delete_dodatki(id):

    conn = sqlite3.connect(DB_DIR)

    cursor = conn.cursor()

    query = f"""
        DELETE
        FROM dodatkiobiadrelation
        WHERE fk_dodatki = {id}"""

    cursor.execute(query)
    conn.commit()

    conn = sqlite3.connect(DB_DIR)

    cursor = conn.cursor()
    query = f"""
            DELETE
            FROM dodatki
            WHERE id_dodatki = {id}"""
    cursor.execute(query)
    conn.commit()
    conn.close()

def get_db_podkladka():
    conn = sqlite3.connect(DB_DIR)

    cursor = conn.cursor()

    query = """
    	    SELECT *
    	    FROM podkladka
    	"""
    lista = []
    cursor.execute(query)
    all_rows = cursor.fetchall()
    for row in all_rows:
        lista.append([row[0], row[1]])
    #one_row = cursor.fetchone()
    conn.commit()
    conn.close()
    return lista

def get_relation_obiad(id_obiad):
    conn = sqlite3.connect(DB_DIR)

    cursor = conn.cursor()

    query = f"""
     	    SELECT *
     	    FROM dodatkiobiadrelation
     	    WHERE fk_obiad={id_obiad}
     	"""
    lista = []
    cursor.execute(query)
    all_rows = cursor.fetchall()
    for row in all_rows:
        lista.append(get_dodatki_name(row[0]))
    # one_row = cursor.fetchone()
    conn.commit()
    conn.close()
    return lista
def list_to_string(list_in):
    print(list_in)
    str_out=""
    for ele in list_in:
        str_out += str(ele)
    return str_out
def get_db_mieso():
    conn = sqlite3.connect(DB_DIR)

    cursor = conn.cursor()

    query = """
    	    SELECT *
    	    FROM mieso
    	"""
    lista2 = []
    cursor.execute(query)
    all_rows = cursor.fetchall()
    for row in all_rows:
        lista2.append([row[0], row[1]])
    #one_row = cursor.fetchone()
    conn.commit()
    conn.close()
    return lista2

def get_db_dodatki():
    conn = sqlite3.connect(DB_DIR)

    cursor = conn.cursor()

    query = """
    	    SELECT *
    	    FROM dodatki
    	"""
    lista3 = []
    cursor.execute(query)
    all_rows = cursor.fetchall()
    for row in all_rows:
        lista3.append([row[0], row[1]])
    #one_row = cursor.fetchone()
    conn.commit()
    conn.close()
    return lista3

def get_db_obiad():
    conn = sqlite3.connect(DB_DIR)

    cursor = conn.cursor()

    query = """
    	    SELECT *
    	    FROM obiad
    	"""
    lista4 = []
    cursor.execute(query)
    all_rows = cursor.fetchall()
    for row in all_rows:
        lista4.append([row[0], row[1], get_podkladka_name(row[2]), get_mieso_name(row[3]), get_relation_obiad(row[0])])
    #one_row = cursor.fetchone()
    #one_row = cursor.fetchone()
    conn.commit()
    conn.close()
    return lista4

def get_podkladka_name(id):
    conn = sqlite3.connect(DB_DIR)

    cursor = conn.cursor()

    query = f"""
               	    SELECT *
               	    FROM podkladka
               	    WHERE id_podkladka = {id}
               	"""
    cursor.execute(query)
    #all_rows = cursor.fetchall()
    one_row = cursor.fetchone()
    conn.commit()
    conn.close()
    return one_row[1]
def get_mieso_name(id):
    conn = sqlite3.connect(DB_DIR)

    cursor = conn.cursor()

    query = f"""
           	    SELECT *
           	    FROM mieso
           	    WHERE id_mieso = {id}
           	"""
    cursor.execute(query)
    #all_rows = cursor.fetchall()
    one_row = cursor.fetchone()
    conn.commit()
    conn.close()
    return one_row[1]
def get_dodatki_name(id):
    conn = sqlite3.connect(DB_DIR)

    cursor = conn.cursor()

    query = f"""
        	    SELECT *
        	    FROM dodatki
        	    WHERE id_dodatki = {id}
        	"""
    cursor.execute(query)
    one_row = cursor.fetchone()
    conn.commit()
    conn.close()
    return one_row[1]

def read_data():
    obiady = get_db_obiad()
    for obiad in obiady:
        print(obiad)

# + moze funkcja na sortowanie???
def validate_sql_safe(slowo):

    forbidden_inputs = ["update", "remove", "drop", "table", "*", "from", "'", "select", "insert", ";", "add", "delete" ]
    new_slowo = slowo.lower()
    if not new_slowo:
        print("Error: empty word")
        return False
    elif new_slowo.isnumeric():
        print("Error: numeric type")
        return False
    else:
        if any(ele in new_slowo for ele in forbidden_inputs):
            print("Error: illegal input")
            return False
        else:
            return True

# def select():
#     choice = input("1. Create\n2. Read\n3. Update\n4. Delete\n5. Exit\n\n")
#     if choice == "1":
#         odp = input("insert new position for category:podkladka\n")
#         if validate_sql_safe(odp):
#             add_podkladka(odp)
#         odp2 = input("insert new position for category:mieso\n")
#         if validate_sql_safe(odp):
#             add_mieso(odp2)
#         odp3 = input("insert new position for category:dodatki\n")
#         if validate_sql_safe(odp):
#             add_dodatki(odp3)
start()


def add_dodatkiobiadrelation(id_dodatki, id_obiad):

    conn = sqlite3.connect(DB_DIR)

    cursor = conn.cursor()

    query = """
	    INSERT INTO dodatkiobiadrelation(fk_dodatki, fk_obiad)
	    	        VALUES ( ?,?)
	"""

    cursor.execute(query, (id_dodatki, id_obiad))

    conn.commit()
    conn.close()

def seed_db():
    add_dodatki("pomidor")
    add_dodatki("burak")
    add_dodatki("ogórek")
    add_mieso("zraz")
    add_mieso("schab")
    add_mieso("kurczak")
    add_podkladka("pyra")
    add_podkladka("kluska")
    add_dodatkiobiadrelation(1,1)
    add_dodatkiobiadrelation(2,1)
    add_dodatkiobiadrelation(1,2)
    add_obiad(1, 1, "pierwszy")
    add_obiad(1,2, "drugi")
    add_obiad(2,2, "trzeci")


def clear_databse():
    pass
start()
#seed_db()

#print(get_db_podkladka())
#print(len(LIST_PODKLADKA))
print(get_db_dodatki())
# add_dodatki("dod4")
# add_dodatki("dod5")
# add_dodatki("dod6")
# add_dodatki("dod7")
# add_dodatki("miłosc")
# add_dodatki("slicznosci")
# add_dodatki("slodkosci")
# add_dodatki("cukier")
