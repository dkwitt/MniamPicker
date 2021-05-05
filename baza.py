import sqlite3


# 1. STWORZENIE BAZY I POŁĄCZENIE JEJ
# 2. NAPISANIE FUNKCJI CREATE/ADD? OBIAD/PODL/DOD
# 3. FUNKCJA READ
# 4. FUNKCJA UPDATE
# 5. FUNKCJA DELETE

def start():
    connection = sqlite3.connect('testdb4.sqlite')

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
    	    	id_obiad INTEGER PRIMARY KEY,
    	    	nazwa VARCHAR(50),
    	    	id_podkladka INTEGER NOT NULL,
    	    	id_mieso INTEGER NOT NULL,
    	    	id_dodatki INTEGER NOT NULL,
    	    	FOREIGN KEY(id_podkladka) REFERENCES podkladka (id_podkladka),
    	    	FOREIGN KEY(id_mieso) REFERENCES mieso (id_mieso),
    	    	FOREIGN KEY(id_dodatki) REFERENCES dodatki (id_dodatki)
    	    )
    	"""

    cursor.execute(query)

    connection.commit()
    connection.close()




def add_obiad(podkladka, mieso, dodatki, nazwa):
    conn = sqlite3.connect('testdb4.sqlite')

    cursor = conn.cursor()
    if validate_sql_safe(nazwa):

        query = """
            INSERT INTO obiad(nazwa, id_podkladka, id_mieso, id_dodatki )
                        VALUES ( ?,?,?,? )
        """

        cursor.execute(query, (nazwa, podkladka, mieso, dodatki))

        conn.commit()
    else:
        print("Niepoprawna nazwa obaidu")
    conn.close()

def add_podkladka(podkladka):
    conn = sqlite3.connect('testdb4.sqlite')

    cursor = conn.cursor()

    query = """
	    INSERT INTO podkladka(nazwa)
	    	        VALUES ( ? )
	"""

    cursor.execute(query, (podkladka,))

    conn.commit()
    conn.close()

def add_mieso(mieso):
    conn = sqlite3.connect('testdb4.sqlite')

    cursor = conn.cursor()

    query = """
	    INSERT INTO mieso(nazwa)
	    	        VALUES ( ? )
	"""

    cursor.execute(query, (mieso,))

    conn.commit()
    conn.close()

def add_dodatki(dodatki):
    conn = sqlite3.connect('testdb4.sqlite')

    cursor = conn.cursor()

    query = """
	    INSERT INTO dodatki(nazwa)
	    	        VALUES ( ?)
	"""

    cursor.execute(query, (dodatki,))

    conn.commit()
    conn.close()

def update_obiad(podkladka, mieso, dodatki):
    conn = sqlite3.connect('testdb4.sqlite')

    cursor = conn.cursor()

    query = """
	    UPDATE obiad
	    SET podkladka = ?, mieso = ?, dodatki =?
	"""

    cursor.execute(query, (podkladka, mieso, dodatki))

    conn.commit()
    conn.close()


def delete_obiad():
    conn = sqlite3.connect('testdb4.sqlite')

    cursor = conn.cursor()

    query = """
        DELETE *
        FROM obiad
        WHERE nazwa = ?"""
    cursor.execute(query)
    all_rows = cursor.fetchall()
    one_row = cursor.fetchone()

    conn.commit()
    conn.close()
    # return all_rows / one_row

def get_obiad():
	conn = sqlite3.connect('testdb4.sqlite')

	cursor = conn.cursor()

	query = """
	    SELECT *
	    FROM obiad
	"""

	cursor.execute(query)
	all_rows = cursor.fetchall()
    # + one_row z fetchone?
	conn.commit()
	conn.close()

	return all_rows


def read_data():
    obiady = get_obiad()
    for obiad in obiady:
        print(obiad)

# + moze funkcja na sortowanie???
def validate_sql_safe(slowo):

    forbidden_inputs = ["update", "remove", "drop", "table", "*", "from", "'", "select", "insert", ";", "add", "delete" ]
    new_slowo = slowo.lower()
    if not new_slowo:
        print("error empty word")
        return False
    elif new_slowo.isnumeric():
        print("error numeric type")
        return False
    else:
        if any(ele in new_slowo for ele in forbidden_inputs):
            print("illegal")
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

def seed_db():
    add_dodatki("pomidor")
    add_dodatki("burak")
    add_dodatki("ogórek")
    add_mieso("zraz")
    add_mieso("schab")
    add_mieso("kurczak")
    add_podkladka("pyra")
    add_podkladka("kluska")
    add_obiad(1,1,2,"pierwszy")

def clear_databse():

seed_db()