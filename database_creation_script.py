import sqlite3

sqliteConnection = sqlite3.connect('student_database.db')
cursor = sqliteConnection.cursor()
print("Database created and connected sucessfully")

try:
    sqlite_create_table_query = '''CREATE TABLE record (   name TEXT,
                                                            roll INTEGER,
                                                            course TEXT,
                                                            age INTEGER,
                                                            dob TEXT);'''

    cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit()
    print("Table is created")
    cursor.close()

except sqlite3.Error as error:
    print("error is ",error)