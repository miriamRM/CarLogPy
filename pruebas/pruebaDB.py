"""Prueba para la conexion de base de datos con python y sqlite"""
import sqlite3

SQLCreateStyles = """CREATE TABLE IF NOT EXISTS Styles(
                Id INTEGER NOT NULL PRIMARY KEY,
                Style TEXT NOT NULL)"""
SQLCreateMakes = """CREATE TABLE IF NOT EXISTS Makes(
                Id INTEGER NOT NULL PRIMARY KEY,
                Make TEXT NOT NULL)"""
SQLCreateModel = """CREATE TABLE IF NOT EXISTS Model(
                Id INTEGER NOT NULL PRIMARY KEY,
                MakeId INTEGER NOT NULL,
                Model TEXT NOT NULL,
                FOREIGN KEY(MakeId) REFERENCES Makes(Id))"""
SQLCreateCars = """CREATE TABLE IF NOT EXISTS Cars(
                Id INTEGER NOT NULL PRIMARY KEY,
                MakeId INTEGER NOT NULL,
                ModelId INTEGER NOT NULL,
                Year INTEGER NOT NULL,
                StyleId INTEGER NOT NULL,
                FOREIGN KEY(StyleId) REFERENCES Styles(Id),
                FOREIGN KEY(MakeId) REFERENCES Makes(Id),
                FOREIGN KEY(ModelId) REFERENCES Model(Id))"""
SQLCreateSpecialty = """CREATE TABLE IF NOT EXISTS Specialty(
                Id INTEGER NOT NULL PRIMARY KEY,
                Specialty TEXT NOT NULL)"""
SQLCreateMechanic = """CREATE TABLE IF NOT EXISTS Mechanic(
                Id INTEGER NOT NULL PRIMARY KEY,
                WorkshopName TEXT NOT NULL,
                MechanicName TEXT NOT NULL,
                SpecialtyId INTEGER NOT NULL,
                Address TEXT,
                Phone INTEGER NOT NULL,
                FOREIGN KEY(SpecialtyId) REFERENCES Specialty(Id))"""
SQLCreateLog = """CREATE TABLE IF NOT EXISTS Log(
                Id INTEGER NOT NULL PRIMARY KEY,
                CarId INTEGER NOT NULL,
                MechanicId INTEGER NOT NULL,
                Problem TEXT NOT NULL,
                Solution TEXT NOT NULL,
                Date DATETIME NOT NULL, 
                NextDate DATETIME,
                FOREIGN KEY(CarId) REFERENCES Cars(Id),
                FOREIGN KEY(MechanicId) REFERENCES Mechanic(Id))"""
CreateTables = [SQLCreateStyles, SQLCreateMakes, SQLCreateModel, SQLCreateCars, SQLCreateSpecialty, SQLCreateMechanic, SQLCreateLog]

try:
	conn = sqlite3.connect("test.db")

except Exception  as err:
	print "Error" + err  

else:
	cursor = conn.cursor()
	for sql in CreateTables:
		cursor.execute(sql)
	conn.commit()
    
finally:
	conn.close()


