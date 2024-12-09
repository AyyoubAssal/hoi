print('hoi')

import pandas as pd
import pyodbc

df = pd.read_csv('C:\DamenTraineeship\corona_cleaned.csv')

print(df)

# Stap 2: Verbinding maken met Azure SQL Database
server = 'datadbserverdamen.database.windows.net'  # Azure servernaam
database = 'db - ayyoub'                  # Naam van de database
username = 'admindamen'                       # Gebruikersnaam
password = 'uiop7890UIOP&*()'                       # Wachtwoord
driver = '{ODBC Driver 17 for SQL Server}'       # Zorg dat de juiste driver is geïnstalleerd

connection_string = f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}'

# Maak een verbinding
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

teller=0


# Stap 4: Data invoegen in de tabel
for index, row in df.iterrows():
    teller += 1
    if teller > 5:
        break
    SQL = f"""
    INSERT INTO dbo.corona_cleaned (Column1, Column2, Column3, column4) 
    VALUES (?, ?, ?)
    """, row['Entity'], row['Code'], row['Day'], row['Daily new confirmed deaths due to COVID-19 per million people (rolling 7-day average, right-aligned)']  # Pas kolomnamen aan op basis van je CSV
    print(SQL)
    #cursor.execute(SQL)
#conn.commit()


