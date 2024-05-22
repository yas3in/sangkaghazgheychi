import sqlite3

def create_table():
    db = sqlite3.connect("database.db")
    cur = db.cursor()
    cur.execute("""
                create table if not exists users(
                    username varchar(255) PRIMARY KEY,
                    password varchar(38),
                    email varchar(185)
                )
                """)
    db.commit()
    db.close()


def insert_valeus(tup):
    db = sqlite3.connect("database.db")
    cur = db.cursor()  
    cur.execute("""
                    insert into users(username, password, email) values(?, ?, ?) """, tup
                    )
    db.commit()
    db.close()
    
    
def login_select(username, password):
    users_list = []
    db = sqlite3.connect("database.db")
    cur = db.cursor()
    
    inserts = cur.execute("""
                select * from users
                
                
                """)
    for i in inserts:
            users_list.append(i)

    for i in users_list:
        if i[0] == username and i[1] == password:
            return True

   
    print(users_list)

    
    db.commit()
    db.close()
 
