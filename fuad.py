import mysql
import mysql.connector
hostname = "127.0.0.1"
username = "root"
password = "31.Fuad10"

try:
    connection = mysql.connector.connect(host=hostname, port=3306, user=username, password=password)
  
    if connection.is_connected():
        print("Connected to MySQL database")
    else:
        print("Failed to connect to MySQL database")
except mysql.connector.Error as e:
    print(f"Error connecting to MySQL database: {e}")