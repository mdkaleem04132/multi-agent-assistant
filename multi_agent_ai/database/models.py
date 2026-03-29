from database.db_connector import connect_db

class BaseModel:
    """Base class for all database models to handle MySQL operations."""

    def __init__(self, table_name):
        self.connection = connect_db()
        self.table_name = table_name

    def execute(self, query, params=None):
        cursor = self.connection.cursor()
        cursor.execute(query, params or ())
        self.connection.commit()
        cursor.close()

    def fetchall(self, query, params=None):
        cursor = self.connection.cursor()
        cursor.execute(query, params or ())
        result = cursor.fetchall()
        cursor.close()
        return result