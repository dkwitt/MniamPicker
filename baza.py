import sqlite3

DB_DIR = 'C:\\Users\\Dominika\\Mniam\\MniamPicker\\testdb5.sqlite'


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


############################## FUNKCJA ADD ##############################

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
        # print("Niepoprawna nazwa obiadu")
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


############################## FUNKCJA UPDATE ##############################

def update_obiad(nazwa, id_obiad, id_podkladka, id_mieso, id_dodatki_new, id_dodatki_old):
    conn = sqlite3.connect(DB_DIR)

    cursor = conn.cursor()

    query = f"""
        UPDATE obiad
        SET nazwa = ?, id_podkladka = ?, id_mieso = ? 
        WHERE id_obiad = {id_obiad}
        """
    cursor.execute(query, (nazwa, id_podkladka, id_mieso))

    lista_do_usuniecia = [ele for ele in id_dodatki_old if ele not in id_dodatki_new]
    lista_do_dodania = [ele for ele in id_dodatki_new if ele not in id_dodatki_old]

    print(lista_do_usuniecia, "usuniecia", "\n", lista_do_dodania, "dodania")
    for ele in lista_do_usuniecia:
        query = f"""
        DELETE
        FROM dodatkiobiadrelation
        WHERE fk_obiad = {id_obiad} AND fk_dodatki = {ele} 
        """

        cursor.execute(query)

    for ele in lista_do_dodania:
        query = f"""
        INSERT INTO dodatkiobiadrelation(fk_obiad, fk_dodatki )
                        VALUES ({id_obiad}, {ele})
        """

        cursor.execute(query)

    conn.commit()
    conn.close()


def update_podkladka(podkladka, id):
    conn = sqlite3.connect(DB_DIR)

    cursor = conn.cursor()

    query = """
	    UPDATE podkladka
	    SET nazwa = ?
	    WHERE id_podkladka = ?
	"""
    cursor.execute(query, (podkladka, id))

    conn.commit()
    conn.close()


def update_mieso(mieso, id):
    conn = sqlite3.connect(DB_DIR)

    cursor = conn.cursor()

    query = """
	    UPDATE mieso
	    SET nazwa = ?
	    WHERE id_mieso = ?
	"""

    cursor.execute(query, (mieso, id))

    conn.commit()
    conn.close()


def update_dodatki(dodatki, id):
    conn = sqlite3.connect(DB_DIR)

    cursor = conn.cursor()

    query = """
	    UPDATE dodatki
	    SET nazwa =?
	    WHERE id_dodatki = ?
	"""

    cursor.execute(query, (dodatki, id))

    conn.commit()
    conn.close()


############################## FUNKCJA DELETE ##############################

def delete_podkladka(id):
    conn = sqlite3.connect(DB_DIR)

    cursor = conn.cursor()

    query = f"""
            DELETE
            FROM podkladka
            WHERE id_podkladka = {id}"""

    cursor.execute(query)
    conn.commit()
    conn.close()


def delete_mieso(id):
    conn = sqlite3.connect(DB_DIR)

    cursor = conn.cursor()

    query = f"""
                DELETE
                FROM mieso
                WHERE id_mieso = {id}"""

    cursor.execute(query)
    conn.commit()
    conn.close()


def delete_from_db(id, table_name):
    if table_name == "obiad":
        delete_obiad(id)
    elif table_name == "podkladka":
        delete_podkladka(id)
    elif table_name == "mieso":
        delete_mieso(id)
    elif table_name == "dodatki":
        delete_dodatki(id)


def delete_obiad(id):
    conn = sqlite3.connect(DB_DIR)

    cursor = conn.cursor()

    query = f"""
        DELETE
        FROM dodatkiobiadrelation
        WHERE fk_obiad = {id}"""

    cursor.execute(query)
    conn.commit()

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


############################## POBIERANIE DANYCH ##############################
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
    # one_row = cursor.fetchone()
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
    # one_row = cursor.fetchone()
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
    # one_row = cursor.fetchone()
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
    # one_row = cursor.fetchone()
    # one_row = cursor.fetchone()
    conn.commit()
    conn.close()
    return lista4


def get_obiad_name(id):
    conn = sqlite3.connect(DB_DIR)

    cursor = conn.cursor()

    query = f"""
               	    SELECT nazwa
               	    FROM obiad
               	    WHERE id_obiad = {id}
               	"""
    cursor.execute(query)
    # all_rows = cursor.fetchall()
    one_row = cursor.fetchone()
    conn.commit()
    conn.close()
    return one_row[0]


def get_podkladka_name(id):
    conn = sqlite3.connect(DB_DIR)

    cursor = conn.cursor()

    query = f"""
               	    SELECT *
               	    FROM podkladka
               	    WHERE id_podkladka = {id}
               	"""
    cursor.execute(query)
    # all_rows = cursor.fetchall()
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
    # all_rows = cursor.fetchall()
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


def get_id_from_obiad(id):
    conn = sqlite3.connect(DB_DIR)

    cursor = conn.cursor()

    query = f"""
        	    SELECT id_podkladka, id_mieso
        	    FROM obiad
        	    WHERE id_obiad = {id}
        	"""
    lista2 = []
    cursor.execute(query)
    all_rows = cursor.fetchall()
    for row in all_rows:
        lista2.append([row[0], row[1]])
    # one_row = cursor.fetchone()
    conn.commit()
    conn.close()
    return lista2


def get_id_from_dodatkiobiadrelation(id):
    conn = sqlite3.connect(DB_DIR)

    cursor = conn.cursor()

    query = f"""
        	    SELECT fk_dodatki
        	    FROM dodatkiobiadrelation
        	    WHERE fk_obiad = {id}
        	"""
    lista2 = []
    cursor.execute(query)
    all_rows = cursor.fetchall()
    for row in all_rows:
        lista2.append(row[0])
    # one_row = cursor.fetchone()
    conn.commit()
    conn.close()
    return lista2


def validate_sql_safe(slowo):
    forbidden_inputs = ["update", "remove", "drop", "table", "*", "from", "'", "select", "insert", ";", "add", "delete"]
    new_slowo = slowo.lower()
    if not new_slowo:
        # print("Error: empty word")
        return False
    elif new_slowo.isnumeric():
        # print("Error: numeric type")
        return False
    else:
        if any(ele in new_slowo for ele in forbidden_inputs):
            # print("Error: illegal input")
            return False
        else:
            return True


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
    add_dodatki("x")
    add_dodatki("y")
    add_dodatki("z")
    add_mieso("zraz")
    add_mieso("schab")
    add_mieso("kurczak")
    add_podkladka("pyra")
    add_podkladka("kluska")
    add_dodatkiobiadrelation(1, 1)
    add_dodatkiobiadrelation(2, 1)
    add_dodatkiobiadrelation(1, 2)
    add_obiad(1, 1, "pierwszy")
    add_obiad(1, 2, "drugi")
    add_obiad(2, 2, "trzeci")


start()
# seed_db()
