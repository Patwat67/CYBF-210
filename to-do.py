import sqlite3

class Database:
    def __init__(self, db_name:str):
        self.name = db_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def __str__(self):
        return self.name

    def __del__(self):
        self.connection.close()

    def create_table(self, ):
        print('hi babe')

    def fetch(self, query:str, num_rows:int):
        self.cursor.execute(query)
        if num_rows == 1:
           return self.cursor.fetchone()
        if num_rows > 1:
            return self.cursor.fetchmany(num_rows)
        else:
            return self.cursor.fetchall()

    def commit(self):
        self.connection.commit()

# #Full List of Parameters (Categorized)
# 1. Data Types
#
#     INTEGER
#     TEXT
#     REAL
#     BLOB
#     NUMERIC
#
# 2. Constraints
#
#     PRIMARY KEY
#     AUTOINCREMENT
#     NOT NULL
#     UNIQUE
#     CHECK(expression)
#     DEFAULT value
#     REFERENCES table(column)
#     FOREIGN KEY(column) REFERENCES table(column)
#     COLLATE collation_name
#     DEFERRABLE
#     INITIALLY DEFERRED
#     INITIALLY IMMEDIATE
#
# 3. Column Options
#
#     AUTOINCREMENT
#     ROWID (default if no primary key is defined)
#
# 4. Other Settings
#
#     WITHOUT ROWID
#     DEFERRABLE
#     INITIALLY DEFERRED
#     INITIALLY IMMEDIATE
