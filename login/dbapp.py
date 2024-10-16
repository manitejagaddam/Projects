import mysql.connector
from mysql.connector import Error
import bcrypt


class dbmanager:
    
    def __init__(self) -> None:
        self.password = 'Maniteja@1107'
        self.user = 'root'
        self.host = 'localhost'
        self.database = 'app'
        

    def check_db(self, username, password):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if connection.is_connected():
                cursor = connection.cursor()
                query = 'SELECT password FROM login_info WHERE username = %s'
                cursor.execute(query, (username,))
                result = cursor.fetchone()
                if result:
                    print(list(result))
                    print(password)
                    if(list(result)[0] == password):
                        print("password is correct")
                    else:
                        print("password is worng")
                    if list(result)[0] == password:
                        return True
                return False
            
        except Error as e:
            print(f"Error: {e}")
            return 0
        
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()

    def add_user(self, name, username, password):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if connection.is_connected():
                cursor = connection.cursor()
                # hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                query = 'INSERT INTO login_info (name, username, password) VALUES (%s, %s, %s)'
                cursor.execute(query, (name, username, password))
                connection.commit()
                
        except Error as e:
            print(f"Error: {e}")
            
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()
