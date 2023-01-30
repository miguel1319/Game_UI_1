import pyodbc as odbc
# make connection to SQL Server

DRIVER_NAME = 'SQL Server Native Client 11.0'
SERVER_NAME = 'DESKTOP-JIJA9GT'
DATABASE_NAME = 'VideoGames'

connection_string = f"""
    Driver={{{DRIVER_NAME}}};
    Server={SERVER_NAME};
    Database={DATABASE_NAME};
    Trusted_Connection=yes;
"""
conn = odbc.connect(connection_string)
print(conn)

def test_find(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Video_Games")
    count = 0
    word = 20
    final_str = ""
    for row in cursor:
        if word < row[2]:
            print(row)




