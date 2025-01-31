import sqlite3
from unittest import case


def isValidSQLType(type:str) -> bool:
    if type in ["TEXT", "REAL", "INTEGER", "BLOB"]:
        return True
    else:
        return False

def isValidSQLModifier(modifier:str) -> bool:
    match modifier:
        case "NOT NULL":
            return True
        case str() as modifier if modifier.startswith("DEFAULT "):
            modifier.replace("DEFAULT ", "")
            if modifier.isdigit():
                return True
            else:
                return False
        case "PRIMARY KEY":
            return True
        case "UNIQUE":
            return True
        case "AUTOINCREMENT":
            return True
        case str() as modifier if modifier.startswith("CHECK("):
            modifier.replace("CHECK(", "")
            if modifier.endswith(")"):
                return True
            else:
                return False
        case str() as modifier if modifier.startswith("REFERENCE "):
            modifier.replace("REFERENCE ", "")



class Database:
    def __init__(self, db_name:str):
        self.name = db_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def __str__(self):
        return self.name

    def __del__(self):
        self.connection.close()

    def close(self):
        self.connection.close()

    def create_table(self, table_name:str, column_def:tuple[dict[str, str], ...], existence_check:bool=False):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
        columns = []
        if table_name.isidentifier():
            raise ValueError("Invalid table name")
        try:
            for i, d in enumerate(column_def):
                column_count = len(column_def)
                column_name = d.get('column_name')
                column_type = d.get('type')
                column_constraints = d.get('constraints')
                if not column_name.isidentifier():
                    raise ValueError("Invalid column name")

                if not column_constraints:
                    column_constraints = ''

                if i < column_count - 1:
                    column = f"{column_name} {column_type} {column_constraints},"
                else:
                    column = f"{column_name} {column_type} {column_constraints});"
                columns.append(column)
            self.cursor.execute(query + " ".join(columns))
            self.connection.commit()
        except Exception as e:
            print(e)

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

test = Database("test.db")
test.create_table("test", (
    {"name": "id", "type": "INTEGER"},
    {"name": "name", "type": "TEXT", "constraints": "NOT NULL"},
    {"name": "waga", "type": "TEXT", "constraints": "NOT NULL"},
    )
)
test.close()

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
