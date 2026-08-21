from flask import Flask
from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv()

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )


@app.route("/")
def home():
    return "LifeLink Blood Donation System"


@app.route("/test-db")
def test_db():
    connection = get_db_connection()

    if connection.is_connected():
        connection.close()
        return "MySQL Connection Successful!"

    return "MySQL Connection Failed!"


if __name__ == "__main__":
    app.run(debug=True)