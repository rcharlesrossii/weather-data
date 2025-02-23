import sqlite3


# Open a new database connection
con = sqlite3.connect("weather.db")

# Create a cursor object
cur = con.cursor()
# Create a new database table
cur.execute("CREATE TABLE weather(clouds, datetime, max_temp, min_temp, pop, precip, rh, snow, temp, weather)")

