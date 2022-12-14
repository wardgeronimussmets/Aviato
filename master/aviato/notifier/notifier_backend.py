import sqlite3

from .containers import Recipient,freeGame
    


def get_all_recipients():
    try:
        conn = sqlite3.connect(DB_REF)

        recipients = []
        results = conn.execute("Select * from " + TABLE_REC).fetchall()
        for row in results:
            id = row[0]
            name = row[1]
            mail = row[2]
            preference = row[3]
            recipients.append(Recipient(id,name,mail,preference))
        conn.close()
        return recipients
    except Exception as e:
        print(str(e))
        conn.close()
    
        
def remove_recipient(id):
    try:
        conn = sqlite3.connect(DB_REF)
        delete_statement = "delete FROM recipient where id=?"
        cursor = conn.cursor()
        cursor.execute(delete_statement,(str(id),))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(str(e))
        conn.close()

def add_recipient(name,mail):
    try:
        conn = sqlite3.connect(DB_REF)
        create_statement = "INSERT INTO " + TABLE_REC + " (Name,mail) VALUES (?,?)"
        cursor = conn.cursor()
        cursor.execute(create_statement,[name,mail])
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(str(e))
        conn.close()

def update_recipient(name,mail,id):
    try:
        conn = sqlite3.connect(DB_REF)
        update_statement = "UPDATE " + TABLE_REC + " SET Name = ?, mail = ? Where Id = ?"
        cursor = conn.cursor()
        cursor.execute(update_statement,[name,mail,id])
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(str(e))
        conn.close()

def update_preferences(string_json,id):
    try:
        conn = sqlite3.connect(DB_REF)
        update_statement = "UPDATE " + TABLE_REC + " SET preference = ? Where Id = ?"
        cursor = conn.cursor()
        cursor.execute(update_statement,[string_json,id])
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(str(e))
        conn.close()

def add_categories_if_not_exists(cats):
    try:
        conn = sqlite3.connect(DB_REF)
        #is defined in the category table that we want to have only unique categories
        insert_statement = "INSERT OR IGNORE INTO " + TABLE_CAT + " (category) VALUES (?);"
        cursor = conn.cursor()
        cursor.executemany(insert_statement,cats)
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(str(e))
        conn.close()

def get_categories():
    try:
        conn = sqlite3.connect(DB_REF)
        categories = []
        results = conn.execute("Select * from " + TABLE_CAT).fetchall()
        for row in results:
            cat = row[1]
            categories.append(cat)
        conn.close()
        return categories
    except Exception as e:
        print(str(e))
        conn.close()




CREATE_STATEMENT_RECIPIENT = """CREATE TABLE "recipient" (
	"Id"	INTEGER NOT NULL,
	"name"	TEXT NOT NULL,
	"mail"	TEXT NOT NULL,
	"preference"	TEXT NOT NULL DEFAULT '{"allowed":"all","exceptions":[]}',
	PRIMARY KEY("Id" AUTOINCREMENT)
)"""
CREATE_STATEMENT_CATEGORY = """CREATE TABLE "category" (
	"Id"	INTEGER,
	"category"	TEXT,
	PRIMARY KEY("Id" AUTOINCREMENT)
)"""
TABLE_REC = "recipient"
TABLE_CAT = "category"
DB_REF = "../notifier.db"