# db.py
from flask_mysqldb import MySQL

def initialize_database(mysql, db_name, sql_file):
    cursor = None
    try:
        cursor = mysql.connection.cursor()
        with open(sql_file, 'r') as file:
            sql_commands = file.read()
        cursor.execute(sql_commands)
        mysql.connection.commit()
    except Exception as e:
        print(f"Error during database initialization: {e}")
    finally:
        if cursor:
            cursor.close()

