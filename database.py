import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="hNk*EH!245",
    database="NHANESdatabase"
)

mycursor = db.cursor()
