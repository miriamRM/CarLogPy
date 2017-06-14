##Imports
import sqlite3

##Constants
## Create tables
SQLCreateStyles = """CREATE TABLE IF NOT EXISTS Styles(
                Id 		INTEGER NOT NULL PRIMARY KEY,
                Style 		TEXT 	NOT NULL UNIQUE)"""
SQLCreateMakes = """CREATE TABLE IF NOT EXISTS Makes(
                Id 		INTEGER NOT NULL PRIMARY KEY,
                Make 		TEXT 	NOT NULL UNIQUE)"""
SQLCreateModel = """CREATE TABLE IF NOT EXISTS Model(
                Id 		INTEGER NOT NULL PRIMARY KEY,
                MakeId 		INTEGER NOT NULL,
                Model 		TEXT 	NOT NULL UNIQUE,
                FOREIGN KEY(MakeId) REFERENCES Makes(Id))"""
SQLCreateCars = """CREATE TABLE IF NOT EXISTS Cars(
                Id 		INTEGER NOT NULL PRIMARY KEY,
                MakeId 		INTEGER NOT NULL,
                ModelId 	INTEGER NOT NULL,
                Year 		INTEGER NOT NULL,
                StyleId 	INTEGER NOT NULL,
                FOREIGN KEY(StyleId) REFERENCES Styles(Id),
                FOREIGN KEY(MakeId) REFERENCES Makes(Id),
                FOREIGN KEY(ModelId) REFERENCES Model(Id))"""
SQLCreateSpecialty = """CREATE TABLE IF NOT EXISTS Specialty(
                Id 	  	INTEGER NOT NULL PRIMARY KEY,
                Specialty 	TEXT 	NOT NULL)"""
SQLCreateMechanic = """CREATE TABLE IF NOT EXISTS Mechanic(
                Id 		INTEGER NOT NULL PRIMARY KEY,
                WorkshopName 	TEXT 	NOT NULL,
                MechanicName 	TEXT 	NOT NULL,
                SpecialtyId 	INTEGER NOT NULL,
                Address 	TEXT,
                Phone 		INTEGER NOT NULL,
                FOREIGN KEY(SpecialtyId) REFERENCES Specialty(Id))"""
SQLCreateLog = """CREATE TABLE IF NOT EXISTS Log(
                Id 		INTEGER NOT NULL PRIMARY KEY,
                CarId 		INTEGER NOT NULL,
                MechanicId 	INTEGER NOT NULL,
                Problem 	TEXT 	NOT NULL,
                Solution 	TEXT 	NOT NULL,
                Date 		DATETIME NOT NULL, 
                NextDate 	DATETIME,
                FOREIGN KEY(CarId) REFERENCES Cars(Id),
                FOREIGN KEY(MechanicId) REFERENCES Mechanic(Id))"""
SQLCreate = [SQLCreateStyles, 
	SQLCreateMakes, 
	SQLCreateModel, 
	SQLCreateCars, 
	SQLCreateSpecialty, 
	SQLCreateMechanic, 
	SQLCreateLog]

## Fill Catalogs
CATALOGS = [["SUV", "PickUp", "Hatchback", "Van", "Sedan"],
	["Dodge", "Chrysler", "Ford", "Toyota", "Nissan", "Chevrolet", 
	"Pontiac"],
	["General", "Electrical", "Transmission", "Motor"],
	{"Caravan": 1, "Intrepid": 1, "Vibe": 7, "Town and Country": 2, 
	"Escape": 3, "Spark": 6, "Malibu": 6}]

SQLInsertStyles = """INSERT OR REPLACE INTO Styles(
		  Style) 
		  VALUES(?)"""
SQLInsertMakes = """INSERT OR REPLACE INTO Makes(
		  Make) 
		  VALUES(?)"""
SQLInsertSpecialty = """INSERT OR REPLACE INTO Specialty(
		  	Specialty) 
		  	VALUES(?)"""
SQLInsertModel = """INSERT OR REPLACE INTO Model(
		  MakeId,
		  Model) 
		  VALUES(?, ?)"""
SQLInsertCat = [SQLInsertStyles,
		SQLInsertMakes, 
		SQLInsertSpecialty, 
		SQLInsertModel]

##Functions
def createTables(conn, cursor):
	for sql in SQLCreate:
		try:
			cursor.execute(sql)
		except Exception as err:
			print "Error when creating tables" + err
		else:
			conn.commit()

def fillCatalogs(conn, cursor):
	for i in range(len(SQLInsertCat)):
		sql = SQLInsertCat[i]
		catalog = CATALOGS[i]
		try:
			if type(catalog) != dict:
				for j in range(len(catalog)):
					cursor.execute(sql, (catalog[j],))
			else:
				for key, val in catalog.items():
					cursor.execute(sql, (val, key))
		
		except Exception as err:
			print "Error when filling catalogs" + err
		
		else:
			conn.commit()


def handleDB():
	try:
		##Make the connection to the DB
		conn = sqlite3.connect("../data/CarLog.db")

	except Exception as err:
		print "Error" + err  

	else:
		##Cursor to handle DB
		cursor = conn.cursor()

		##Create all tables
		createTables(conn, cursor)

		##Fill the catalogs
		fillCatalogs(conn, cursor)
		print "Catalogs filled."

	finally:
		conn.close()

handleDB()
