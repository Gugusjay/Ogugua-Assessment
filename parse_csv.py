import csv
import sqlite3

# Open the connection to the database
conn = sqlite3.connect('exoplanets.db')
cur = conn.cursor()

# open the data from the table so that if we rerun the file, we don't repeat values
conn.execute('DROP TABLE IF EXISTS stars')
conn.execute('DROP TABLE IF EXISTS planets')
print("table dropped successfully");

# Create the stars table
conn.execute('CREATE TABLE stars (name TEXT, distance INTEGER, stellar_magnitude REAL, discovery_year INTEGER, mass_multiplier REAL, radius_multiplier REAL)')
print("table created successfully");

# Create the planets table
conn.execute('CREATE TABLE planets (planet_type TEXT, mass_wrt TEXT, orbital_period REAL, orbital_radius REAL, eccentricity REAL, detection_method TEXT)')
print("table created successfully");


# open the file to read it into the database
with open('exoplanets.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    for row in reader:
        print(row)

        name = row[0]
        distance = row[1]
        stellar_magnitude = row[2]
        discovery_year = int(row[4])
        mass_multiplier = (row[5])
        radius_multiplier = (row[7])
    

        cur.execute('INSERT INTO stars VALUES (?,?,?,?,?,?)', (name, distance, stellar_magnitude, discovery_year, mass_multiplier,radius_multiplier ))
        conn.commit()
print("data parsed successfully");

with open('exoplanets.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    for row in reader:
        print(row)

        planet_type = row[3]
        mass_wrt = (row[6])
        orbital_period = (row[10])
        orbital_radius = (row[9])
        eccentricity = (row[11])
        detection_method = row[10]
        

        cur.execute('INSERT INTO planets VALUES (?,?,?,?,?,?)', (planet_type, mass_wrt, orbital_period, orbital_radius, eccentricity, detection_method))
        conn.commit()
print("data parsed successfully");

#conn.close()
# Commit the changes and close the database connection
conn.commit()
print("data parsed successfully")
conn.close()
