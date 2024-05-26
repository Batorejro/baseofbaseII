import sqlite3

"""
conn = sqlite3.connect('clean_m.db')
cur = conn.cursor() 
conn.execute("SELECT * FROM clean LIMIT 2")


rows = cur.fetchall()
print(rows)

for row in rows:
    print(row)

conn.close()
"""

def getVRows():
    try:
        conn = sqlite3.connect('clean_m.db')
        cur = conn.cursor()
        print("Połączono z BAZĄ")

        sqlite_select_query = ("SELECT * from clean LIMIT 5")
        cur.execute(sqlite_select_query)
        records = cur.fetchall()

        for row in records:
            print(row)# prostszy i szybszy sposób
            #print("station: ", row[0])
            #print("date: ", row[1])
            #print("precip: ", row[2])
            #print("tobs: ", row[3])
            print("\n")

        cur.close()

    finally:
        if conn:
            conn.close()
            print("Bela Lugosi is dead ")

getVRows()