from era import *
from cy import *
import sqlite3
conn = sqlite3.connect('baseball.sqlite')
cur = conn.cursor()

eraorcy = input("Do you want to know about the Cy Young Award Winners or the ERA Leaders? [Type: CY or ERA] ")
eraorcy = eraorcy.upper()
if eraorcy == "ERA":
   col1 = 'Year'
   col2 = 'Leader'
   col3 = 'ERA'
   col4 = 'Team'
   sql = ''' CREATE TABLE IF NOT EXISTS era (
	"id"	INTEGER NOT NULL UNIQUE,
	"Year"	TEXT,
	"Leader"	TEXT,
	"ERA"	TEXT,
	"Team"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
)'''
   cur.execute(sql)
   e =  ERA()
   x = e.eraFunct(col1,col2,col3,col4)
   pieces = x.split('\n')
   print(x)
   pieces2 = pieces[1].split()
   leaderVar =  str(pieces2[1]).strip()  + " " + str(pieces2[2]).strip()
   cur.execute('SELECT id FROM era WHERE Year = ? and Leader = ? ', (pieces2[0],leaderVar))
   row = cur.fetchone()

   if row is None:
        yearVar = str(pieces2[0]).strip()
        eraVar = str(pieces2[3]).strip()
        try:
            teamVar = str(pieces2[4]).strip() + " " + str(pieces2[5]).strip()  + " " + str(pieces2[6]).strip()   + " " + str(pieces2[7]).strip()    + " " + str(pieces2[8]).strip()
        except:
            teamVar = str(pieces2[4]).strip() + " " + str(pieces2[5]).strip()  + " " + str(pieces2[6]).strip()   + " " + str(pieces2[7]).strip()
        cur.execute('''INSERT INTO era (Year, Leader, ERA, Team)
            VALUES (?, ?, ?, ? )''', (yearVar, leaderVar, eraVar, teamVar) )
        conn.commit()
        cur.close()
        print("Info added to the database")
   else:
        print("Item already in the database at row {}".format(row))
elif eraorcy == "CY":
    col1 = 'Year'
    col2 = 'Pitcher'
    col3 = 'Record[B]'
    col4 = 'Saves[C]'
    col5 = 'ERA'
    col6 = 'Team'
    sql = ''' CREATE TABLE IF NOT EXISTS cyyoung (
	"id"	INTEGER NOT NULL UNIQUE,
	"Year"	TEXT,
	"Pitcher"	TEXT,
	"Team"	TEXT,
	"Record"	TEXT,
	"Saves"	TEXT,
	"ERA"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
    )'''
    cur.execute(sql)
    c = CYYOUNG()
    y = c.cyFunct(col1,col2,col3,col4,col5,col6)
    pieces = y.split('\n')
    print(y)
    pieces2 = pieces[1].split()
    leaderVar =  str(pieces2[1]).strip()  + " " + str(pieces2[2]).strip()
    cur.execute('SELECT id FROM cyyoung WHERE Year = ? and Pitcher = ? ', (pieces2[0],leaderVar))
    row = cur.fetchone()
    if row is None:
        yearVar = str(pieces2[0]).strip()
        recordVar = str(pieces2[3]).strip()
        savesVar = str(pieces2[4]).strip()
        eraVar = str(pieces2[5]).strip()
        try:
            teamVar = str(pieces2[6]).strip() + " " + str(pieces2[7]).strip()  + " " + str(pieces2[8]).strip()   + " " + str(pieces2[9]).strip()    + " " + str(pieces2[10]).strip()
        except:
            teamVar = str(pieces2[6]).strip() + " " + str(pieces2[7]).strip()  + " " + str(pieces2[8]).strip()   + " " + str(pieces2[9]).strip()
        cur.execute('''INSERT INTO cyyoung (Year, Pitcher, Team, Record, Saves, ERA)
            VALUES (?, ?, ?, ?, ?, ? )''', (yearVar, leaderVar, teamVar, recordVar, savesVar, eraVar) )
        conn.commit()
        cur.close()
        print("Info added to the database")
        #print("{} {} {} {} {} {}".format(yearVar,leaderVar,recordVar,savesVar,eraVar,teamVar))
    else:
        print("Item already in the database at row {}".format(row))


else:
    print("You must type CY or ERA to select a function")
