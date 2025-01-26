from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    try:
        connection = mysql.connector.connect(
            host="custom_mysql",  # MySQL 컨테이너 이름
            user="my_user",
            password="my_password",
            database="my_database"
        )
        if connection.is_connected():
            return "Connected successfully to the database!"
    except Exception as e:
        return f"Database connection failed: {str(e)}"
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

