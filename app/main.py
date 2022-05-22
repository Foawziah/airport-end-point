# importing libraries
import pandas as pd
import sqlite3
from fastapi import FastAPI, status

# converting sql data to json format
def sql_data_to_json(data):
    data_json = []
    header = [i[0] for i in cursor.description]
    for i in data:
        data_json.append(dict(zip(header, i)))
    return data_json

# search airport by iata
def search_by_iata(cursor, iata):
    cursor.execute("SELECT name, iata, city, country, latitude, longitude FROM airports WHERE iata LIKE '%{}%'".format(iata))
    data = cursor.fetchall()
    return sql_data_to_json(data)

# search airport by name
def search_by_name(cursor, name):
    cursor.execute("SELECT name, iata, city, country, latitude, longitude FROM airports WHERE name LIKE '%{}%'".format(name))
    data = cursor.fetchall()
    return sql_data_to_json(data)

# creating fastapi app
app = FastAPI()

# connecting to the database
conn = sqlite3.connect('airports.db', check_same_thread=False)

# importing data from csv file
df = pd.read_csv("https://davidmegginson.github.io/ourairports-data/airports.csv")

# dropping all rows with null iata_code
df = df.dropna(subset=['iata_code'])

# reseting index
df.reset_index(drop=True, inplace=True)

# creating database from dataframe
df.to_sql("airports", conn, if_exists="replace", index=False)

# creating cursor
cursor = conn.cursor()

# renaming columns
cursor.execute("ALTER TABLE airports RENAME COLUMN iata_code TO iata")
cursor.execute("ALTER TABLE airports RENAME COLUMN municipality TO city")
cursor.execute("ALTER TABLE airports RENAME COLUMN iso_country TO country")
cursor.execute("ALTER TABLE airports RENAME COLUMN latitude_deg TO latitude")
cursor.execute("ALTER TABLE airports RENAME COLUMN longitude_deg TO longitude")

@app.get("/", status_code=200)
def read_root():
    return {"message": "Welcome to the airport search API"}

@app.get("/search_name", status_code=200)
def search_name(name: str):
    data = search_by_name(cursor, name)
    if data:
        return data
    else:
        error = {status.HTTP_204_NO_CONTENT: "No data found"}
        return error

@app.get("/search_iata", status_code=200)
def search_iata_code(code: str):
    data = search_by_iata(cursor, code)
    if data:
        return data
    else:
        error = {status.HTTP_204_NO_CONTENT: "No data found"}
        return error