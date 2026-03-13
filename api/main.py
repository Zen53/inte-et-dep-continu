import mysql.connector
import os
import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db_connection():
    """Create a connection to the database with retry logic."""
    max_retries = 30
    for attempt in range(max_retries):
        try:
            conn = mysql.connector.connect(
                database=os.getenv("MYSQL_DATABASE"),
                user=os.getenv("MYSQL_USER"),
                password=os.getenv("MYSQL_ROOT_PASSWORD"),
                port=3306,
                host=os.getenv("MYSQL_HOST")
            )
            print(f"Connected to MySQL on attempt {attempt + 1}")
            return conn
        except mysql.connector.Error as e:
            print(f"Attempt {attempt + 1}/{max_retries} - MySQL not ready: {e}")
            if attempt < max_retries - 1:
                time.sleep(3)
    raise Exception("Could not connect to MySQL after multiple retries")

conn = get_db_connection()

@app.get("/users")
async def get_users():
    cursor = conn.cursor()
    sql_select_Query = "select * from utilisateur"
    cursor.execute(sql_select_Query)

    # get all records
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)

    # renvoyer nos données et 200 code OK
    return {'utilisateurs': records}
