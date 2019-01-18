import sqlite3

def get_data_from_database():
  

    conn = sqlite3.connect('test.db')

    conn.execute('''CREATE TABLE COMPANY
            (ID INT PRIMARY KEY     NOT NULL,
            NAME           TEXT    NOT NULL,
            AGE            INT     NOT NULL,
            ADDRESS        CHAR(50),
            SALARY         REAL);''')
    print "Table created successfully"

    conn.close()