import mysql.connector as connector
from mysql.connector import errors
database = None
try:
    # Try to establish the connection
    database = connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="py24",
        port=3306
    )
    print("Connection Established")

except errors.InterfaceError as err:
    print(f"invalid port no: {err}")
    # This handles errors like 'Can't connect to MySQL server on 'localhost:3305' (10061)'
except errors.ProgrammingError as err:
    print(f"invalid database name (database does not exists) {err}")
    # This handles errors like 'Unknown database 'py2'' or 'Access denied'
except errors.NotSupportedError as err:
    print(f"invalid password for user: {err}")
    # This handles errors like 'Authentication plugin 'caching_sha2_password' is not supported'
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    # This catches any other exceptions not specifically handled above

#create function to run insert, update, delete sql command
def RunQuery(sql,data):
    isSuccess = False
    try:
        mycursor = database.cursor()
        mycursor.execute(sql,data);
        database.commit()
        isSuccess = True
    except errors.ProgrammingError as err:
        print(sql,data)
        print(err)
    except mysql.connector.errors.DataError as err:
        print(sql,data)
        print(err)
    finally:
        return isSuccess
def fetchTable(sql,data=None):
    mycursor = database.cursor(dictionary=True)
    if data==None:
        mycursor.execute(sql)
    else:
        mycursor.execute(sql,data)
    tables = mycursor.fetchall()
    return tables